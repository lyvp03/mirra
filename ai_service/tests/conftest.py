"""Shared fixtures: ephemeral RSA keys + JWKS file, settings, app and HTTP client.

Keys are generated per test session (never read from .dev-keys/), reusing scripts/dev_keys.py.
"""

from __future__ import annotations

import json
import os
import sys
from collections.abc import Callable, Iterator
from pathlib import Path

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import dev_keys  # noqa: E402

from ai_service.core.config import Settings  # noqa: E402
from ai_service.main import create_app  # noqa: E402

KID = "test-kid-1"
TEST_DATABASE_URL = os.environ.get(
    "TEST_DATABASE_URL", "postgresql+asyncpg://mirra_ai:mirra_ai_dev@127.0.0.1:5432/mirra_test"
)
TEST_REDIS_URL = os.environ.get("TEST_REDIS_URL", "redis://127.0.0.1:6379/15")


@pytest.fixture(scope="session")
def signing_key():
    return dev_keys.generate_keypair()


@pytest.fixture(scope="session")
def jwks_file(tmp_path_factory: pytest.TempPathFactory, signing_key) -> Path:
    path = tmp_path_factory.mktemp("jwks") / "jwks.json"
    path.write_text(json.dumps(dev_keys.build_jwks({KID: signing_key.public_key()})), "utf-8")
    return path


@pytest.fixture
def make_token(signing_key) -> Callable[..., str]:
    def _make(**kwargs) -> str:
        return dev_keys.sign_token(signing_key, KID, **kwargs)

    return _make


def build_settings(**overrides) -> Settings:
    values = {
        "env": "dev",
        "database_url": TEST_DATABASE_URL,
        "redis_url": TEST_REDIS_URL,
        "jwks_url": "",
        "error_type_base_url": "https://mirra.example/errors",
    }
    values.update(overrides)
    return Settings(_env_file=None, **values)


@pytest.fixture
def settings(jwks_file: Path) -> Settings:
    return build_settings(jwks_url=jwks_file.as_uri())


@pytest.fixture
def app(settings: Settings) -> FastAPI:
    return create_app(settings)


@pytest.fixture
def client(app: FastAPI) -> Iterator[TestClient]:
    # raise_server_exceptions=False: assert on the 500 problem+json instead of re-raising.
    with TestClient(app, raise_server_exceptions=False) as test_client:
        yield test_client
