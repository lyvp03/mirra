"""Alembic environment for ai_service: async (asyncpg), schema `ai` only.

- URL: `sqlalchemy.url` if a caller set it (tests), otherwise DATABASE_URL from Settings.
- The version table lives in schema `ai` (B3 5-3: one version table per service, in its own schema),
  so the schema is created before Alembic touches the version table.
"""

import asyncio
from logging.config import fileConfig

from alembic import context
from sqlalchemy import pool, text
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import create_async_engine

from ai_service.core.config import Settings
from ai_service.models.base import SCHEMA, Base

config = context.config

if config.config_file_name is not None:
    # Keep the app's loggers alive when migrations run inside a test process.
    fileConfig(config.config_file_name, disable_existing_loggers=False)

target_metadata = Base.metadata


def _database_url() -> str:
    return config.get_main_option("sqlalchemy.url") or Settings().database_url


def _include_name(name: str | None, type_: str, parent_names: object) -> bool:
    """Autogenerate only looks at schema `ai`; schema `core` belongs to core-api."""
    return name == SCHEMA if type_ == "schema" else True


def _configure(**kwargs: object) -> None:
    context.configure(
        target_metadata=target_metadata,
        version_table_schema=SCHEMA,
        include_schemas=True,
        include_name=_include_name,
        **kwargs,
    )


def run_migrations_offline() -> None:
    _configure(url=_database_url(), literal_binds=True, dialect_opts={"paramstyle": "named"})
    with context.begin_transaction():
        context.execute(f"CREATE SCHEMA IF NOT EXISTS {SCHEMA}")
        context.run_migrations()


def do_run_migrations(connection: Connection) -> None:
    _configure(connection=connection)
    with context.begin_transaction():
        connection.execute(text(f"CREATE SCHEMA IF NOT EXISTS {SCHEMA}"))
        context.run_migrations()


async def run_async_migrations() -> None:
    engine = create_async_engine(_database_url(), poolclass=pool.NullPool)
    async with engine.connect() as connection:
        await connection.run_sync(do_run_migrations)
    await engine.dispose()


def run_migrations_online() -> None:
    asyncio.run(run_async_migrations())


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
