from pydantic import BaseModel
from typing import Optional

class RightCreate(BaseModel):
    contract_id: int
    title_id: int
    right_type: str
    territories: str
    languages: str
    platforms: str
    start: str
    end: str
    exclusivity: Optional[str] = None
    blackout_dates: Optional[str] = None
    plays_cap: Optional[int] = None

class RightRead(RightCreate):
    id: int
    class Config:
        from_attributes = True
