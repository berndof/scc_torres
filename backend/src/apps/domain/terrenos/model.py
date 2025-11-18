# import uuid

from sqlalchemy import Boolean, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from core.orm import BaseORM, GeolocationMixin, StatusMixin, TimeStampMixin


class Terreno(BaseORM, StatusMixin, TimeStampMixin, GeolocationMixin):
    __tablename__ = "terrenos"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)

    # TODO
    # audit
    # empresa_responvael
    # alugado
    # custo
    # rendimento
