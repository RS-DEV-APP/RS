from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey
from ..db import Base

class Title(Base):
    __tablename__ = "titles"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    type: Mapped[str] = mapped_column(String(16))  # MOVIE|SERIES
    name: Mapped[str] = mapped_column(String(255), index=True)
    original_title: Mapped[str | None] = mapped_column(String(255), nullable=True)
    production_year: Mapped[int | None] = mapped_column(Integer, nullable=True)
    vendor: Mapped[str | None] = mapped_column(String(255), nullable=True)

    episodes = relationship("Episode", back_populates="title", cascade="all, delete-orphan")
