# Mirra

Graduation thesis (ĐATN): women's fashion web shop + virtual try-on + AI agent.
Current phase: `ai_service` only. `core_api` and `web` do not exist yet.

## Design docs (READ-ONLY)
- Design docs live in `docs/design/` (written in Vietnamese). Never edit them.
- Read `docs/design/INDEX.md` first, open only the small files you need, never read the whole directory.
- If the code must deviate from the design: STOP, ask the user, then record the decision in `docs/adr/`.
- Per-UC implementation plans live in `docs/plans/`.

## ai_service
- FastAPI + LangGraph, Python 3.12.
- Use only the Postgres schema `ai`; never read the `core` schema.
- Data from core goes through `CoreApiClient`. For now use `FakeCoreApiClient` with fixtures.
- JWTs are RS256, signed by core. For now use a dev key pair; ai_service reads the JWKS via the `JWKS_URL` env var.
- Service-specific rules: see `ai_service/CLAUDE.md`.

## Commands
- Dev infrastructure (postgres + pgvector, redis, minio): `docker compose up -d`
- Inside `ai_service/`:
  - `uv run pytest -x`
  - `uv run ruff check --fix`
  - `uv run lint-imports`

## Conventions
- Class names, methods, endpoints and error codes must match design docs B5, B6, B7 exactly.
- Money is an integer in VND.
- User-facing text is in Vietnamese. Code comments and docs you write are in English.
- Never skip tests; never swallow exceptions just to make tests pass.
- When reporting a task as done, include the final test output.
- Conventional Commits, one change per commit.
