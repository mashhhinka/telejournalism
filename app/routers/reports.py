from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas
from app.database import get_db

router = APIRouter(
    prefix="/reports",
    tags=["reports"]
)

# CREATE a report
@router.post("/", response_model=schemas.Report)
def create_report(report: schemas.ReportCreate, db: Session = Depends(get_db)):
    db_report = models.Report(**report.dict())
    db.add(db_report)
    db.commit()
    db.refresh(db_report)
    return db_report

# READ all reports with optional pagination
@router.get("/", response_model=List[schemas.Report])
def get_reports(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.Report).offset(skip).limit(limit).all()

# READ single report by ID
@router.get("/{report_id}", response_model=schemas.Report)
def get_report(report_id: int, db: Session = Depends(get_db)):
    db_report = db.query(models.Report).filter(models.Report.id == report_id).first()
    if not db_report:
        raise HTTPException(status_code=404, detail="Report not found")
    return db_report

# UPDATE a report
@router.put("/{report_id}", response_model=schemas.Report)
def update_report(report_id: int, updated_report: schemas.ReportCreate, db: Session = Depends(get_db)):
    db_report = db.query(models.Report).filter(models.Report.id == report_id).first()
    if not db_report:
        raise HTTPException(status_code=404, detail="Report not found")
    for key, value in updated_report.dict().items():
        setattr(db_report, key, value)
    db.commit()
    db.refresh(db_report)
    return db_report

# DELETE a report
@router.delete("/{report_id}")
def delete_report(report_id: int, db: Session = Depends(get_db)):
    db_report = db.query(models.Report).filter(models.Report.id == report_id).first()
    if not db_report:
        raise HTTPException(status_code=404, detail="Report not found")
    db.delete(db_report)
    db.commit()
    return {"detail": "Report deleted successfully"}
