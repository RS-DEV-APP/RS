# Broadcast Rights & Scheduling — Monorepo

A production-ready starter for a **Broadcast Rights & Scheduling** system.

- **Backend**: FastAPI (Python), SQLAlchemy, Pydantic, Celery, Redis
- **Frontend**: React + TypeScript + Vite, TailwindCSS
- **DB**: PostgreSQL (Docker)
- **Packaging**: Docker Compose, Makefile
- **Tests**: pytest, Playwright scaffold (frontend)

## Quick Start

```bash
# 1) Copy .env.example -> .env and adjust
cp .env.example .env

# 2) Start everything
make up

# 3) Seed demo data (in another terminal)
make seed

# 4) Open web app
# http://localhost:5173

# 5) API docs
# http://localhost:8000/docs
```

### Demo Script
Build a day schedule for **Channel One** on **2025-09-01** (Europe/Berlin):
```bash
make demo
```

## Project Structure

```
rights-scheduling-app/
├─ api/                 # FastAPI backend
│  ├─ app/
│  │  ├─ main.py
│  │  ├─ db.py
│  │  ├─ config.py
│  │  ├─ models/...
│  │  ├─ schemas/...
│  │  ├─ services/...
│  │  └─ routers/...
│  ├─ tests/...
│  ├─ pyproject.toml
│  └─ celery_app.py
├─ web/                 # React + Vite + TS frontend
│  ├─ index.html
│  ├─ package.json
│  ├─ tsconfig.json
│  ├─ vite.config.ts
│  └─ src/...
├─ db/                  # Migrations placeholder
├─ .env.example
├─ docker-compose.yml
├─ Makefile
└─ .gitignore
```

## Environment

Edit `.env` before `make up`:

```
POSTGRES_USER=app
POSTGRES_PASSWORD=app
POSTGRES_DB=bms
POSTGRES_PORT=5432
API_PORT=8000
WEB_PORT=5173
REDIS_PORT=6379
JWT_SECRET=change-me
```

## Common Make targets

```bash
make up         # start docker services
make down       # stop
make logs       # tail logs
make seed       # seed demo data
make demo       # run the 2025-09-01 demo schedule
make test       # run backend tests
```

## Pushing to GitHub

1. Create an empty repository on GitHub (without README).
2. Run in the project root:

```bash
git init
git add .
git commit -m "Initial commit: Broadcast Rights & Scheduling starter"
git branch -M main
git remote add origin https://github.com/<your-user>/<your-repo>.git
git push -u origin main
```

---

**Have fun!** This is a foundation—extend the availability engine, conflict checks, and UI per your needs.
