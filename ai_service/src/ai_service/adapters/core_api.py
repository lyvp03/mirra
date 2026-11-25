"""CoreApiClient: the only way ai_service reads core data (B3 2-3, BR17).

Signature from B6 4-1 (assistant class diagram).
Deviations, see docs/adr/0002-core-api-client-async.md:
- methods are `async` (B6 draws plain methods; ai_service is async end to end);
- `json` defaults to None (B6 makes it required, meaningless for GET).
`request` has no query-parameter argument, so query strings go inside `path`
(e.g. "/products?ids=a,b"). Paths are relative to core's public prefix /api/v1 (B5 3).
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class CoreApiClient(ABC):
    @abstractmethod
    async def request(
        self, method: str, path: str, token: str | None, json: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Call a public core endpoint with the end user's access token (None for Guest)."""

    @abstractmethod
    async def internal(self, path: str, params: dict[str, Any]) -> dict[str, Any]:
        """Call core's /internal/v1 endpoints with the service key (B5 2-5, 4-2)."""
