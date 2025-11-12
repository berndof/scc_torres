import uuid
from typing import Literal

from sqlalchemy import Integer, Uuid
from sqlalchemy.orm import DeclarativeBase, Mapped, declared_attr, mapped_column


class BaseORM(DeclarativeBase):
    __mapper_args__ = {"eager_defaults": True}

    def __repr__(self) -> str:
        attrs = ", ".join(
            f"{key}={value!r}"
            for key, value in self.__dict__.items()
            if not key.startswith("_")
        )
        return f"<{self.__class__.__name__}({attrs})>"
