"""Service settings from environment variables (and an optional .env file).

Variable names are not fixed by the design docs; see docs/plans/skeleton.md section 8.5.
"""

from __future__ import annotations

from typing import Literal

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env", "../.env"), env_file_encoding="utf-8", extra="ignore"
    )

    # Safe default: dev-only routes (me-check, OpenAPI docs) stay off unless ENV=dev.
    env: Literal["dev", "test", "prod"] = "prod"
    log_level: str = "INFO"

    # 127.0.0.1, not localhost: on Windows localhost tries ::1 first (compose publishes IPv4 only),
    # which costs ~2 s per new connection and trips the health-check timeout.
    database_url: str = "postgresql+asyncpg://mirra_ai:mirra_ai_dev@127.0.0.1:5432/mirra"
    redis_url: str = "redis://127.0.0.1:6379/0"
    health_timeout_seconds: float = 2.0

    # JWT issued by core-api (B5 2-1, 2-2). JWKS_URL accepts file:// (dev) and http(s)://.
    jwks_url: str = ""
    jwks_cache_ttl_seconds: float = 600  # B5: cache 10 minutes
    jwks_min_refresh_seconds: float = 30  # throttle for forced reloads on unknown kid
    jwks_timeout_seconds: float = 3.0
    jwt_issuer: str = "mirra-core"
    jwt_audience: str = "mirra-ai"

    # problem+json `type` = {ERROR_TYPE_BASE_URL}/{code-in-kebab-case} (B5 1-4)
    error_type_base_url: str = "https://mirra.example/errors"

    minio_endpoint: str = "127.0.0.1:9000"
    minio_access_key: str = ""
    minio_secret_key: SecretStr = SecretStr("")
