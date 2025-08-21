from fastapi import FastAPI
from .db import init_db
from .routers import titles, episodes, rights, schedule

app = FastAPI(title="Broadcast Rights & Scheduling API")

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(titles.router)
app.include_router(episodes.router)
app.include_router(rights.router)
app.include_router(schedule.router)

@app.get("/health")
def health():
    return {"status": "ok"}
