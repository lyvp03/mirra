"""Dev-only routes. Registered by create_app() only when ENV=dev."""

from __future__ import annotations

from typing import Annotated, Any

from fastapi import APIRouter, Depends

from ai_service.core.security import AuthContext, get_auth_context

router = APIRouter(prefix="/dev", tags=["dev"])


@router.get("/me-check")
async def me_check(auth: Annotated[AuthContext, Depends(get_auth_context)]) -> dict[str, Any]:
    """Echo the verified JWT claims, to check the token pipeline end to end."""
    return auth.claims
