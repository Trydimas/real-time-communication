import uuid

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, DateTime, Boolean, ForeignKey
from sqlalchemy.sql import func
from db import Base
from datetime import datetime, timezone
from enum import Enum


class StatusEnum(str, Enum):
    DANGEGOUSE = "Dangerouse"
    WARNING = "Warning"
    INFO = "Info"
    NAN = "NAN"


class Message(Base):
    id: Mapped[str] = mapped_column(primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    text: Mapped[str] = mapped_column(String, nullable=False)
    is_checked: Mapped[bool] = mapped_column(Boolean, default=False)
    status:Mapped[StatusEnum] = mapped_column(String, default=StatusEnum.NAN)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(),
                                                 onupdate=func.now())
    user: Mapped["User"] = relationship(back_populates="messages")
