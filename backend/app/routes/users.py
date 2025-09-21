from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, models, schemas
from ..database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@router.get("/")
def list_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db, user_id)
