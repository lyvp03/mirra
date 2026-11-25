# ADR 0001: Error codes not listed in B5

- Status: accepted (2026-11-12)
- Context: ai_service walking skeleton (`docs/plans/skeleton.md` section 8.3, 8.4)

## Context

B5 (`05-api-contract-events/1-4-errors.md`, `7-1-error-codes.md`) requires every error to be
`application/problem+json` with a `code` from the table in 7.1. Three situations have no code there:

1. An unhandled exception (bug) -> HTTP 500.
2. A route called with the wrong method -> HTTP 405 (raised by Starlette routing).
3. The JWKS cannot be loaded (file missing, core-api down) while a token is presented.
   Returning 401 would blame the caller for an outage on our side; B5 1-4 reserves 502/503
   for external-service failures but has no matching code.

Using FastAPI's defaults for these would return `{"detail": ...}`, breaking the "every error is
problem+json with a code" rule that clients rely on.

## Decision

Add three codes, used only by ai_service until core-api adopts them:

| code | status | when |
|---|---|---|
| `INTERNAL_ERROR` | 500 | unhandled exception; logged with traceback, generic `detail` |
| `METHOD_NOT_ALLOWED` | 405 | wrong HTTP method; `Allow` header kept |
| `AUTH_UNAVAILABLE` | 503 | signing keys (JWKS) cannot be loaded and none are cached |

They live in `ai_service.core.errors.ERROR_CATALOG` under a comment pointing to this ADR.

## Consequences

- Clients can handle every response from ai_service with one problem+json parser.
- B5 7.1 should list these codes in its next revision (owner: design docs, read-only for code).
- `FEATURE_DISABLED` (503) was rejected for case 3: it means a feature was switched off by config,
  which would mislead operators.
