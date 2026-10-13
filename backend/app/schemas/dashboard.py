from pydantic import BaseModel, Field


class DashboardRequest(BaseModel):
    title: str = Field(..., min_length=1)
    metrics: list[dict] = []
    charts: list[dict] = []


class ReportRequest(BaseModel):
    title: str = Field(..., min_length=1)
    metrics: list[dict] = []


class DashboardResponse(BaseModel):
    title: str
    metrics: list[dict]
    charts: list[dict]
    summary: str


class ReportResponse(BaseModel):
    title: str
    metrics: list[dict]
    summary: str
