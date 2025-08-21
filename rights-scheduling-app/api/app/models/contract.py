from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Date
from ..db import Base

class Contract(Base):
    __tablename__ = "contracts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    counterparty: Mapped[str] = mapped_column(String(255))
    start_date: Mapped[str] = mapped_column(String(10))  # ISO date
    end_date: Mapped[str] = mapped_column(String(10))
    currency: Mapped[str] = mapped_column(String(8), default="EUR")
    payment_terms: Mapped[str | None] = mapped_column(String(255), nullable=True)
