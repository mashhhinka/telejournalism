from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import get_db

router = APIRouter()


@router.post("/", response_model=schemas.Correspondent)
def create_correspondent(
    correspondent: schemas.CorrespondentCreate,
    db: Session = Depends(get_db)
):
    db_obj = models.Correspondent(**correspondent.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


@router.get("/", response_model=list[schemas.Correspondent])
def list_correspondents(db: Session = Depends(get_db)):
    return db.query(models.Correspondent).all()
