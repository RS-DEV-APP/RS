from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ..db import SessionLocal
from ..models.right import Right
from ..schemas.right import RightCreate, RightRead

router = APIRouter(prefix="/rights", tags=["rights"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("", response_model=RightRead)
def create_right(payload: RightCreate, db: Session = Depends(get_db)):
    obj = Right(**payload.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.get("", response_model=List[RightRead])
def list_rights(db: Session = Depends(get_db)):
    return db.query(Right).all()
