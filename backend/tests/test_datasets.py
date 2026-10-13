import pandas as pd

from app.services.dataset_service import profile_dataframe


def test_profile_dataframe_computes_summary_metrics() -> None:
    df = pd.DataFrame(
        {
            "customer_id": [1, 2, 3],
            "segment": ["A", "B", "A"],
            "revenue": [120.0, 85.5, 200.0],
            "notes": ["ok", None, "great"],
        }
    )

    summary = profile_dataframe(df)

    assert summary["row_count"] == 3
    assert summary["column_count"] == 4
    assert summary["missing_values"]["notes"] == 1
    assert summary["data_quality_score"] > 0
    assert summary["columns"][0]["name"] == "customer_id"


def test_profile_dataframe_detects_numeric_columns() -> None:
    df = pd.DataFrame({"amount": [10, 20, 30], "city": ["NY", "LA", "SF"]})

    summary = profile_dataframe(df)

    numeric_columns = [column["name"] for column in summary["columns"] if column["type"] == "numeric"]
    assert "amount" in numeric_columns
    assert "city" in {column["name"] for column in summary["columns"]}
