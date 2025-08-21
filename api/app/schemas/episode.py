from pydantic import BaseModel

class EpisodeCreate(BaseModel):
    title_id: int
    season_number: int
    episode_number: int
    duration: int

class EpisodeRead(EpisodeCreate):
    id: int
    class Config:
        from_attributes = True
