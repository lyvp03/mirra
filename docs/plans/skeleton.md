# Plan: ai_service walking skeleton (rev 2)

No use case yet. Goal: an app that boots, talks to Postgres and Redis, verifies RS256 JWTs through JWKS,
returns `application/problem+json` errors, and has CI. Design sources are cited as `B3/B5/B6` plus the small file name under `docs/design/`.

Rev 2 changes: health path follows B3; `dev_keys.py` at the root as requested; ADR for the 500 code;
deviations from B6 stated; pgvector privilege verified; dev/CI privilege parity; Starlette 404/405; JWKS outage, lock;
engine in lifespan; health failure case; complete import-linter contracts; configurable host ports.

## 1. Files to create

Repo root:
- `docker-compose.yml`: postgres (`pgvector/pgvector:pg17`), redis (`redis:7-alpine`, AOF on), minio. Healthchecks on all three
  (`pg_isready`, `redis-cli ping`, `mc ready local`), named volumes (`pg_data`, `redis_data`, `minio_data`),
  ports bound to `127.0.0.1` and overridable (`POSTGRES_PORT`, `REDIS_PORT`, `MINIO_PORT`, `MINIO_CONSOLE_PORT`), console dev-only.
  Every `${VAR:-default}` has a default, so `docker compose up -d` works without a `.env`.
  No ai_service container in this step: the app runs on the host with `uv run` (B3 5-5 dev-in-container comes later).
- `docker/postgres/init-ai.sh`: runs as superuser; creates role `mirra_ai` (password from env), grants `CREATE` on the database
  (so the ai side creates its own schema), and runs `CREATE EXTENSION IF NOT EXISTS vector` (see 8.1).
  Mounted into `/docker-entrypoint-initdb.d/` for dev; CI runs the same script with `psql` (see section 7).
- `.env.example` (no real `.env`). `.gitignore`: add `.dev-keys/`.
- `scripts/dev_keys.py` (as requested): `generate_keypair()`, `build_jwks()`, `sign_token(claims, ...)`; CLI writes
  `.dev-keys/private.pem`, `.dev-keys/jwks.json` and prints the absolute `file:///...` URL for `JWKS_URL`.
  Run with `uv run --project ai_service python scripts/dev_keys.py` (needs cryptography + PyJWT from ai_service).
  Keys sit at the root because they belong to the issuer (core) and core will reuse them.
- `docs/adr/0001-internal-error-code.md` (see 8.3).
- `.github/workflows/ci.yml`

`ai_service/` (created with `uv init --package`, Python 3.12):
```
pyproject.toml            deps, ruff (C901 max 10), pytest markers, import-linter contracts
alembic.ini
migrations/env.py         async env; CREATE SCHEMA IF NOT EXISTS ai before configuring; version_table_schema="ai"
migrations/versions/0001_create_ai_schema_and_vector.py
data/seed/catalog.json    provisional fixture for FakeCoreApiClient
src/ai_service/
  main.py                 create_app(settings): lifespan creates engine + redis, registers handlers, routers; me-check only if ENV=dev
  core/config.py          Settings (pydantic-settings); get_settings dependency
  core/db.py              engine/sessionmaker built in lifespan (never at import time), get_session
  core/redis.py           redis.asyncio client built in lifespan
  core/logging.py
  core/errors.py          AppError, FieldError, problem+json handlers (AppError, RequestValidationError, Starlette HTTPException, Exception)
  core/security.py        JwksProvider, verify_token, CurrentUser, Role, get_current_user dependency
  models/base.py          DeclarativeBase, MetaData(schema="ai"); no tables yet
  adapters/core_api.py    CoreApiClient (ABC)
  eval/fake_core_api.py   FakeCoreApiClient (B3 puts fakes in package `eval`)
  api/health.py           GET /health
  api/dev.py              GET /ai/v1/dev/me-check (dev only)
tests/conftest.py         ephemeral RSA keys in tmp_path (reusing scripts/dev_keys.py functions), app/client fixtures
tests/unit/               test_errors.py, test_security.py, test_health.py, test_fake_core_api.py
tests/integration/        test_health.py, test_migrations.py
```
Not created (nothing uses them yet): `services`, `repositories`, `domain`, `schemas`, `agent`, `workers`.

