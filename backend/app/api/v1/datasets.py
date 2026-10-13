from __future__ import annotations

from fastapi import APIRouter, File, HTTPException, UploadFile, status

from app.schemas.dataset import DatasetProfileResponse, DatasetUploadResponse
from app.services.dataset_service import load_dataset_file, profile_dataframe

router = APIRouter(prefix="/datasets", tags=["datasets"])


@router.post("/upload", response_model=DatasetUploadResponse)
async def upload_dataset(file: UploadFile = File(...)) -> DatasetUploadResponse:
    if not file.filename:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="A file is required")

    raw_bytes = await file.read()
    try:
        df, metadata = load_dataset_file(file.filename, raw_bytes)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc

    summary = profile_dataframe(df)
    return DatasetUploadResponse(
        filename=metadata["filename"],
        rows=metadata["rows"],
        columns=metadata["columns"],
        summary=summary,
    )


@router.post("/profile", response_model=DatasetProfileResponse)
async def profile_dataset(file: UploadFile = File(...)) -> DatasetProfileResponse:
    if not file.filename:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="A file is required")

    raw_bytes = await file.read()
    try:
        df, _ = load_dataset_file(file.filename, raw_bytes)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc

    summary = profile_dataframe(df)
    return DatasetProfileResponse(**summary)
