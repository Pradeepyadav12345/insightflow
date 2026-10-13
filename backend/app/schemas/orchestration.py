from pydantic import BaseModel, Field


class OrchestrationRequest(BaseModel):
    question: str = Field(..., min_length=3)
    dataset_profile: dict | None = None


class OrchestrationResponse(BaseModel):
    status: str
    result: dict
