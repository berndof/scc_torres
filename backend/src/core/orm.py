import enum
import uuid
from datetime import datetime

from sqlalchemy import DateTime, Enum, Float, ForeignKey, Integer, String, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class BaseORM(DeclarativeBase):
    __mapper_args__ = {"eager_defaults": True}

    def __repr__(self) -> str:
        attrs = ", ".join(
            f"{key}={value!r}"
            for key, value in self.__dict__.items()
            if not key.startswith("_")
        )
        return f"<{self.__class__.__name__}({attrs})>"


class OptionalEnderecoMixin:
    logradouro: Mapped[str] = mapped_column(String(255), nullable=True)
    numero: Mapped[int] = mapped_column(Integer(), nullable=True)
    complemento: Mapped[str] = mapped_column(String(255), nullable=True)
    bairro: Mapped[str] = mapped_column(String(255), nullable=True)
    cidade: Mapped[str] = mapped_column(String(255), nullable=True)
    estado: Mapped[str] = mapped_column(String(255), nullable=True)
    cep: Mapped[int] = mapped_column(Integer, nullable=True)


class GeolocationMixin:
    latitude: Mapped[float] = mapped_column(Float)
    longitude: Mapped[float] = mapped_column(Float)


class StatusMixin:
    class StatusEnum(enum.Enum):
        ENABLE = "enable"
        DISABLE = "disable"
        DELETED = "deleted"

    status: Mapped[StatusEnum] = mapped_column(
        Enum, default=StatusEnum.ENABLE, nullable=False
    )

    def disable(self):
        self.status = self.StatusEnum.DISABLE


class OwnerMixin:
    owner_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), nullable=False)


class TimeStampMixin:
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), server_onupdate=func.now()
    )
