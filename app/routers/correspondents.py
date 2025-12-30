from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter(prefix="/correspondents", tags=["Correspondents"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Correspondent)
def create_correspondent_endpoint(correspondent: schemas.CorrespondentCreate, db: Session = Depends(get_db)):
    return crud.create_correspondent(db, correspondent)

@router.get("/", response_model=list[schemas.Correspondent])
def read_correspondents(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_correspondents(db, skip=skip, limit=limit)
