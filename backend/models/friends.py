from .base import Base
from sqlalchemy import String, DateTime, Text, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from datetime import datetime, timezone

class FriendShip(Base):
    __tablename__ = "friendships"

    id : Mapped[int] = mapped_column(
        primary_key=True
    )


    sender_id : Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    reciever_id : Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    status : Mapped[str] = mapped_column(
        String(50),
        default="pending"
    )

