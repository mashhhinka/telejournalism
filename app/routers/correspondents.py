from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models

router = APIRouter(
    prefix="/correspondents",
    tags=["Correspondents"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_correspondent(data: dict, db: Session = Depends(get_db)):
    obj = models.Correspondent(**data)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@router.get("/")
def get_all(db: Session = Depends(get_db)):
    return db.query(models.Correspondent).all()


@router.get("/{id}")
def get_one(id: int, db: Session = Depends(get_db)):
    return db.query(models.Correspondent).filter_by(id=id).first()


@router.delete("/{id}")
def delete_one(id: int, db: Session = Depends(get_db)):
    obj = db.query(models.Correspondent).get(id)
    db.delete(obj)
    db.commit()
    return {"status": "deleted"}
