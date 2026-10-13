# API Guide

## Base URL

- Local: http://localhost:8000
- API prefix: /api/v1

## Core routes

### Health

- GET /api/v1/health
- Returns backend service health and readiness metadata.

### Auth

- POST /api/v1/auth/register
  - Body: { email, password, full_name, organization_name? }
- POST /api/v1/auth/login
  - Body: { email, password }
- GET /api/v1/auth/me
  - Requires bearer token

### Datasets

- POST /api/v1/datasets/upload
  - Multipart form-data with a file upload
- POST /api/v1/datasets/profile
  - Multipart form-data with a file upload

### Analytics

- POST /api/v1/analytics/query
  - Body: { question }

### Orchestration

- POST /api/v1/orchestration/run
  - Body: { question, dataset_profile? }

### Dashboards

- POST /api/v1/dashboards/
  - Body: { title, metrics, charts }
- POST /api/v1/dashboards/report
  - Body: { title, metrics }

### Integrations

- POST /api/v1/integrations/register
  - Body: { name, connector_type, enabled, status, metadata }

### Schedules

- POST /api/v1/schedules
  - Body: { name, cron_expression, job_type, organization_id, status }

### Monitoring

- GET /api/v1/monitoring/health

## Example requests

### Register a user

```bash
curl -X POST http://localhost:8000/api/v1/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "admin@example.com",
    "password": "StrongP@ssw0rd!",
    "full_name": "Platform Admin",
    "organization_name": "Default Org"
  }'
```

### Upload a dataset

```bash
curl -X POST http://localhost:8000/api/v1/datasets/upload \
  -F "file=@sample.csv"
```

### Ask an analysis question

```bash
curl -X POST http://localhost:8000/api/v1/analytics/query \
  -H "Content-Type: application/json" \
  -d '{
    "question": "What is the average revenue by segment?"
  }'
```

## Authentication

Most protected routes expect a bearer token in the Authorization header:

```http
Authorization: Bearer <token>
```

## Notes

- Local development is intended to run through the FastAPI backend on port 8000.
- The platform exposes a structured v1 API layer for auth, data, analysis, orchestration, dashboarding, integrations, scheduling, and monitoring.
- More endpoints and production-grade security controls can be added as the platform expands.
