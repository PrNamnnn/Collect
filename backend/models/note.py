from .base import Base
from sqlalchemy import String, DateTime, Text, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from datetime import datetime, timezone


class Note(Base):
    __tablename__ = "notes"

    id : Mapped[int] = mapped_column(
        primary_key=True
    )

    user_id : Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    title : Mapped[str] = mapped_column(
        String(100), 
    default="Untitled Notebook"
    )

    content : Mapped[str] = mapped_column(
        Text
    )

    created_date : Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        default=lambda: datetime.now(timezone.utc)
    )

    last_edited : Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        default=lambda: datetime.now(timezone.utc), 
        onupdate=lambda : datetime.now(timezone.utc)
    )
    
    importance : Mapped[str] = mapped_column(
        String(100), 
        default="Unknown"
    )
