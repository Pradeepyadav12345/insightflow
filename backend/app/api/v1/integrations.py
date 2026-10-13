from __future__ import annotations

from fastapi import APIRouter, HTTPException, status

from app.schemas.integration import IntegrationRequest, IntegrationResponse
from app.services.integration_service import build_integration_summary

router = APIRouter(prefix="/integrations", tags=["integrations"])


@router.post("/register", response_model=IntegrationResponse)
async def register_integration(payload: IntegrationRequest) -> IntegrationResponse:
    if not payload.name or not payload.name.strip():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Integration name is required")

    return IntegrationResponse(**build_integration_summary(
        name=payload.name,
        connector_type=payload.connector_type,
        enabled=payload.enabled,
        status=payload.status,
        metadata=payload.metadata or {},
    ))
