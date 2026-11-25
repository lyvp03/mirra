"""GET /health against the real Postgres and Redis from docker compose (or the CI services)."""

from __future__ import annotations

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

pytestmark = pytest.mark.integration


def test_health_with_real_postgres_and_redis(app: FastAPI) -> None:
    with TestClient(app) as client:
        response = client.get("/health")
    assert response.status_code == 200, response.text
    assert response.json() == {"status": "ok", "checks": {"postgres": "ok", "redis": "ok"}}
