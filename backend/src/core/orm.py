import enum

from sqlalchemy.orm import DeclarativeBase


class BaseORM(DeclarativeBase):
    __mapper_args__ = {"eager_defaults": True}

    def __repr__(self) -> str:
        attrs = ", ".join(
            f"{key}={value!r}"
            for key, value in self.__dict__.items()
            if not key.startswith("_")
        )
        return f"<{self.__class__.__name__}({attrs})>"


class ObjectStatus(enum.Enum):
    ENABLE = "enable"
    DISABLE = "disable"
    DELETED = "deleted"
