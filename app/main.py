from fastapi import FastAPI
from app.database import init_db
from app.routers import items, reports

app = FastAPI(title="TicketOps API", version="0.1.0")

app.include_router(items.router, prefix="/items", tags=["items"])
app.include_router(reports.router, prefix="/reports", tags=["reports"])


@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/health")
def health():
    return {"status": "ok"}
