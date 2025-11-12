import uuid

from sqlalchemy import Boolean, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column

from core.orm import BaseORM


class User(BaseORM):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid, primary_key=True, default=uuid.uuid4, unique=True
    )
    username: Mapped[str] = mapped_column(
        String(255), unique=True, nullable=False, index=True
    )
    password: Mapped[str] = mapped_column(
        String(255), nullable=False
    )  # set nullable para true

    # email: Mapped[str] = mapped_column(
    #    String(100), nullable=False, index=True, unique=True
    # )

    from_ad: Mapped[bool] = mapped_column(Boolean(), default=False, nullable=False)
