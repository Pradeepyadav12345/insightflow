from __future__ import annotations

from datetime import datetime, timezone
from io import BytesIO
from typing import Any

import pandas as pd


def infer_column_type(series: pd.Series) -> str:
    non_null = series.dropna()
    if non_null.empty:
        return "unknown"

    if pd.api.types.is_bool_dtype(non_null):
        return "boolean"
    if pd.api.types.is_datetime64_any_dtype(non_null):
        return "datetime"
    if pd.api.types.is_numeric_dtype(non_null):
        return "numeric"
    return "string"


def profile_dataframe(df: pd.DataFrame) -> dict[str, Any]:
    if df.empty and len(df.columns) == 0:
        return {
            "row_count": 0,
            "column_count": 0,
            "columns": [],
            "missing_values": {},
            "data_quality_score": 1.0,
            "profiled_at": datetime.now(timezone.utc).isoformat(),
        }

    columns: list[dict[str, Any]] = []
    for column_name in df.columns:
        series = df[column_name]
        missing_values = int(series.isna().sum())
        columns.append(
            {
                "name": str(column_name),
                "type": infer_column_type(series),
                "missing_values": missing_values,
                "null_ratio": round(float(missing_values / len(df)), 4) if len(df) else 0.0,
                "unique_count": int(series.nunique(dropna=True)),
            }
        )

    total_missing = int(df.isna().sum().sum())
    total_cells = max(len(df) * len(df.columns), 1)
    quality_score = max(0.0, min(1.0, 1.0 - (total_missing / total_cells)))

    return {
        "row_count": int(len(df)),
        "column_count": int(len(df.columns)),
        "columns": columns,
        "missing_values": {str(column): int(df[column].isna().sum()) for column in df.columns},
        "data_quality_score": round(quality_score, 4),
        "profiled_at": datetime.now(timezone.utc).isoformat(),
    }


def load_dataset_file(filename: str, file_bytes: bytes) -> tuple[pd.DataFrame, dict[str, Any]]:
    lower_name = filename.lower()

    try:
        if lower_name.endswith(".csv"):
            df = pd.read_csv(BytesIO(file_bytes))
        elif lower_name.endswith((".xlsx", ".xls")):
            df = pd.read_excel(BytesIO(file_bytes))
        elif lower_name.endswith(".json"):
            raw = file_bytes.decode("utf-8")
            payload = pd.read_json(BytesIO(raw.encode("utf-8")))
            df = pd.DataFrame(payload)
        else:
            raise ValueError("Unsupported file type. Please upload CSV, Excel, or JSON.")
    except Exception as exc:  # pragma: no cover - explicit file validation layer.
        raise ValueError(f"Unable to parse dataset: {exc}") from exc

    metadata = {
        "filename": filename,
        "rows": int(len(df)),
        "columns": list(df.columns),
        "source_type": "uploaded_file",
    }
    return df, metadata
