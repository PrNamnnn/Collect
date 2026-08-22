from .base import Base
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import String, DateTime, Boolean, Text, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from datetime import datetime, timezone


class User(Base):
    __tablename__ = "users"

    id : Mapped[int] = mapped_column(
        primary_key=True
    )

    name : Mapped[str] = mapped_column(
        String(100), 
        nullable=True
    )

    email : Mapped[str] = mapped_column(
        String(255), 
        unique=True, 
        nullable=False
    )

    password_hash : Mapped[str] = mapped_column(
        String(255), 
        nullable=False
    )

    phone_no : Mapped[str | None] = mapped_column(
        String(15), 
        nullable=True
    )

    theme : Mapped[str] = mapped_column(
        String(50), 
        default="white"
    )

    premium : Mapped[bool] = mapped_column(
        Boolean, 
        default=False
    )

    joined_date : Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        default=lambda: datetime.now(timezone.utc)
    )







