"""Application errors rendered as RFC 9457 problem+json with a B5 `code` (B5 1-4, 7-1; B6 2).

Services raise `AppError(code)` and never `HTTPException` (B6 1-3). One set of handlers converts
AppError, request validation errors, Starlette HTTP errors and unhandled exceptions.
"""

from __future__ import annotations

import logging
from collections.abc import Iterable, Sequence
from dataclasses import dataclass
from typing import Any

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

logger = logging.getLogger(__name__)

PROBLEM_JSON = "application/problem+json"

# code -> (HTTP status, title). The generic group of B5 7-1 plus ADR 0001.
# Feature codes (CHAT_LIMIT_REACHED, QUOTA_EXCEEDED, ...) are added with their use case.
ERROR_CATALOG: dict[str, tuple[int, str]] = {
    "VALIDATION_ERROR": (422, "Validation error"),
    "UNAUTHENTICATED": (401, "Unauthenticated"),
    "FORBIDDEN": (403, "Forbidden"),
    "NOT_FOUND": (404, "Not found"),
    "RATE_LIMITED": (429, "Rate limited"),
    "FEATURE_DISABLED": (503, "Feature disabled"),
    "FILE_TOO_LARGE": (413, "File too large"),
    "UNSUPPORTED_FILE_TYPE": (415, "Unsupported file type"),
    # Not in B5, see docs/adr/0001-error-codes-outside-b5.md
    "METHOD_NOT_ALLOWED": (405, "Method not allowed"),
    "INTERNAL_ERROR": (500, "Internal error"),
    "AUTH_UNAVAILABLE": (503, "Authentication unavailable"),
}

# Starlette raises HTTPException for routing problems (404, 405); map statuses back to codes.
_CODE_BY_STATUS = {
    status: code
    for code, (status, _) in ERROR_CATALOG.items()
    if code not in {"FEATURE_DISABLED", "INTERNAL_ERROR", "AUTH_UNAVAILABLE"}
}

_LOCATIONS = {"body", "query", "path", "header", "cookie"}


@dataclass(frozen=True)
class FieldError:
    field: str
    message: str


class AppError(Exception):
    """Business error carrying a B5 `code`; its HTTP status comes from ERROR_CATALOG."""

    def __init__(
        self,
        code: str,
        detail: str = "",
        errors: Iterable[FieldError] = (),
        headers: dict[str, str] | None = None,
    ) -> None:
        if code not in ERROR_CATALOG:
            raise ValueError(f"Unknown error code {code!r}: add it to ERROR_CATALOG (B5 7-1)")
        super().__init__(f"{code}: {detail}" if detail else code)
        self.code = code
        self.status = ERROR_CATALOG[code][0]
        self.detail = detail
        self.errors = list(errors)
        self.headers = headers or {}


def problem_response(
    base_url: str,
    code: str,
    detail: str = "",
    errors: Sequence[FieldError] = (),
    headers: dict[str, str] | None = None,
    status: int | None = None,
) -> JSONResponse:
    default_status, title = ERROR_CATALOG[code]
    status = status or default_status
    body: dict[str, Any] = {
        "type": f"{base_url.rstrip('/')}/{code.lower().replace('_', '-')}",
        "title": title,
        "status": status,
        "code": code,
    }
    if detail:
        body["detail"] = detail  # for developers only (B5 1-4)
    if errors:
        body["errors"] = [{"field": e.field, "message": e.message} for e in errors]
    return JSONResponse(body, status_code=status, media_type=PROBLEM_JSON, headers=headers)


def field_path(loc: Sequence[str | int]) -> str:
    """("body", "lines", 0, "quantity") -> "lines[0].quantity" (format of the B5 example)."""
    parts = loc[1:] if loc and loc[0] in _LOCATIONS else loc
    path = ""
    for part in parts:
        if isinstance(part, int):
            path += f"[{part}]"
        else:
            path += f".{part}" if path else str(part)
    return path


def install_error_handlers(app: FastAPI, base_url: str) -> None:
    async def on_app_error(_: Request, exc: Exception) -> JSONResponse:
        assert isinstance(exc, AppError)
        return problem_response(base_url, exc.code, exc.detail, exc.errors, exc.headers)

    async def on_validation_error(_: Request, exc: Exception) -> JSONResponse:
        assert isinstance(exc, RequestValidationError)
        errors = [FieldError(field_path(e["loc"]), e["msg"]) for e in exc.errors()]
        return problem_response(base_url, "VALIDATION_ERROR", "Request validation failed", errors)

    async def on_http_error(_: Request, exc: Exception) -> JSONResponse:
        assert isinstance(exc, StarletteHTTPException)
        fallback = "INTERNAL_ERROR" if exc.status_code >= 500 else "VALIDATION_ERROR"
        code = _CODE_BY_STATUS.get(exc.status_code, fallback)
        detail = exc.detail if isinstance(exc.detail, str) else ""
        return problem_response(base_url, code, detail, headers=exc.headers, status=exc.status_code)

    async def on_unhandled(request: Request, exc: Exception) -> JSONResponse:
        # Logged with traceback; the client only gets a generic message.
        logger.exception("Unhandled error on %s %s", request.method, request.url.path)
        return problem_response(base_url, "INTERNAL_ERROR", "Unexpected error")

    app.add_exception_handler(AppError, on_app_error)
    app.add_exception_handler(RequestValidationError, on_validation_error)
    app.add_exception_handler(StarletteHTTPException, on_http_error)
    app.add_exception_handler(Exception, on_unhandled)
