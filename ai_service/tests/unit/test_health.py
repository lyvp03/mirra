"""GET /health with fake probes (the real Postgres/Redis path is covered by integration tests)."""

from __future__ import annotations

import asyncio

from fastapi import FastAPI
from fastapi.testclient import TestClient

from ai_service.api.health import get_probes


async def ok() -> None:
    return None


async def broken() -> None:
    raise ConnectionError("redis is down")


async def hangs() -> None:
    await asyncio.sleep(10)


def call_health(app: FastAPI, probes: dict) -> tuple[int, dict]:
    app.dependency_overrides[get_probes] = lambda: probes
    with TestClient(app) as client:
        response = client.get("/health")  # no Authorization header: health is public
    return response.status_code, response.json()


def test_all_up_is_200(app: FastAPI) -> None:
    status, body = call_health(app, {"postgres": ok, "redis": ok})
    assert status == 200
    assert body == {"status": "ok", "checks": {"postgres": "ok", "redis": "ok"}}


def test_one_down_is_503_with_details(app: FastAPI) -> None:
    status, body = call_health(app, {"postgres": ok, "redis": broken})
    assert status == 503
    assert body == {"status": "error", "checks": {"postgres": "ok", "redis": "down"}}


def test_slow_dependency_times_out_as_down(app: FastAPI, settings) -> None:
    app.state.settings = settings.model_copy(update={"health_timeout_seconds": 0.05})
    status, body = call_health(app, {"postgres": hangs, "redis": ok})
    assert status == 503
    assert body["checks"]["postgres"] == "down"
