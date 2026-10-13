from pydantic import BaseModel, Field


class DatasetUploadResponse(BaseModel):
    filename: str
    rows: int = Field(..., ge=0)
    columns: list[str]
    summary: dict


class DatasetProfileResponse(BaseModel):
    row_count: int
    column_count: int
    columns: list[dict]
    missing_values: dict
    data_quality_score: float
    profiled_at: str
