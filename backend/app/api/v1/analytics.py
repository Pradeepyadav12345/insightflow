from __future__ import annotations

import pandas as pd
from fastapi import APIRouter, HTTPException, status

from app.schemas.analytics import AnalyticsQueryRequest, AnalyticsQueryResponse
from app.services.analytics_service import run_sql_agent

router = APIRouter(prefix="/analytics", tags=["analytics"])


@router.post("/query", response_model=AnalyticsQueryResponse)
async def run_analytics_query(payload: AnalyticsQueryRequest) -> AnalyticsQueryResponse:
    sample_frame = pd.DataFrame(
        {
            "segment": ["A", "A", "B", "B"],
            "revenue": [100.0, 200.0, 60.0, 80.0],
            "orders": [10, 12, 5, 8],
        }
    )

    try:
        result = run_sql_agent(sample_frame, payload.question)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc

    return AnalyticsQueryResponse(**result)
