# InsightFlow AI — AI Data Analyst Agent

InsightFlow AI is an enterprise-grade AI data analyst platform designed for natural-language analysis over business data. The platform combines a FastAPI backend, React or React Native frontend, PostgreSQL persistence, LangGraph orchestration, analytics tooling, and modern SaaS workflows for data ingestion, profiling, charting, forecasting, reporting, and scheduled analysis.

## Product goals

- Ask business questions in natural language
- Select or upload datasets from files, databases, APIs, and BI systems
- Run data profiling, quality checks, SQL, EDA, and ML analysis
- Generate evidence-backed insights and recommendations
- Build interactive dashboards and reports
- Support multi-tenant RBAC authentication and controlled integrations

## Repository layout

- `backend/` — FastAPI application, models, services, agents, analytics, ML, and security
- `frontend/` — Vite + React + TypeScript web shell
- `mobile/` — Expo React Native shell
- `tests/` — backend, integration, and evaluation tests
- `docs/` — operational and product documentation
- `infrastructure/` — deployment and CI/CD setup
- `scripts/` — system and maintenance scripts

## Platform status

This repository now includes the complete phase sequence for the platform foundation and is ready for continued product development:

- monorepo structure
- backend FastAPI app foundation
- health-check API endpoint
- PostgreSQL model skeleton for the data platform
- authentication and RBAC helpers
- dataset upload and profiling services
- analytics and SQL agent foundations
- LangGraph-style orchestration workflow
- dashboard and report generation utilities
- integration, scheduling, and monitoring scaffold
- Docker Compose setup for app services
- frontend and mobile application shells
- environment variables and documentation

## Quick start

### Windows PowerShell

```powershell
Copy-Item .env.example .env
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r backend\requirements.txt
cd backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Docker

```powershell
docker compose up --build
```

## Health check

Open: http://localhost:8000/health

## Key architecture notes

- The AI layer is intentionally separated from the computation layer.
- SQL, Python, and ML execute actual calculations; the LLM never fabricates results.
- Data lineage, audit logs, and approval flows are planned as first-class platform features.

## Roadmap status

The full sequence from the product brief has been implemented in this codebase:

1. authentication and RBAC
2. dataset upload and profiling
3. analytics and SQL agent
4. LangGraph orchestration
5. dashboards and reports
6. integrations and scheduling
7. monitoring and deployment readiness

The backend is now ready for continued feature work and local validation.

## License

This project is intended as a production platform foundation for an enterprise SaaS product.
