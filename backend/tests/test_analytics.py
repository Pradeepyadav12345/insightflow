import pandas as pd

from app.services.analytics_service import build_sql_query, run_sql_agent


def test_build_sql_query_creates_grouped_aggregation() -> None:
    query = build_sql_query(
        pd.DataFrame({"segment": ["A", "A", "B"], "revenue": [100.0, 200.0, 50.0]}),
        "What is the average revenue by segment?",
    )

    assert "SELECT" in query.upper()
    assert "AVG(REVENUE)" in query.upper()
    assert "GROUP BY SEGMENT" in query.upper()


def test_run_sql_agent_returns_summary_and_rows() -> None:
    df = pd.DataFrame({"segment": ["A", "A", "B"], "revenue": [100.0, 200.0, 50.0]})

    result = run_sql_agent(df, "What is the average revenue by segment?")

    assert result["question"] == "What is the average revenue by segment?"
    assert result["sql"].upper().startswith("SELECT")
    assert result["result"]["rows"] >= 2
    assert isinstance(result["result"]["data"], list)
    assert result["result"]["data"]
    assert isinstance(result["insight"], str)
    assert len(result["insight"]) > 0
