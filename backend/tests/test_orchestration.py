from app.services.orchestration_service import build_workflow_plan, run_agent_workflow


def test_build_workflow_plan_creates_steps_for_dataset_question() -> None:
    plan = build_workflow_plan(
        "What is the average revenue by segment?",
        {"row_count": 500, "column_count": 4, "columns": [{"name": "segment", "type": "string"}, {"name": "revenue", "type": "numeric"}]},
    )

    assert plan["question"] == "What is the average revenue by segment?"
    assert len(plan["steps"]) >= 3
    assert any(step["name"] == "validate_dataset" for step in plan["steps"])
    assert any(step["name"] == "run_sql_analysis" for step in plan["steps"])


def test_run_agent_workflow_returns_status_and_summary() -> None:
    execution = run_agent_workflow(
        "What is the average revenue by segment?",
        {"row_count": 500, "column_count": 4, "columns": [{"name": "segment", "type": "string"}, {"name": "revenue", "type": "numeric"}]},
    )

    assert execution["status"] == "completed"
    assert execution["result"]["question"] == "What is the average revenue by segment?"
    assert execution["result"]["plan"]["steps"]
    assert isinstance(execution["result"]["summary"], str)
