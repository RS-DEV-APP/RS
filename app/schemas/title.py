from pydantic import BaseModel
from typing import Optional

class TitleCreate(BaseModel):
    type: str
    name: str
    original_title: Optional[str] = None
    production_year: Optional[int] = None
    vendor: Optional[str] = None

class TitleRead(TitleCreate):
    id: int
    class Config:
        from_attributes = True
