"""Alembic on a real Postgres (docker compose / CI service), as the limited role mirra_ai."""

from __future__ import annotations

import asyncio
from pathlib import Path

import pytest
from alembic import command
from alembic.config import Config
from sqlalchemy import pool, text
from sqlalchemy.exc import DBAPIError
from sqlalchemy.ext.asyncio import create_async_engine

from tests.conftest import TEST_DATABASE_URL

pytestmark = pytest.mark.integration

AI_SERVICE_DIR = Path(__file__).resolve().parents[2]


def alembic_config() -> Config:
    config = Config(str(AI_SERVICE_DIR / "alembic.ini"))
    config.set_main_option("sqlalchemy.url", TEST_DATABASE_URL)
    return config


def query(sql: str) -> list:
    async def run() -> list:
        engine = create_async_engine(TEST_DATABASE_URL, poolclass=pool.NullPool)
        try:
            async with engine.connect() as connection:
                return list((await connection.execute(text(sql))).all())
        finally:
            await engine.dispose()

    return asyncio.run(run())


def db_state() -> tuple[bool, bool, list[str]]:
    has_schema = bool(query("SELECT 1 FROM information_schema.schemata WHERE schema_name = 'ai'"))
    has_vector = bool(query("SELECT 1 FROM pg_extension WHERE extname = 'vector'"))
    versions = [row[0] for row in query("SELECT version_num FROM ai.alembic_version")]
    return has_schema, has_vector, versions


def test_upgrade_downgrade_upgrade() -> None:
    config = alembic_config()

    command.upgrade(config, "head")
    assert db_state() == (True, True, ["0001"])

    command.downgrade(config, "base")
    # Schema and extension stay on purpose (see the migration docstring); only the version is gone.
    assert db_state() == (True, True, [])

    command.upgrade(config, "head")
    assert db_state() == (True, True, ["0001"])


def test_migrations_run_as_a_limited_role() -> None:
    # B3 5-2: one DB user per schema. If this ever runs as a superuser, privilege bugs stay hidden.
    [(user, is_superuser)] = query(
        "SELECT current_user, rolsuper FROM pg_roles WHERE rolname = current_user"
    )
    assert user == "mirra_ai"
    assert is_superuser is False


def test_limited_role_cannot_drop_the_extension() -> None:
    with pytest.raises(DBAPIError, match="must be owner"):
        query("DROP EXTENSION vector")
