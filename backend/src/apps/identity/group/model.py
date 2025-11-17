from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import Column, ForeignKey, String, Table, Text, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.orm import BaseORM

if TYPE_CHECKING:
    from apps.identity.user.model import User


group_members = Table(
    "group_members",
    BaseORM.metadata,
    Column(
        "group_id", ForeignKey(column="groups.id", ondelete="CASCADE"), primary_key=True
    ),
    Column(
        "user_id", ForeignKey(column="users.id", ondelete="CASCADE"), primary_key=True
    ),
)


class Group(BaseORM):
    __tablename__ = "groups"
    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, default=uuid4, unique=True)
    name: Mapped[str] = mapped_column(
        String(50), unique=True, nullable=False, index=True
    )
    description: Mapped[str] = mapped_column(Text, nullable=True)

    members: Mapped[list["User"]] = relationship(
        "User", secondary="group_members", back_populates="groups", lazy="selectin"
    )
