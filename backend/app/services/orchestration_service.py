from __future__ import annotations

from typing import Any

try:
    from langgraph.graph import END, StateGraph
except ImportError:  # pragma: no cover - optional dependency
    StateGraph = None
    END = None


def build_workflow_plan(question: str, dataset_profile: dict[str, Any]) -> dict[str, Any]:
    if not question or not question.strip():
        raise ValueError("A question is required to build the workflow plan.")

    row_count = int(dataset_profile.get("row_count", 0) or 0)
    column_count = int(dataset_profile.get("column_count", 0) or 0)
    columns = dataset_profile.get("columns", [])
    numeric_columns = [column.get("name") for column in columns if column.get("type") == "numeric"]

    steps: list[dict[str, str]] = [
        {
            "name": "validate_dataset",
            "description": f"Validate dataset integrity for {row_count} rows and {column_count} columns.",
        },
        {
            "name": "resolve_metrics",
            "description": "Identify the best measure and grouping columns for the user question.",
        },
        {
            "name": "run_sql_analysis",
            "description": "Run the aggregation query needed for the analysis request.",
        },
        {
            "name": "summarize_insight",
            "description": "Turn the analytical result into a concise business insight.",
        },
    ]

    if numeric_columns:
        steps.insert(
            2,
            {
                "name": "check_numeric_measures",
                "description": f"Confirm the numeric fields available for analysis: {', '.join(numeric_columns)}.",
            },
        )

    return {
        "question": question,
        "dataset_summary": {
            "row_count": row_count,
            "column_count": column_count,
            "numeric_columns": numeric_columns,
        },
        "steps": steps,
    }


def build_langgraph_workflow() -> Any | None:
    if StateGraph is None or END is None:
        return None

    workflow = StateGraph(dict)
    workflow.add_node("validate_dataset", lambda state: {**state, "status": "validated"})
    workflow.add_node("run_sql_analysis", lambda state: {**state, "status": "analyzed"})
    workflow.add_node("summarize_insight", lambda state: {**state, "status": "completed"})
    workflow.set_entry_point("validate_dataset")
    workflow.add_edge("validate_dataset", "run_sql_analysis")
    workflow.add_edge("run_sql_analysis", "summarize_insight")
    workflow.add_edge("summarize_insight", END)
    return workflow.compile()


def run_agent_workflow(question: str, dataset_profile: dict[str, Any]) -> dict[str, Any]:
    plan = build_workflow_plan(question, dataset_profile)
    summary = (
        f"Prepared a workflow for '{question}' over {plan['dataset_summary']['row_count']} rows and "
        f"{plan['dataset_summary']['column_count']} columns. The analysis will validate the dataset, "
        "resolve the key measures, run the SQL aggregation, and summarize the result."
    )

    workflow = build_langgraph_workflow()
    if workflow is not None:
        initial_state = {"question": question, "dataset_profile": dataset_profile, "plan": plan}
        state = workflow.invoke(initial_state)
        status = state.get("status", "completed")
    else:
        status = "completed"

    return {
        "status": status,
        "result": {
            "question": question,
            "plan": plan,
            "summary": summary,
        },
    }
