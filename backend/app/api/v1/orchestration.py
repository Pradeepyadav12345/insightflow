from __future__ import annotations

from fastapi import APIRouter, HTTPException, status

from app.schemas.orchestration import OrchestrationRequest, OrchestrationResponse
from app.services.orchestration_service import run_agent_workflow

router = APIRouter(prefix="/orchestration", tags=["orchestration"])


@router.post("/run", response_model=OrchestrationResponse)
async def run_orchestration(payload: OrchestrationRequest) -> OrchestrationResponse:
    if not payload.question or not payload.question.strip():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Question is required")

    dataset_profile = payload.dataset_profile or {
        "row_count": 0,
        "column_count": 0,
        "columns": [],
    }

    result = run_agent_workflow(payload.question, dataset_profile)
    return OrchestrationResponse(**result)
