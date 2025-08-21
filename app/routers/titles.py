from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import SessionLocal
from ..models.title import Title
from ..schemas.title import TitleCreate, TitleRead
from typing import List

router = APIRouter(prefix="/titles", tags=["titles"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("", response_model=TitleRead)
def create_title(payload: TitleCreate, db: Session = Depends(get_db)):
    obj = Title(**payload.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.get("", response_model=List[TitleRead])
def list_titles(db: Session = Depends(get_db)):
    return db.query(Title).all()
