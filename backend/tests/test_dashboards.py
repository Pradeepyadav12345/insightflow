from app.services.dashboard_service import build_dashboard, build_report


def test_build_dashboard_creates_summary_blocks() -> None:
    dashboard = build_dashboard(
        {
            "title": "Revenue overview",
            "metrics": [{"label": "Revenue", "value": 125000, "trend": "+8.1%"}],
            "charts": [{"title": "Revenue by segment", "type": "bar"}],
        }
    )

    assert dashboard["title"] == "Revenue overview"
    assert len(dashboard["metrics"]) == 1
    assert dashboard["metrics"][0]["label"] == "Revenue"
    assert len(dashboard["charts"]) == 1


def test_build_report_generates_summary_text() -> None:
    report = build_report(
        "Quarterly performance report",
        [
            {"label": "Revenue", "value": 125000, "trend": "+8.1%"},
            {"label": "Orders", "value": 4200, "trend": "+5.4%"},
        ],
    )

    assert report["title"] == "Quarterly performance report"
    assert "Revenue" in report["summary"]
    assert "Orders" in report["summary"]
    assert "125000" in report["summary"]
