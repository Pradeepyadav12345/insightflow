# Architecture

## Overview

InsightFlow AI is organized as a monorepo with a FastAPI backend, React web shell, and Expo mobile shell. The platform separates AI orchestration, data execution, security, and business logic to keep the architecture modular and production-friendly.

## Core principles

- AI decides the plan, not the numbers
- computation happens in SQL/Python/ML layers
- validation occurs before presenting results
- each analysis is auditable and traceable
- multi-tenancy and RBAC are enforced by design

## Layers

1. Client apps
2. API gateway and auth services
3. LangGraph orchestration and agent workflows
4. Data connectors and execution engines
5. Persistence and lineage storage
6. Monitoring and background workers

## Phase 1 foundation

The current version establishes the repo structure, backend API, database schema skeleton, Docker environment, and shell applications.
