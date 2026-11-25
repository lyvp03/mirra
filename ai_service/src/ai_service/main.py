"""Composition root: builds the FastAPI app.

Run with: uv run uvicorn ai_service.main:create_app --factory --port 8001
"""

from __future__ import annotations

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from ai_service.api import dev, health
from ai_service.core.config import Settings
from ai_service.core.db import create_engine, create_sessionmaker
from ai_service.core.errors import install_error_handlers
from ai_service.core.logging import configure_logging
from ai_service.core.redis import create_redis
from ai_service.core.security import JwksProvider

API_PREFIX = "/ai/v1"  # B5 4-1: public prefix of ai-service


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    settings: Settings = app.state.settings
    engine = create_engine(settings)
    app.state.engine = engine
    app.state.sessionmaker = create_sessionmaker(engine)
    app.state.redis = create_redis(settings)
    try:
        yield
    finally:
        await app.state.redis.aclose()
        await engine.dispose()


def create_app(settings: Settings | None = None) -> FastAPI:
    settings = settings or Settings()
    configure_logging(settings.log_level)
    is_dev = settings.env == "dev"

    app = FastAPI(
        title="Mirra ai_service",
        lifespan=lifespan,
        docs_url=f"{API_PREFIX}/docs" if is_dev else None,
        openapi_url=f"{API_PREFIX}/openapi.json" if is_dev else None,
        redoc_url=None,
    )
    app.state.settings = settings
    app.state.jwks_provider = JwksProvider(
        settings.jwks_url,
        cache_ttl=settings.jwks_cache_ttl_seconds,
        min_refresh_interval=settings.jwks_min_refresh_seconds,
        timeout=settings.jwks_timeout_seconds,
    )
    install_error_handlers(app, settings.error_type_base_url)

    app.include_router(health.router)
    if is_dev:
        app.include_router(dev.router, prefix=API_PREFIX)
    return app
