# Troubleshooting

## Backend not starting

- confirm `.env` is present
- ensure PostgreSQL and Redis are running
- verify Python dependencies were installed

## Port conflicts

- change ports in `.env` or `docker-compose.yml`
- ensure no prior service is using 8000, 5432, or 6379

## Dependency issues

- recreate the virtual environment
- install requirements again
