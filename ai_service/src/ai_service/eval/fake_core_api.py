"""In-memory CoreApiClient backed by data/seed/catalog.json.

Implements only what the skeleton needs:
- GET /products/{slug}
- GET /products?ids=a,b (at most 30 ids, B5 3-2), returned in the B5 page shape.
Anything else raises NotImplementedError naming the call, so a missing fake is obvious in tests.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, urlsplit

from ai_service.adapters.core_api import CoreApiClient
from ai_service.core.errors import AppError, FieldError

# src/ai_service/eval/fake_core_api.py -> ai_service/data/seed/catalog.json
DEFAULT_CATALOG = Path(__file__).resolve().parents[3] / "data" / "seed" / "catalog.json"
MAX_IDS = 30
_SLUG_PATH = re.compile(r"/products/(?P<slug>[a-z0-9]+(?:-[a-z0-9]+)*)")


class FakeCoreApiClient(CoreApiClient):
    def __init__(self, catalog_path: Path = DEFAULT_CATALOG) -> None:
        products = json.loads(catalog_path.read_text(encoding="utf-8"))["products"]
        self._by_slug: dict[str, dict[str, Any]] = {p["slug"]: p for p in products}
        self._by_id: dict[str, dict[str, Any]] = {p["id"]: p for p in products}
        self.calls: list[tuple[str, str, str | None]] = []  # for assertions in tests

    async def request(
        self, method: str, path: str, token: str | None, json: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        self.calls.append((method.upper(), path, token))
        url = urlsplit(path)
        if method.upper() == "GET" and url.path == "/products" and "ids" in parse_qs(url.query):
            return self._products_by_ids(parse_qs(url.query)["ids"][0])
        match = _SLUG_PATH.fullmatch(url.path)
        if method.upper() == "GET" and match:
            return self._product_by_slug(match["slug"])
        raise NotImplementedError(
            f"FakeCoreApiClient does not implement {method.upper()} {path} yet"
        )

    async def internal(self, path: str, params: dict[str, Any]) -> dict[str, Any]:
        raise NotImplementedError(f"FakeCoreApiClient does not implement internal {path} yet")

    def _product_by_slug(self, slug: str) -> dict[str, Any]:
        product = self._by_slug.get(slug)
        if product is None:
            raise AppError("NOT_FOUND", f"Product {slug!r} not found")
        return product

    def _products_by_ids(self, raw_ids: str) -> dict[str, Any]:
        ids = [i for i in raw_ids.split(",") if i]
        if len(ids) > MAX_IDS:
            raise AppError("VALIDATION_ERROR", errors=[FieldError("ids", f"at most {MAX_IDS} ids")])
        items = [self._by_id[i] for i in ids if i in self._by_id]  # unknown ids are skipped
        return {"items": items, "page": 1, "page_size": len(items), "total": len(items)}
