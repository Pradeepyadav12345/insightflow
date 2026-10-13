from __future__ import annotations

from typing import Any


def build_dashboard(payload: dict[str, Any]) -> dict[str, Any]:
    title = payload.get("title", "Dashboard")
    metrics = payload.get("metrics", [])
    charts = payload.get("charts", [])

    return {
        "title": title,
        "metrics": metrics,
        "charts": charts,
        "summary": f"Dashboard '{title}' contains {len(metrics)} metrics and {len(charts)} charts.",
    }


def build_report(title: str, metrics: list[dict[str, Any]]) -> dict[str, Any]:
    if not title:
        raise ValueError("A report title is required.")

    summary_lines = [
        f"{metric.get('label', 'Metric')}: {metric.get('value', 0)} ({metric.get('trend', 'n/a')})"
        for metric in metrics
    ]

    return {
        "title": title,
        "metrics": metrics,
        "summary": " | ".join(summary_lines) if summary_lines else "No metrics available for this report.",
    }
