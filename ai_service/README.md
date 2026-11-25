# ai_service

Mirra AI service (FastAPI + LangGraph, Python 3.12). Walking skeleton: health, JWT via JWKS,
problem+json errors, Alembic on schema `ai`. See `docs/plans/skeleton.md` at the repo root.

## Run locally

```bash
# from the repo root
docker compose up -d
uv run --project ai_service python scripts/dev_keys.py      # prints JWKS_URL

# from ai_service/
export ENV=dev JWKS_URL=<printed file:/// URL>
uv run alembic upgrade head
uv run uvicorn ai_service.main:create_app --factory --reload --port 8001
```

## Checks

```bash
uv run ruff check --fix && uv run ruff format
uv run lint-imports
uv run pytest -m "not integration"   # unit
uv run pytest -m integration         # needs docker compose services
```
