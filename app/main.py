from fastapi import FastAPI
from app.routers import correspondents

app = FastAPI(title="Telejournalism API")

app.include_router(correspondents.router)
app.include_router(events.router)
app.include_router(reports.router)


@app.get("/")
def root():
    return {"message": "Telejournalism API is running"}
