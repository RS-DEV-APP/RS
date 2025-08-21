from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String
from ..db import Base

class Right(Base):
    __tablename__ = "rights"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    contract_id: Mapped[int] = mapped_column(Integer)
    title_id: Mapped[int] = mapped_column(Integer, index=True)
    right_type: Mapped[str] = mapped_column(String(32))  # EXHIBITION|VOD|CATCHUP
    territories: Mapped[str] = mapped_column(String(255))  # CSV, e.g., DE,AT,CH
    languages: Mapped[str] = mapped_column(String(255))
    platforms: Mapped[str] = mapped_column(String(255))
    start: Mapped[str] = mapped_column(String(20))  # ISO datetime
    end: Mapped[str] = mapped_column(String(20))
    exclusivity: Mapped[str | None] = mapped_column(String(32), nullable=True)
    blackout_dates: Mapped[str | None] = mapped_column(String(255), nullable=True)
    plays_cap: Mapped[int | None] = mapped_column(Integer, nullable=True)
