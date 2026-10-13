from __future__ import annotations

from fastapi import APIRouter, HTTPException, status

from app.schemas.dashboard import DashboardRequest, DashboardResponse, ReportRequest, ReportResponse
from app.services.dashboard_service import build_dashboard, build_report

router = APIRouter(prefix="/dashboards", tags=["dashboards"])


@router.post("", response_model=DashboardResponse)
async def create_dashboard(payload: DashboardRequest) -> DashboardResponse:
    if not payload.title or not payload.title.strip():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Title is required")

    return DashboardResponse(**build_dashboard(payload.model_dump()))


@router.post("/report", response_model=ReportResponse)
async def create_report(payload: ReportRequest) -> ReportResponse:
    if not payload.title or not payload.title.strip():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Title is required")

    return ReportResponse(**build_report(payload.title, payload.metrics))
