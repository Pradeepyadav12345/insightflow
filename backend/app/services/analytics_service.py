from __future__ import annotations

import re
from typing import Any

import pandas as pd


def _choose_metric_column(df: pd.DataFrame) -> str | None:
    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df[column]):
            return str(column)
    return None


def _choose_group_column(df: pd.DataFrame, question: str) -> str | None:
    lowered = question.lower()
    for column in df.columns:
        column_name = str(column).lower()
        if column_name in lowered and not pd.api.types.is_numeric_dtype(df[column]):
            return str(column)

    for column in df.columns:
        if not pd.api.types.is_numeric_dtype(df[column]):
            return str(column)
    return None


def _aggregate_name(metric_column: str, aggregation: str) -> str:
    return f"{aggregation.lower()}_{metric_column}"


def build_sql_query(df: pd.DataFrame, question: str) -> str:
    metric_column = _choose_metric_column(df)
    group_column = _choose_group_column(df, question)
    aggregation = "AVG"

    lowered = question.lower()
    if any(token in lowered for token in ["sum", "total", "aggregate"]):
        aggregation = "SUM"
    elif any(token in lowered for token in ["count", "number of", "how many"]):
        aggregation = "COUNT"
    elif "max" in lowered:
        aggregation = "MAX"
    elif "min" in lowered:
        aggregation = "MIN"

    if metric_column is None:
        raise ValueError("No numeric column available for aggregation.")

    if group_column and group_column != metric_column:
        alias = _aggregate_name(metric_column, aggregation.lower())
        return (
            f"SELECT {group_column}, {aggregation}({metric_column}) AS {alias} "
            f"FROM dataset GROUP BY {group_column} ORDER BY {alias} DESC;"
        )

    alias = _aggregate_name(metric_column, aggregation.lower())
    return f"SELECT {aggregation}({metric_column}) AS {alias} FROM dataset;"


def _build_grouped_result(df: pd.DataFrame, metric_column: str, group_column: str, aggregation: str) -> dict[str, Any]:
    if aggregation == "COUNT":
        aggregated = df.groupby(group_column, dropna=False)[metric_column].count().reset_index()
    elif aggregation == "SUM":
        aggregated = df.groupby(group_column, dropna=False)[metric_column].sum().reset_index()
    elif aggregation == "MAX":
        aggregated = df.groupby(group_column, dropna=False)[metric_column].max().reset_index()
    elif aggregation == "MIN":
        aggregated = df.groupby(group_column, dropna=False)[metric_column].min().reset_index()
    else:
        aggregated = df.groupby(group_column, dropna=False)[metric_column].mean().reset_index()

    alias = _aggregate_name(metric_column, aggregation.lower())
    aggregated = aggregated.rename(columns={metric_column: alias})
    return {"rows": aggregated.to_dict(orient="records")}


def _build_scalar_result(df: pd.DataFrame, metric_column: str, aggregation: str) -> dict[str, Any]:
    if aggregation == "COUNT":
        value = int(df[metric_column].count())
    elif aggregation == "SUM":
        value = float(df[metric_column].sum())
    elif aggregation == "MAX":
        value = float(df[metric_column].max())
    elif aggregation == "MIN":
        value = float(df[metric_column].min())
    else:
        value = float(df[metric_column].mean())

    alias = _aggregate_name(metric_column, aggregation.lower())
    return {"rows": [{alias: value}]}


def run_sql_agent(df: pd.DataFrame, question: str) -> dict[str, Any]:
    metric_column = _choose_metric_column(df)
    if metric_column is None:
        raise ValueError("No numeric measure available for SQL analysis.")

    group_column = _choose_group_column(df, question)
    lowered = question.lower()

    if any(token in lowered for token in ["sum", "total", "average", "avg", "mean", "max", "min", "count", "how many"]):
        if any(token in lowered for token in ["by", "group by", "per", "segment", "category"]):
            group_column = group_column if group_column and group_column != metric_column else None
        else:
            group_column = None

    aggregation = "AVG"
    if any(token in lowered for token in ["sum", "total", "aggregate"]):
        aggregation = "SUM"
    elif any(token in lowered for token in ["count", "how many", "number of"]):
        aggregation = "COUNT"
    elif "max" in lowered:
        aggregation = "MAX"
    elif "min" in lowered:
        aggregation = "MIN"

    if group_column and group_column != metric_column:
        result = _build_grouped_result(df, metric_column, group_column, aggregation)
        rows = result["rows"]
        top_row = rows[0] if rows else {}
        aggregate_key = next(iter(top_row.keys())) if top_row else "value"
        top_value = top_row.get(aggregate_key, 0)
        insight = (
            f"The {aggregation.lower()} of {metric_column} is {top_value} for the leading segment. "
            f"The dataset contains {len(rows)} grouped segments."
        )
    else:
        result = _build_scalar_result(df, metric_column, aggregation)
        rows = result["rows"]
        aggregate_key = next(iter(rows[0].keys())) if rows else "value"
        scalar_value = rows[0].get(aggregate_key, 0) if rows else 0
        insight = f"The {aggregation.lower()} of {metric_column} is {scalar_value} across the dataset."

    sql = build_sql_query(df, question)
    return {
        "question": question,
        "sql": sql,
        "result": {
            "rows": len(rows),
            "data": rows,
            "summary": {"metric_column": metric_column, "aggregation": aggregation},
        },
        "insight": insight,
    }
