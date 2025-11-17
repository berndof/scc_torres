import uuid
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, ForeignKey, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.orm import BaseORM

if TYPE_CHECKING:
    from apps.identity.group.model import Group, group_members


class User(BaseORM):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    username: Mapped[str] = mapped_column(
        String(50), unique=True, nullable=False, index=True
    )
    password: Mapped[str] = mapped_column(
        String(50), nullable=False
    )  # set nullable para true

    # email: Mapped[str] = mapped_column(
    #    String(100), nullable=False, index=True, unique=True
    # )

    from_ad: Mapped[bool] = mapped_column(Boolean(), default=False, nullable=False)

    groups: Mapped[list["Group"]] = relationship(
        "Group", secondary="group_members", back_populates="members", lazy="selectin"
    )
