from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db  # your DB session dependency
from app import models, schemas
from fastapi import Depends
from fastapi import Query
from sqlalchemy import func
from sqlalchemy import text

router = APIRouter(
    prefix="/events",
    tags=["events"]
)



@router.post("/", response_model=schemas.Event)
def create_event(event: schemas.EventCreate, db: Session = Depends(get_db)):
    db_event = models.Event(**event.dict())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event



@router.get("/", response_model=list[schemas.Event])
def list_events(db: Session = Depends(get_db)):
    return db.query(models.Event).all()


@router.get("/events/")
def get_events(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.Event).offset(skip).limit(limit).all()


@router.get("/{event_id}", response_model=schemas.Event)
def get_event(event_id: int, db: Session = Depends(get_db)):
    event = db.query(models.Event).filter(models.Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@router.put("/{event_id}", response_model=schemas.Event)
def update_event(event_id: int, event: schemas.EventCreate, db: Session = Depends(get_db)):
    # Find the event in the database
    db_event = db.query(models.Event).filter(models.Event.id == event_id).first()
    if not db_event:
        raise HTTPException(status_code=404, detail="Event not found")
    
    db_event.title = event.title
    db_event.location = event.location
    db_event.description = event.description
    db.commit()           
    db.refresh(db_event)  
    return db_event


@router.delete("/{event_id}")
def delete_event(event_id: int, db: Session = Depends(get_db)):
    event = db.query(models.Event).filter(models.Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    
    db.delete(event)
    db.commit()
    return {"detail": "Event deleted"}

@router.get("/", response_model=list[schemas.Event])
def read_events(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    events = db.query(models.Event).offset(skip).limit(limit).all()
    return events

@router.get("/events/filter/")
def filter_events(title: str = None, location: str = None, db: Session = Depends(get_db)):
    query = db.query(models.Event)
    if title:
        query = query.filter(models.Event.title.ilike(f"%{title}%"))
    if location:
        query = query.filter(models.Event.location.ilike(f"%{location}%"))
    return query.all()


@router.put("/update-location/")
def update_events(db: Session = Depends(get_db)):
    events_to_update = db.query(models.Event).filter(models.Event.location == "Yerevan").all()
    for event in events_to_update:
        event.description = "Updated Description"
    db.commit()
    return {"updated": len(events_to_update)}



@router.get("/groupby-location/")
def group_by_location(db: Session = Depends(get_db)):
    result = db.query(models.Event.location, func.count(models.Event.id)).group_by(models.Event.location).all()
    return [{"location": loc, "count": count} for loc, count in result]


@router.get("/events/sorted/")
def sorted_events(order: str = "asc", db: Session = Depends(get_db)):
    query = db.query(models.Event)
    if order == "asc":
        query = query.order_by(models.Event.date.asc())
    else:
        query = query.order_by(models.Event.date.desc())
    return query.all()
u8999i8

@router.get("/events/search/")
def search_events(query: str = Query(...), db: Session = Depends(get_db)):
    results = db.execute(
        text("SELECT * FROM events WHERE data::text ILIKE :q"),
        {"q": f"%{query}%"}
    ).fetchall()
    return results

@router.get("/events/")
def list_events(skip: int = Query(0, ge=0), limit: int = Query(10, ge=1), db: Session = Depends(get_db)):
    """
    List events with pagination.
    skip: number of records to skip
    limit: number of records to return
    """
    events = db.query(models.Event).offset(skip).limit(limit).all()
    return events


@router.get("/events/with-reports/")
def events_with_reports(db: Session = Depends(get_db)):
    events = db.query(models.Event).join(models.Report).all()
    return events

@router.put("/events/update-location/")
def update_location(old_location: str, new_location: str, db: Session = Depends(get_db)):
    updated = db.query(models.Event).filter(models.Event.location == old_location).update({"location": new_location})
    db.commit()
    return {"updated": updated}


@router.get("/events/count-by-location/")
def count_by_location(db: Session = Depends(get_db)):
    from sqlalchemy import func
    result = db.query(models.Event.location, func.count(models.Event.id)).group_by(models.Event.location).all()
    return result
