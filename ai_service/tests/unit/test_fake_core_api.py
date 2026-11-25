"""FakeCoreApiClient serves the two skeleton calls from catalog.json and refuses the rest loudly."""

from __future__ import annotations

import pytest

from ai_service.adapters.core_api import CoreApiClient
from ai_service.core.errors import AppError
from ai_service.eval.fake_core_api import FakeCoreApiClient

DRESS_ID = "0b9a3c1e-1f2a-4c5d-8e7f-000000000001"
SHIRT_ID = "0b9a3c1e-1f2a-4c5d-8e7f-000000000002"


@pytest.fixture
def core() -> FakeCoreApiClient:
    return FakeCoreApiClient()


def test_fake_implements_the_interface(core: FakeCoreApiClient) -> None:
    assert isinstance(core, CoreApiClient)


async def test_get_product_by_slug(core: FakeCoreApiClient) -> None:
    product = await core.request("GET", "/products/dam-midi-hoa-nhi", token="user-token")
    assert product["id"] == DRESS_ID
    assert isinstance(product["price"], int)  # money is integer VND
    assert core.calls == [("GET", "/products/dam-midi-hoa-nhi", "user-token")]


async def test_unknown_slug_is_not_found(core: FakeCoreApiClient) -> None:
    with pytest.raises(AppError) as exc:
        await core.request("GET", "/products/khong-ton-tai", token=None)
    assert exc.value.code == "NOT_FOUND"


async def test_get_products_by_ids_keeps_order_and_skips_unknown(core: FakeCoreApiClient) -> None:
    page = await core.request("GET", f"/products?ids={SHIRT_ID},missing,{DRESS_ID}", token=None)
    assert [p["id"] for p in page["items"]] == [SHIRT_ID, DRESS_ID]
    assert page["total"] == 2 and page["page"] == 1


async def test_more_than_30_ids_is_a_validation_error(core: FakeCoreApiClient) -> None:
    ids = ",".join(f"id-{n}" for n in range(31))
    with pytest.raises(AppError) as exc:
        await core.request("GET", f"/products?ids={ids}", token=None)
    assert exc.value.code == "VALIDATION_ERROR"


@pytest.mark.parametrize(
    ("method", "path"),
    [("POST", "/cart/items"), ("GET", "/orders"), ("GET", "/products")],
)
async def test_other_calls_are_not_implemented(core: FakeCoreApiClient, method, path) -> None:
    with pytest.raises(NotImplementedError, match=f"{method} {path}"):
        await core.request(method, path, token="t")


async def test_internal_is_not_implemented(core: FakeCoreApiClient) -> None:
    with pytest.raises(NotImplementedError, match="internal /variants"):
        await core.internal("/variants", {"ids": "a"})
