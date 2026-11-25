#!/usr/bin/env python3
"""Dev RS256 key pair, JWKS and token signing for Mirra (stands in for core-api until it exists).

Usage (needs cryptography + PyJWT, provided by the ai_service environment):
    uv run --project ai_service python scripts/dev_keys.py              # create keys if missing
    uv run --project ai_service python scripts/dev_keys.py --force      # rotate keys
    uv run --project ai_service python scripts/dev_keys.py token --role ADMIN

Writes .dev-keys/private.pem and .dev-keys/jwks.json at the repo root (git-ignored) and prints the
`file:///...` URL to put in JWKS_URL. Claims follow B5 2-2 (iss, aud, sub, role, email_verified,
iat, exp, jti; header kid). The functions are also imported by the ai_service tests.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
import uuid
from collections.abc import Iterable
from pathlib import Path
from typing import Any

import jwt
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from jwt.algorithms import RSAAlgorithm

ISSUER = "mirra-core"
AUDIENCE = ["mirra-core", "mirra-ai"]
ACCESS_TTL_SECONDS = 15 * 60  # B5 2-1: access token lives 15 minutes
DEFAULT_DIR = Path(__file__).resolve().parents[1] / ".dev-keys"


def generate_keypair() -> rsa.RSAPrivateKey:
    return rsa.generate_private_key(public_exponent=65537, key_size=2048)


def private_pem(key: rsa.RSAPrivateKey) -> bytes:
    return key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )


def load_private_key(path: Path) -> rsa.RSAPrivateKey:
    key = serialization.load_pem_private_key(path.read_bytes(), password=None)
    if not isinstance(key, rsa.RSAPrivateKey):
        raise TypeError(f"{path} is not an RSA private key")
    return key


def build_jwks(public_keys: dict[str, rsa.RSAPublicKey]) -> dict[str, Any]:
    """JWKS document for {kid: public key}. Core publishes the current and previous key (B5 2-2)."""
    keys = []
    for kid, public_key in public_keys.items():
        jwk = RSAAlgorithm.to_jwk(public_key, as_dict=True)
        jwk.update({"kid": kid, "use": "sig", "alg": "RS256"})
        keys.append(jwk)
    return {"keys": keys}


def sign_token(
    private_key: rsa.RSAPrivateKey,
    kid: str,
    *,
    sub: str | None = None,
    role: str = "CUSTOMER",
    email_verified: bool = True,
    ttl_seconds: int = ACCESS_TTL_SECONDS,
    now: int | None = None,
    overrides: dict[str, Any] | None = None,
    drop: Iterable[str] = (),
) -> str:
    """Sign an access token like core would. `overrides`/`drop` build invalid tokens for tests."""
    issued_at = int(time.time()) if now is None else now
    claims: dict[str, Any] = {
        "iss": ISSUER,
        "aud": AUDIENCE,
        "sub": sub or str(uuid.uuid4()),
        "role": role,
        "email_verified": email_verified,
        "iat": issued_at,
        "exp": issued_at + ttl_seconds,
        "jti": str(uuid.uuid4()),
    }
    claims.update(overrides or {})
    for name in drop:
        claims.pop(name, None)
    return jwt.encode(claims, private_key, algorithm="RS256", headers={"kid": kid})


# --------------------------------------------------------------------------- CLI


def _ensure_keys(out: Path, force: bool) -> tuple[rsa.RSAPrivateKey, str]:
    pem, kid_file, jwks_file = out / "private.pem", out / "kid.txt", out / "jwks.json"
    if pem.exists() and kid_file.exists() and not force:
        return load_private_key(pem), kid_file.read_text(encoding="utf-8").strip()
    out.mkdir(parents=True, exist_ok=True)
    key, kid = generate_keypair(), f"dev-{uuid.uuid4().hex[:8]}"
    pem.write_bytes(private_pem(key))
    kid_file.write_text(kid, encoding="utf-8")
    jwks_file.write_text(
        json.dumps(build_jwks({kid: key.public_key()}), indent=2), encoding="utf-8"
    )
    return key, kid


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("--dir", type=Path, default=DEFAULT_DIR)
    parser.add_argument("--force", action="store_true", help="generate a new key pair")
    sub = parser.add_subparsers(dest="command")
    token = sub.add_parser("token", help="print a signed access token")
    token.add_argument("--role", default="CUSTOMER", choices=["CUSTOMER", "STAFF", "ADMIN"])
    token.add_argument("--sub", default=None, help="user id (UUID); random if omitted")
    token.add_argument("--unverified", action="store_true", help="email_verified=false")
    args = parser.parse_args(argv)

    key, kid = _ensure_keys(args.dir, args.force)
    if args.command == "token":
        print(
            sign_token(key, kid, sub=args.sub, role=args.role, email_verified=not args.unverified)
        )
    else:
        print(f"kid: {kid}")
        print(f"JWKS_URL={(args.dir / 'jwks.json').resolve().as_uri()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
