from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String
from ..db import Base

class Channel(Base):
    __tablename__ = "channels"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), unique=True)
    timezone: Mapped[str] = mapped_column(String(64), default="Europe/Berlin")
    country: Mapped[str | None] = mapped_column(String(2), nullable=True)
