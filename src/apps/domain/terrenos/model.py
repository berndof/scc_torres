# import uuid

from sqlalchemy import Boolean, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from core.orm import BaseORM


class Terreno(BaseORM):
    __tablename__ = "terrenos"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    latitude: Mapped[float] = mapped_column(Float, nullable=False, unique=True)
    longitude: Mapped[float] = mapped_column(Float, nullable=False, unique=True)
    endereco: Mapped[str] = mapped_column(String(255), nullable=True)  # opcional

    # TODO
    # audit
    # empresa_responvael
    # alugado
    # custo
    # rendimento
