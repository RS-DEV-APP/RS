from pydantic import BaseModel
from typing import Optional, List

class ScheduleItemCreate(BaseModel):
    channel_id: int
    start: str
    end: str
    content_ref: str
    version: Optional[str] = None
    status: str = "PLANNED"

class ScheduleItemRead(ScheduleItemCreate):
    id: int
    class Config:
        from_attributes = True

class ValidateResult(BaseModel):
    ok: bool
    issues: List[str]
