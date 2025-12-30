from fastapi import FastAPI
from app.routers import correspondents, events

app = FastAPI()

app.include_router(correspondents.router, prefix="/correspondents", tags=["Correspondents"])
app.include_router(events.router, prefix="/events", tags=["Events"])
