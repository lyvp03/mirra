# ADR 0002: CoreApiClient is async and `json` is optional

- Status: accepted (2026-11-12)
- Context: ai_service walking skeleton (`docs/plans/skeleton.md` section 5, 8.2)

## Context

B6 (`06-class-and-design-pattern/4-1-assistant-uc15-uc16-uc31.md`) is the only place that gives
`CoreApiClient` a signature:

```
+request(method: str, path: str, token: str | None, json: dict) dict
+internal(path: str, params: dict) dict
```

The class diagram draws plain (synchronous) methods and makes `json` required.

## Decision

```python
class CoreApiClient(ABC):
    async def request(self, method: str, path: str, token: str | None,
                      json: dict | None = None) -> dict: ...
    async def internal(self, path: str, params: dict) -> dict: ...
```

- `async`: ai_service is async end to end (FastAPI, asyncpg, LangGraph). A synchronous HTTP call
  inside a request would block the event loop for every other request.
- `json=None` by default: GET calls (`/products/{slug}`, `/products?ids=`) have no body.
- Names, parameters and return types otherwise match B6 exactly. `request` has no query-parameter
  argument, so query strings go inside `path`; adding a `params` argument was rejected to stay
  close to B6.

## Consequences

- Fakes (`FakeCoreApiClient`) and the future HTTP adapter implement the async interface.
- B6 should note `async` in its next revision.
