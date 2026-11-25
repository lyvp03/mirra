"""Create schema ai and ensure extension vector. No business tables yet.

Revision ID: 0001
Revises:
Create Date: 2026-11-12

pgvector is not a trusted extension, so the limited role `mirra_ai` cannot create it.
It is created once by docker/postgres/init-ai.sh (superuser); here we only make sure it exists
and fail with a clear message otherwise (docs/plans/skeleton.md 8.1). If this migration happens
to run as a superuser, it creates the extension itself.
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "0001"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None

MISSING_VECTOR = (
    "Extension 'vector' is missing and the current DB role cannot create it (pgvector is not a "
    "trusted extension). Run docker/postgres/init-ai.sh as a superuser on this database; "
    "see docs/plans/skeleton.md section 8.1."
)


def _has_vector(bind: sa.Connection) -> bool:
    found = bind.execute(sa.text("SELECT 1 FROM pg_extension WHERE extname = 'vector'"))
    return found.scalar() is not None


def upgrade() -> None:
    op.execute("CREATE SCHEMA IF NOT EXISTS ai")
    bind = op.get_bind()
    if _has_vector(bind):
        return
    try:
        with bind.begin_nested():  # savepoint: a failure must not poison the migration transaction
            bind.execute(sa.text("CREATE EXTENSION IF NOT EXISTS vector"))
    except sa.exc.DBAPIError as exc:
        raise RuntimeError(MISSING_VECTOR) from exc


def downgrade() -> None:
    # Intentionally empty:
    # - schema `ai` holds the alembic_version table, so dropping it would break Alembic itself;
    # - extension `vector` is owned by the superuser that created it; `mirra_ai` cannot drop it.
    pass
