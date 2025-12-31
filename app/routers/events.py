from fastapi import APIRouter, HTTPException, Query, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List
from app.database import get_db
from app.models import Event, Report
from app import schemas

router = APIRouter(
    prefix="/events",
    tags=["events"]
)

# 1. Search route first
@router.get("/search", response_model=List[schemas.Event])
def search_events(query: str = Query(...), skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    results = db.query(Event).filter(
        (Event.title.ilike(f"%{query}%")) | (Event.description.ilike(f"%{query}%"))
    ).offset(skip).limit(limit).all()
    return results

# 2. List all events with pagination
@router.get("/", response_model=List[schemas.Event])
def list_events(skip: int = Query(0, ge=0), limit: int = Query(10, ge=1), db: Session = Depends(get_db)):
    events = db.query(Event).offset(skip).limit(limit).all()
    return events

# 3. Get event by ID
@router.get("/{event_id}", response_model=schemas.Event)
def get_event(event_id: int, db: Session = Depends(get_db)):
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

# 4. Create event
@router.post("/", response_model=schemas.Event)
def create_event(event: schemas.EventCreate, db: Session = Depends(get_db)):
    db_event = Event(**event.dict())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

# 5. Update event
@router.put("/{event_id}", response_model=schemas.Event)
def update_event(event_id: int, event: schemas.EventCreate, db: Session = Depends(get_db)):
    db_event = db.query(Event).filter(Event.id == event_id).first()
    if not db_event:
        raise HTTPException(status_code=404, detail="Event not found")
    db_event.title = event.title
    db_event.location = event.location
    db_event.description = event.description
    db.commit()
    db.refresh(db_event)
    return db_event

# 6. Delete event
@router.delete("/{event_id}")
def delete_event(event_id: int, db: Session = Depends(get_db)):
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    db.delete(event)
    db.commit()
    return {"detail": "Event deleted"}

# 7. Group by location
@router.get("/groupby-location/")
def group_by_location(db: Session = Depends(get_db)):
    result = db.query(Event.location, func.count(Event.id)).group_by(Event.location).all()
    return [{"location": loc, "count": count} for loc, count in result]

# 8. Sorted events
@router.get("/sorted/")
def sorted_events(order: str = "asc", db: Session = Depends(get_db)):
    query = db.query(Event)
    if order == "asc":
        query = query.order_by(Event.date.asc())
    else:
        query = query.order_by(Event.date.desc())
    return query.all()
