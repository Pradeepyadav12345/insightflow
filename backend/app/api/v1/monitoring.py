from __future__ import annotations

from fastapi import APIRouter

from app.schemas.monitoring import SystemHealthResponse
from app.services.monitoring_service import build_system_health

router = APIRouter(prefix="/monitoring", tags=["monitoring"])


@router.get("/health", response_model=SystemHealthResponse)
async def get_monitoring_health() -> SystemHealthResponse:
    return SystemHealthResponse(**build_system_health())
