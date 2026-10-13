from pydantic import BaseModel, Field


class IntegrationRequest(BaseModel):
    name: str = Field(..., min_length=1)
    connector_type: str = Field(..., min_length=1)
    enabled: bool = True
    status: str = "connected"
    metadata: dict | None = None


class IntegrationResponse(BaseModel):
    name: str
    connector_type: str
    enabled: bool
    status: str
    metadata: dict
    ready: bool


class ScheduleRequest(BaseModel):
    name: str = Field(..., min_length=1)
    cron_expression: str = Field(..., min_length=1)
    job_type: str = Field(..., min_length=1)
    organization_id: str = Field(..., min_length=1)
    status: str = "active"


class ScheduleResponse(BaseModel):
    name: str
    cron_expression: str
    job_type: str
    organization_id: str
    status: str
    next_run: str
