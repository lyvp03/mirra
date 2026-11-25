"""JWT RS256 verification through JWKS (B5 2-1, 2-2) and the FastAPI auth dependencies.

core-api signs access tokens; ai_service only verifies them (it never issues tokens).
"""

from __future__ import annotations

import asyncio
import json
import logging
import time
from collections.abc import Callable
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path
from typing import Annotated, Any
from urllib.parse import urlsplit
from urllib.request import url2pathname
from uuid import UUID

import httpx
import jwt
from fastapi import Depends, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from ai_service.core.errors import AppError

logger = logging.getLogger(__name__)

ALGORITHM = "RS256"
REQUIRED_CLAIMS = ["iss", "aud", "sub", "role", "email_verified", "iat", "exp", "jti"]


class Role(StrEnum):
    CUSTOMER = "CUSTOMER"
    STAFF = "STAFF"
    ADMIN = "ADMIN"


@dataclass(frozen=True)
class CurrentUser:
    """B6 2: built from the JWT at the api layer and passed down to services."""

    id: UUID
    role: Role
    email_verified: bool


@dataclass(frozen=True)
class AuthContext:
    user: CurrentUser
    claims: dict[str, Any]
    token: str  # forwarded to core through CoreApiClient (BR17); never stored


class JwksUnavailableError(Exception):
    """The JWKS document could not be loaded (file missing, core down, bad JSON)."""


class JwksProvider:
    """Loads and caches the JWKS from JWKS_URL (file:// or http(s)://).

    - Cache for `cache_ttl` seconds (B5: 10 minutes).
    - Unknown `kid` -> one forced reload, at most once per `min_refresh_interval` seconds,
      so tokens with random kids cannot hammer core.
    - A lock makes concurrent requests share a single load.
    - If a refresh fails but keys are cached, keep serving them and retry later.
    """

    def __init__(
        self,
        url: str,
        *,
        cache_ttl: float = 600,
        min_refresh_interval: float = 30,
        timeout: float = 3.0,
        clock: Callable[[], float] = time.monotonic,
    ) -> None:
        self._url = url
        self._ttl = cache_ttl
        self._min_interval = min_refresh_interval
        self._timeout = timeout
        self._clock = clock
        self._keys: dict[str, jwt.PyJWK] | None = None
        self._loaded_at = float("-inf")
        self._last_forced = float("-inf")
        self._lock = asyncio.Lock()

    async def get_key(self, kid: str) -> jwt.PyJWK | None:
        if self._keys is None or self._clock() - self._loaded_at >= self._ttl:
            await self._refresh(seen=self._loaded_at)
        key = (self._keys or {}).get(kid)
        if key is not None or self._clock() - self._last_forced < self._min_interval:
            return key
        self._last_forced = self._clock()
        await self._refresh(seen=self._loaded_at)
        return (self._keys or {}).get(kid)

    async def _refresh(self, seen: float) -> None:
        async with self._lock:
            if self._loaded_at != seen:
                return  # another request refreshed while we waited for the lock
            try:
                self._keys = await self._load()
            except JwksUnavailableError:
                if self._keys is None:
                    raise
                logger.warning("JWKS refresh failed; keeping cached keys", exc_info=True)
                self._loaded_at = self._clock() - self._ttl + self._min_interval
                return
            self._loaded_at = self._clock()

    async def _load(self) -> dict[str, jwt.PyJWK]:
        try:
            raw = await self._read()
            jwk_set = jwt.PyJWKSet.from_dict(json.loads(raw))
        except (OSError, httpx.HTTPError, ValueError, jwt.PyJWKError, jwt.PyJWKSetError) as exc:
            raise JwksUnavailableError(f"Cannot load JWKS from {self._url!r}: {exc}") from exc
        return {key.key_id: key for key in jwk_set.keys if key.key_id}

    async def _read(self) -> str:
        parts = urlsplit(self._url)
        if parts.scheme == "file":
            path = Path(url2pathname(parts.path))
            return await asyncio.to_thread(path.read_text, "utf-8")
        if parts.scheme in {"http", "https"}:
            async with httpx.AsyncClient(timeout=self._timeout) as client:
                response = await client.get(self._url)
                response.raise_for_status()
                return response.text
        raise JwksUnavailableError(
            f"Unsupported JWKS_URL {self._url!r} (use file:// or http(s)://)"
        )


def _unauthenticated(detail: str) -> AppError:
    return AppError("UNAUTHENTICATED", detail, headers={"WWW-Authenticate": "Bearer"})


async def verify_token(
    token: str, jwks: JwksProvider, *, issuer: str, audience: str
) -> AuthContext:
    """Verify signature, alg, iss, aud, exp and the B5 claims. Raises AppError(UNAUTHENTICATED).

    JwksUnavailableError propagates: an outage of the key source is not the caller's fault.
    """
    try:
        header = jwt.get_unverified_header(token)
    except jwt.PyJWTError as exc:
        raise _unauthenticated("Malformed token") from exc
    kid = header.get("kid")
    if header.get("alg") != ALGORITHM or not isinstance(kid, str):
        raise _unauthenticated("Token must be RS256 with a kid header")
    key = await jwks.get_key(kid)
    if key is None:
        raise _unauthenticated("Unknown signing key")
    try:
        claims = jwt.decode(
            token,
            key.key,
            algorithms=[ALGORITHM],
            audience=audience,
            issuer=issuer,
            options={"require": REQUIRED_CLAIMS},
        )
    except jwt.PyJWTError as exc:
        raise _unauthenticated(str(exc)) from exc
    return AuthContext(user=_current_user(claims), claims=claims, token=token)


def _current_user(claims: dict[str, Any]) -> CurrentUser:
    try:
        user_id, role = UUID(str(claims["sub"])), Role(claims["role"])
    except ValueError as exc:
        raise _unauthenticated("Invalid sub or role claim") from exc
    if not isinstance(claims["email_verified"], bool):
        raise _unauthenticated("Claim email_verified must be a boolean")
    return CurrentUser(id=user_id, role=role, email_verified=claims["email_verified"])


# --------------------------------------------------------------------------- FastAPI dependencies

_bearer = HTTPBearer(auto_error=False)


async def get_auth_context(
    request: Request,
    credentials: Annotated[HTTPAuthorizationCredentials | None, Depends(_bearer)],
) -> AuthContext:
    if credentials is None:
        raise _unauthenticated("Missing bearer token")
    settings = request.app.state.settings
    try:
        return await verify_token(
            credentials.credentials,
            request.app.state.jwks_provider,
            issuer=settings.jwt_issuer,
            audience=settings.jwt_audience,
        )
    except JwksUnavailableError as exc:
        logger.error("JWKS unavailable: %s", exc)
        raise AppError("AUTH_UNAVAILABLE", "Signing keys cannot be loaded") from exc


async def get_current_user(
    auth: Annotated[AuthContext, Depends(get_auth_context)],
) -> CurrentUser:
    return auth.user
