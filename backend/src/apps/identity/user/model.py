import uuid
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, DateTime, Enum, Integer, String, Uuid, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from apps.identity.group.model import group_members
from core.orm import BaseORM, ObjectStatus

if TYPE_CHECKING:
    from apps.identity.group.model import Group


class User(BaseORM):
    __tablename__ = "users"
    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)

    username: Mapped[str] = mapped_column(
        String(50), unique=True, nullable=False, index=True
    )

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    first_name: Mapped[str] = mapped_column(String(120), nullable=False)
    last_name: Mapped[str] = mapped_column(String(120), nullable=False)

    telefone: Mapped[int] = mapped_column(Integer(), nullable=True)

    status: Mapped[ObjectStatus] = mapped_column(
        Enum(ObjectStatus), default=ObjectStatus.ENABLE, nullable=False
    )

    password: Mapped[str] = mapped_column(
        String(255), nullable=False
    )  # set nullable para true

    email: Mapped[str] = mapped_column(
        String(100), nullable=True, index=True, unique=True
    )

    from_ad: Mapped[bool] = mapped_column(Boolean(), default=False, nullable=False)

    groups: Mapped[list["Group"]] = relationship(
        "Group", secondary=group_members, back_populates="members", lazy="selectin"
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), server_onupdate=func.now()
    )
