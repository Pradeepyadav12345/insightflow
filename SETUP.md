# Setup Guide

## Windows PowerShell

```powershell
Copy-Item .env.example .env
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r backend\requirements.txt
cd backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Docker

```powershell
docker compose up --build
```

## Frontend

```powershell
cd frontend
npm install
npm run dev -- --host 0.0.0.0
```

## Mobile

```powershell
cd mobile
npm install
npx expo start
```
