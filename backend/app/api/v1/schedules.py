from __future__ import annotations

from fastapi import APIRouter, HTTPException, status

from app.schemas.integration import ScheduleRequest, ScheduleResponse
from app.services.scheduler_service import create_schedule

router = APIRouter(prefix="/schedules", tags=["schedules"])


@router.post("", response_model=ScheduleResponse)
async def create_schedule_route(payload: ScheduleRequest) -> ScheduleResponse:
    if not payload.name or not payload.name.strip():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Schedule name is required")

    return ScheduleResponse(**create_schedule(
        name=payload.name,
        cron_expression=payload.cron_expression,
        job_type=payload.job_type,
        organization_id=payload.organization_id,
        status=payload.status,
    ))
