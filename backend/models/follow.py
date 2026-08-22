from .base import Base
from sqlalchemy import String, DateTime, Text, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from datetime import datetime, timezone


class Follow(Base):
    __tablename__ = "follows"

    follower_id : Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        primary_key=True
    )

    following_id : Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        primary_key=True
    )
