from fastapi import FastAPI
from app.routers import correspondents, events, reports

app = FastAPI()

app.include_router(correspondents.router, prefix="/correspondents", tags=["Correspondents"])
app.include_router(events.router, prefix="/events", tags=["Events"])
app.include_router(reports.router, prefix="/reports", tags=["Reports"])
app.include_router(events.router)