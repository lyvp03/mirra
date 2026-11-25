"""AppError and framework errors are rendered as application/problem+json with a B5 `code`."""

from __future__ import annotations

from collections.abc import Iterator

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel

from ai_service.core.errors import AppError, FieldError

PROBLEM_JSON = "application/problem+json"


class Item(BaseModel):
    name: str
    quantity: int


@pytest.fixture
def error_client(app: FastAPI) -> Iterator[TestClient]:
    @app.get("/_test/app-error")
    async def app_error() -> None:
        raise AppError("FORBIDDEN", detail="role CUSTOMER cannot do this")

    @app.get("/_test/field-errors")
    async def field_errors() -> None:
        raise AppError(
            "VALIDATION_ERROR", errors=[FieldError("lines[0].quantity", "exceeds stock")]
        )

    @app.post("/_test/items")
    async def items(item: Item) -> Item:
        return item

    @app.get("/_test/crash")
    async def crash() -> None:
        raise RuntimeError("secret internals")

    with TestClient(app, raise_server_exceptions=False) as client:
        yield client


def assert_problem(response, status: int, code: str) -> dict:
    assert response.status_code == status
    assert response.headers["content-type"].startswith(PROBLEM_JSON)
    body = response.json()
    assert body["status"] == status
    assert body["code"] == code
    assert body["type"] == f"https://mirra.example/errors/{code.lower().replace('_', '-')}"
    assert body["title"]
    return body


def test_app_error_becomes_problem_json(error_client: TestClient) -> None:
    body = assert_problem(error_client.get("/_test/app-error"), 403, "FORBIDDEN")
    assert body["title"] == "Forbidden"
    assert body["detail"] == "role CUSTOMER cannot do this"
    assert "errors" not in body


def test_app_error_with_field_errors(error_client: TestClient) -> None:
    body = assert_problem(error_client.get("/_test/field-errors"), 422, "VALIDATION_ERROR")
    assert body["errors"] == [{"field": "lines[0].quantity", "message": "exceeds stock"}]


def test_pydantic_validation_error_maps_to_validation_error(error_client: TestClient) -> None:
    response = error_client.post("/_test/items", json={"quantity": "many"})
    body = assert_problem(response, 422, "VALIDATION_ERROR")
    fields = {error["field"] for error in body["errors"]}
    assert fields == {"name", "quantity"}


def test_unknown_route_is_not_found(error_client: TestClient) -> None:
    assert_problem(error_client.get("/_test/does-not-exist"), 404, "NOT_FOUND")


def test_wrong_method_is_method_not_allowed(error_client: TestClient) -> None:
    response = error_client.delete("/_test/app-error")
    assert_problem(response, 405, "METHOD_NOT_ALLOWED")  # ADR 0001
    assert "GET" in response.headers["allow"]


def test_unhandled_exception_is_internal_error_without_leaking(error_client: TestClient) -> None:
    response = error_client.get("/_test/crash")
    assert_problem(response, 500, "INTERNAL_ERROR")  # ADR 0001
    assert "secret internals" not in response.text


def test_unknown_code_is_rejected_at_raise_time() -> None:
    with pytest.raises(ValueError, match="NOT_A_CODE"):
        AppError("NOT_A_CODE")
