from pydantic import BaseModel, Field


class AnalyticsQueryRequest(BaseModel):
    question: str = Field(..., min_length=3)


class AnalyticsQueryResponse(BaseModel):
    question: str
    sql: str
    result: dict
    insight: str
