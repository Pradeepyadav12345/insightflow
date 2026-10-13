# Deployment Guide

## Docker Compose

```powershell
docker compose up --build
```

## Cloud targets

- AWS: ECS, RDS, S3, ElastiCache, Secrets Manager, CloudWatch
- Azure: Container Apps, PostgreSQL, Blob Storage, Redis, Key Vault, Azure Monitor

## CI/CD

GitHub Actions should run lint, tests, security scans, build, and deploy stages.
