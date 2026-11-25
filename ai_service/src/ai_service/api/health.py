"""GET /health (B3 5-3: every service has /health). No token; checks Postgres and Redis."""

from __future__ import annotations

import asyncio
import logging
from collections.abc import Awaitable, Callable
from typing import Annotated

from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncEngine

logger = logging.getLogger(__name__)
router = APIRouter(tags=["health"])

Probe = Callable[[], Awaitable[object]]


async def _ping_postgres(engine: AsyncEngine) -> None:
    async with engine.connect() as connection:
        await connection.execute(text("SELECT 1"))


def get_probes(request: Request) -> dict[str, Probe]:
    """One probe per dependency; overridden in unit tests."""
    engine, redis = request.app.state.engine, request.app.state.redis
    return {"postgres": lambda: _ping_postgres(engine), "redis": redis.ping}


async def _run(name: str, probe: Probe, limit_seconds: float) -> tuple[str, str]:
    try:
        async with asyncio.timeout(limit_seconds):
            await probe()
    except Exception:
        # Not swallowed: reported as "down" in the response and logged with the traceback.
        logger.warning("Health check %s failed", name, exc_info=True)
        return name, "down"
    return name, "ok"


@router.get("/health")
async def health(
    request: Request, probes: Annotated[dict[str, Probe], Depends(get_probes)]
) -> JSONResponse:
    timeout = request.app.state.settings.health_timeout_seconds
    results = await asyncio.gather(*(_run(name, probe, timeout) for name, probe in probes.items()))
    checks = dict(results)
    healthy = all(state == "ok" for state in checks.values())
    # A status report, not an error of the caller, so plain JSON rather than problem+json.
    return JSONResponse(
        {"status": "ok" if healthy else "error", "checks": checks},
        status_code=200 if healthy else 503,
    )
