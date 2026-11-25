"""Redis client, created in the lifespan (streams, pub/sub, cache, rate limits later; B3 5-2)."""

from __future__ import annotations

from redis.asyncio import Redis

from ai_service.core.config import Settings


def create_redis(settings: Settings) -> Redis:
    # from_url does not connect; the first command does.
    return Redis.from_url(settings.redis_url, decode_responses=True, socket_timeout=5)