## 2. Libraries (latest on PyPI today; `uv lock` pins them)
fastapi 0.162.5, uvicorn 0.54.0, sqlalchemy[asyncio] 2.1.8, asyncpg 0.32.0, alembic 1.20.1,
pydantic 2.14.3, pydantic-settings 2.16.2, pyjwt[crypto] 2.15.1 (cryptography 50.0.2), httpx 0.28.1, redis 8.1.0.
Dev: pytest 9.2.0, pytest-asyncio 1.4.1.post1, import-linter 2.16, ruff 0.17.4. Not yet: langgraph.
The context7 MCP is not available in this session; API details (SQLAlchemy 2.1, import-linter optional layers,
pytest-asyncio loop scope) will be checked against official docs on the web, and the tests will catch any mismatch.

## 3. JWT (B5 `2-2-jwt-claims`, `2-1-access-and-refresh-tokens`)
- Algorithms allow-list: `["RS256"]` (rejects `none`/HS*). Header `kid` required.
- Required claims: `iss="mirra-core"`, `aud` contains `"mirra-ai"`, `sub` (must parse as UUID), `role` in `CUSTOMER|STAFF|ADMIN`,
  `email_verified` (bool), `iat`, `exp`, `jti`. Leeway 0 (not specified by B5).
- Any token problem -> `401 UNAUTHENTICATED`, problem+json, header `WWW-Authenticate: Bearer`.
- `JwksProvider`: `JWKS_URL` accepts `file://` (dev) and `http(s)://` (core later, `/api/v1/.well-known/jwks.json`).
  Cache 10 minutes (B5). Unknown `kid` -> one forced reload, at most once every 30 s (my addition).
  An `asyncio.Lock` ensures concurrent requests trigger a single fetch. HTTP timeout 3 s.
- JWKS cannot be loaded (file missing, core down) -> NOT a 401; see 8.4.
- `CurrentUser{id: UUID, role: Role, email_verified: bool}` (B6 `2-shared-base-classes`).

## 4. Errors (B5 `1-4-errors`, `7-1-error-codes`)
Fields: `type` (`{ERROR_TYPE_BASE_URL}/{code-in-kebab-case}`), `title`, `status`, `code`, `detail`, optional `errors[{field, message}]`.
Media type `application/problem+json`. Services raise `AppError(code)`, never `HTTPException` (B6 `1-3-design-rules`).

| Source | Status | `code` |
|---|---|---|
| `AppError` | its own | its own |
| Pydantic `RequestValidationError` | 422 | `VALIDATION_ERROR`, `errors[]` filled |
| Starlette 404 (unknown route) | 404 | `NOT_FOUND` |
| Starlette 405 (wrong method) | 405 | no B5 code -> see 8.3 |
| Bad/missing token | 401 | `UNAUTHENTICATED` |
| Unhandled exception | 500 | `INTERNAL_ERROR` (ADR 0001); logged with traceback, `detail` generic |

## 5. CoreApiClient (B6 `4-1-assistant`, the only place with a signature)
```
class CoreApiClient(ABC):
    async def request(self, method: str, path: str, token: str | None, json: dict | None = None) -> dict
    async def internal(self, path: str, params: dict) -> dict
```
Deviations from B6, stated explicitly: (a) `async` (B6 draws plain methods; the app is async end to end);
(b) `json` defaults to `None` (B6 makes it required, which is meaningless for GET). Both are recorded in ADR 0002 (see 8.2).
The query string for `?ids=` goes inside `path`, since `request` has no `params` argument.
`FakeCoreApiClient` implements `GET /products/{slug}` and `GET /products?ids=a,b` (max 30, per B5) from `catalog.json`;
unknown slug -> `AppError("NOT_FOUND")`; any other call -> `NotImplementedError("FakeCoreApiClient does not implement <METHOD> <path> yet")`.

## 6. Endpoints
- `GET /health` (B3 5-3: "every service has `/health`"; container healthchecks do not go through Caddy). No token.
  Checks Postgres (`SELECT 1`) and Redis (`PING`), each with a 2 s timeout.
  All up: `200 {"status":"ok","checks":{"postgres":"ok","redis":"ok"}}`.
  Any down: `503 {"status":"error","checks":{"postgres":"ok","redis":"down"}}` (plain JSON: a status report, not an error of the caller).
