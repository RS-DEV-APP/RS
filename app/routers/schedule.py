from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ..db import SessionLocal
from ..models.schedule import ScheduleItem
from ..models.right import Right
from ..schemas.schedule import ScheduleItemCreate, ScheduleItemRead, ValidateResult
from ..services.availability import validate_against_rights

router = APIRouter(prefix="/schedule", tags=["schedule"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("", response_model=ScheduleItemRead)
def create_item(payload: ScheduleItemCreate, db: Session = Depends(get_db)):
    obj = ScheduleItem(**payload.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.get("", response_model=List[ScheduleItemRead])
def list_items(db: Session = Depends(get_db)):
    return db.query(ScheduleItem).all()

@router.post("/validate", response_model=ValidateResult)
def validate_items(items: List[ScheduleItemCreate], db: Session = Depends(get_db)):
    issues: List[str] = []
    # naive: check each against first matching right by title_id from content_ref like "episode:123" or "title:5"
    rights = db.query(Right).all()
    for item in items:
        # parse content_ref expecting "title:<id>" or "episode:<id>"
        parts = item.content_ref.split(":")
        title_id = None
        if parts[0] == "title":
            title_id = int(parts[1])
        # minimal: pick first right that matches title_id
        r = next((r for r in rights if title_id and r.title_id == title_id), None)
        if r:
            issues.extend(validate_against_rights(item.start, item.end, r))
        else:
            issues.append(f"No rights found for {item.content_ref}")
    return ValidateResult(ok=len(issues)==0, issues=issues)
