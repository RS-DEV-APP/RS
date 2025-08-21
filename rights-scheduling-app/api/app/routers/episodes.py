from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ..db import SessionLocal
from ..models.episode import Episode
from ..schemas.episode import EpisodeCreate, EpisodeRead

router = APIRouter(prefix="/episodes", tags=["episodes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("", response_model=EpisodeRead)
def create_episode(payload: EpisodeCreate, db: Session = Depends(get_db)):
    obj = Episode(**payload.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.get("", response_model=List[EpisodeRead])
def list_episodes(db: Session = Depends(get_db)):
    return db.query(Episode).all()
