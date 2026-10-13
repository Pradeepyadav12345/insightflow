# Database Guide

## Stack

- PostgreSQL 16
- SQLAlchemy ORM
- Alembic migration support

## Core entities

The schema includes organizations, roles, users, datasets, sources, analyses, charts, dashboards, scheduled jobs, notifications, integrations, API keys, and audit logs.

## Local setup

```powershell
docker compose up postgres -d
```

Then connect using the value in `.env`.
