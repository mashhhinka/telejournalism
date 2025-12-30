from sqlalchemy.orm import Session
from . import models, schemas

def create_correspondent(db: Session, correspondent: schemas.CorrespondentCreate):
    db_cor = models.Correspondent(**correspondent.dict())
    db.add(db_cor)
    db.commit()
    db.refresh(db_cor)
    return db_cor

def get_correspondents(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Correspondent).offset(skip).limit(limit).all()
