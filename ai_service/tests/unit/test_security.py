"""JWT RS256 verification through JWKS (B5 2-2) and the auth dependency."""

from __future__ import annotations

import asyncio
import json
import time
import uuid
from pathlib import Path

import dev_keys
import jwt
import pytest
from fastapi.testclient import TestClient

from ai_service.core.errors import AppError
from ai_service.core.security import (
    JwksProvider,
    JwksUnavailableError,
    Role,
    verify_token,
)
from ai_service.main import create_app
from tests.conftest import KID, build_settings

ISSUER, AUDIENCE = "mirra-core", "mirra-ai"
REQUIRED_CLAIMS = ["iss", "aud", "sub", "role", "email_verified", "iat", "exp", "jti"]


@pytest.fixture
def jwks(jwks_file: Path) -> JwksProvider:
    return JwksProvider(jwks_file.as_uri())


async def verify(token: str, provider: JwksProvider):
    return await verify_token(token, provider, issuer=ISSUER, audience=AUDIENCE)


async def assert_unauthenticated(token: str, provider: JwksProvider) -> None:
    with pytest.raises(AppError) as exc:
        await verify(token, provider)
    assert exc.value.code == "UNAUTHENTICATED"
    assert exc.value.status == 401


# --------------------------------------------------------------------------- the 4 required cases


async def test_valid_token_returns_current_user(make_token, jwks) -> None:
    user_id = str(uuid.uuid4())
    auth = await verify(make_token(sub=user_id, role="STAFF", email_verified=False), jwks)
    assert auth.user.id == uuid.UUID(user_id)
    assert auth.user.role is Role.STAFF
    assert auth.user.email_verified is False
    assert auth.claims["iss"] == ISSUER


async def test_wrong_signature_is_rejected(jwks) -> None:
    other_key = dev_keys.generate_keypair()
    forged = dev_keys.sign_token(other_key, KID)  # same kid, different key
    await assert_unauthenticated(forged, jwks)


async def test_expired_token_is_rejected(make_token, jwks) -> None:
    token = make_token(now=int(time.time()) - 3600, ttl_seconds=900)
    await assert_unauthenticated(token, jwks)


@pytest.mark.parametrize("claim", REQUIRED_CLAIMS)
async def test_missing_claim_is_rejected(make_token, jwks, claim: str) -> None:
    await assert_unauthenticated(make_token(drop=[claim]), jwks)


# --------------------------------------------------------------------------- other invalid tokens


@pytest.mark.parametrize(
    "overrides",
    [
        {"aud": ["mirra-core"]},  # not meant for ai_service
        {"iss": "someone-else"},
        {"role": "ROOT"},
        {"sub": "not-a-uuid"},
        {"email_verified": "yes"},
    ],
    ids=["aud", "iss", "role", "sub", "email_verified"],
)
async def test_invalid_claim_values_are_rejected(make_token, jwks, overrides) -> None:
    await assert_unauthenticated(make_token(overrides=overrides), jwks)


async def test_hs256_token_is_rejected(jwks) -> None:
    claims = {"iss": ISSUER, "aud": [AUDIENCE], "sub": str(uuid.uuid4())}
    token = jwt.encode(claims, "x" * 32, algorithm="HS256", headers={"kid": KID})
    await assert_unauthenticated(token, jwks)


async def test_garbage_token_is_rejected(jwks) -> None:
    await assert_unauthenticated("not.a.jwt", jwks)


# --------------------------------------------------------------------------- JWKS provider


async def test_unknown_kid_reloads_jwks_once(tmp_path: Path, signing_key) -> None:
    path = tmp_path / "jwks.json"
    path.write_text(json.dumps(dev_keys.build_jwks({KID: signing_key.public_key()})), "utf-8")
    provider = JwksProvider(path.as_uri())
    assert await provider.get_key(KID) is not None

    rotated = dev_keys.generate_keypair()  # core rotates: publishes the new key next to the old one
    keys = {KID: signing_key.public_key(), "kid-2": rotated.public_key()}
    path.write_text(json.dumps(dev_keys.build_jwks(keys)), "utf-8")

    auth = await verify(dev_keys.sign_token(rotated, "kid-2"), provider)
    assert auth.user.role is Role.CUSTOMER


async def test_forced_reload_is_throttled(jwks_file: Path, monkeypatch) -> None:
    now = [1000.0]
    provider = JwksProvider(jwks_file.as_uri(), min_refresh_interval=30, clock=lambda: now[0])
    loads = 0
    original = provider._load

    async def counting_load():
        nonlocal loads
        loads += 1
        return await original()

    monkeypatch.setattr(provider, "_load", counting_load)
    await provider.get_key("unknown-1")  # initial load + one forced reload
    await provider.get_key("unknown-2")  # within 30 s: no new reload
    assert loads == 2
    now[0] += 31
    await provider.get_key("unknown-3")
    assert loads == 3


async def test_concurrent_unknown_kids_trigger_a_single_load(jwks_file: Path, monkeypatch) -> None:
    provider = JwksProvider(jwks_file.as_uri())
    loads = 0
    original = provider._load

    async def slow_load():
        nonlocal loads
        loads += 1
        await asyncio.sleep(0.05)
        return await original()

    monkeypatch.setattr(provider, "_load", slow_load)
    await asyncio.gather(*(provider.get_key(KID) for _ in range(10)))
    assert loads == 1


async def test_missing_jwks_raises_unavailable(tmp_path: Path) -> None:
    provider = JwksProvider((tmp_path / "missing.json").as_uri())
    with pytest.raises(JwksUnavailableError):
        await provider.get_key(KID)


# --------------------------------------------------------------------------- HTTP: me-check

ME_CHECK = "/ai/v1/dev/me-check"


def test_me_check_without_token_is_401(client: TestClient) -> None:
    response = client.get(ME_CHECK)
    assert response.status_code == 401
    assert response.headers["content-type"].startswith("application/problem+json")
    assert response.json()["code"] == "UNAUTHENTICATED"
    assert response.headers["www-authenticate"] == "Bearer"


def test_me_check_with_valid_token_returns_claims(client: TestClient, make_token) -> None:
    user_id = str(uuid.uuid4())
    response = client.get(ME_CHECK, headers={"Authorization": f"Bearer {make_token(sub=user_id)}"})
    assert response.status_code == 200
    assert response.json()["sub"] == user_id


def test_me_check_with_expired_token_is_401(client: TestClient, make_token) -> None:
    token = make_token(now=int(time.time()) - 3600)
    response = client.get(ME_CHECK, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 401
    assert response.json()["code"] == "UNAUTHENTICATED"


def test_jwks_unavailable_is_503_not_401(tmp_path: Path, make_token) -> None:
    app = create_app(build_settings(jwks_url=(tmp_path / "missing.json").as_uri()))
    with TestClient(app, raise_server_exceptions=False) as client:
        response = client.get(ME_CHECK, headers={"Authorization": f"Bearer {make_token()}"})
    assert response.status_code == 503
    assert response.json()["code"] == "AUTH_UNAVAILABLE"  # ADR 0001


def test_me_check_is_not_registered_outside_dev(jwks_file: Path, make_token) -> None:
    app = create_app(build_settings(env="prod", jwks_url=jwks_file.as_uri()))
    with TestClient(app, raise_server_exceptions=False) as client:
        response = client.get(ME_CHECK, headers={"Authorization": f"Bearer {make_token()}"})
    assert response.status_code == 404