- `GET /ai/v1/dev/me-check`: requires token, returns the verified claims; registered only when `ENV=dev`.

## 7. Quality gates and CI
- ruff: `select` includes `C901`, `max-complexity = 10`; `ruff format --check` in CI.
- import-linter contracts:
  1. layers: `api` > `(services)` > `(repositories)` > `models`, with optional layers in parentheses
     (syntax to verify; fallback: create those packages empty).
  2. forbidden: `ai_service.domain` must not import `ai_service.adapters`, `ai_service.api`, `fastapi`, `sqlalchemy` (if `domain` is absent, the contract is added with the first domain class).
  3. forbidden: no module except tests may import `ai_service.eval` (B3).
  4. forbidden: `ai_service.core` must not import `api`, `adapters`, `eval` (core is the base everyone uses).
  `adapters` may import `core` only.
- CI job `ai_service` (`working-directory: ai_service`): setup-uv, `uv sync --locked`, ruff check, ruff format --check, lint-imports,
  pytest unit; then services `pgvector/pgvector:pg17` and `redis:7-alpine` with health options, a step
  `psql -f`/`bash docker/postgres/init-ai.sh` as superuser so CI uses the same `mirra_ai` role as dev, `alembic upgrade head`, pytest integration.
- Root `tests/` (doc-splitting tool) stays out of this job.

## 8. Decisions and open points
1. **pgvector privilege (verified).** `vector.control` (0.8.7) has no `trusted = true`, so only a superuser can create it; `mirra_ai` cannot.
   Decision: `init-ai.sh` (superuser) creates the extension. Migration 0001 runs `CREATE SCHEMA IF NOT EXISTS ai` and
   `CREATE EXTENSION IF NOT EXISTS vector` (a no-op when already present; I will confirm it does not need superuser in that case),
   then checks the extension exists and fails with a clear message if not.
   Downgrade: drops nothing. The schema holds the Alembic version table, and the extension is owned by the superuser.
   The integration test still runs upgrade -> downgrade base -> upgrade.
   Alternative (not chosen): a separate privileged "migrator" DB role. That is closer to "the migration creates everything",
   but it adds a third DB user that B3 does not mention.
2. **ADR 0002: CoreApiClient async + optional `json`.** Small deviation from B6; I need your OK.
3. **ADR 0001: `INTERNAL_ERROR` (500) and 405.** B5 has neither. Proposal: `INTERNAL_ERROR` for 500, and `METHOD_NOT_ALLOWED` for 405.
   Both go in the same ADR. Your call; the alternative is FastAPI defaults (not problem+json).
4. **JWKS unavailable.** Not specified. Proposal: `503` problem+json with `code: FEATURE_DISABLED`?  It fits poorly.
   Better: include it in ADR 0001 as `AUTH_UNAVAILABLE` 503. Your call.
5. **Env variable names** (not in design): `ENV` (dev|test|prod), `DATABASE_URL`, `REDIS_URL`, `JWKS_URL`, `ERROR_TYPE_BASE_URL`
   (default `https://mirra.example/errors`), `MINIO_ENDPOINT`, `MINIO_ACCESS_KEY`, `MINIO_SECRET_KEY`, plus compose-only
   `POSTGRES_*`, `AI_DB_PASSWORD` and host ports.
6. **catalog.json shape** (not in design): provisional `id, slug, name, category, price` (integer VND),
   `variants[{id, color, size, in_stock, effective_price}]`, `images`; 6 products. To be aligned when core exists.
7. **me-check path** (not in design): `/ai/v1/dev/me-check`.

## 9. Order of work and final verification
1. Scaffold (uv init, pyproject, compose), no app code.
2. Tests for sections 3 and 4 first; run them and show RED.
3. Code until green; then health, Fake, Alembic, CI.
4. Run and paste output: `docker compose up -d`, `uv run alembic upgrade head`, all tests (unit + integration), ruff, lint-imports,
   `GET /health`, `GET /ai/v1/dev/me-check` with and without a token. No commit.
