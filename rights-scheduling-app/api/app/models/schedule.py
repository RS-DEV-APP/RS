from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String
from ..db import Base

class ScheduleItem(Base):
    __tablename__ = "schedule_items"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    channel_id: Mapped[int] = mapped_column(Integer, index=True)
    start: Mapped[str] = mapped_column(String(20))  # ISO datetime
    end: Mapped[str] = mapped_column(String(20))
    content_ref: Mapped[str] = mapped_column(String(64))  # e.g., episode:123
    version: Mapped[str | None] = mapped_column(String(64), nullable=True)
    status: Mapped[str] = mapped_column(String(16), default="PLANNED")
