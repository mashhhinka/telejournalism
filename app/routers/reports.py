from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import models, schemas

router = APIRouter()


@router.post("/", response_model=schemas.Report)
def create_report(report: schemas.ReportCreate, db: Session = Depends(get_db)):
    # check FK existence
    if not db.get(models.Correspondent, report.correspondent_id):
        raise HTTPException(status_code=404, detail="Correspondent not found")

    if not db.get(models.Event, report.event_id):
        raise HTTPException(status_code=404, detail="Event not found")

    db_report = models.Report(**report.dict())
    db.add(db_report)
    db.commit()
    db.refresh(db_report)
    return db_report


@router.get("/", response_model=list[schemas.Report])
def list_reports(db: Session = Depends(get_db)):
    return db.query(models.Report).all()

@router.get("/reports/", response_model=list[schemas.Report])
def get_reports_with_event(db: Session = Depends(get_db)):
    return db.query(models.Report).join(models.Event).all()
