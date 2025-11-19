# import uuid
import enum
from datetime import datetime

from sqlalchemy import DateTime, Enum, Float, ForeignKey, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.orm import BaseORM, ObjectStatus


class TipoCliente(enum.Enum):
    PF = "pf"
    PJ = "pj"


class Cliente(BaseORM):
    __tablename__ = "clientes"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    # property name = fullname se pf razao_social se pj
    tipo: Mapped[TipoCliente] = mapped_column(Enum(TipoCliente), nullable=False)

    # Define polimorfismo
    __mapper_args__ = {
        "polymorphic_on": tipo,
        "polymorphic_identity": "cliente",  # opcional, mas deixa explicito
    }

    status: Mapped[ObjectStatus] = mapped_column(
        Enum(ObjectStatus), default=ObjectStatus.ENABLE, nullable=False
    )

    # Endereços (mesmo para PF e PJ)
    enderecos: Mapped[list["ClienteEndereco"]] = relationship(
        back_populates="cliente",
        cascade="all, delete-orphan",
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), server_onupdate=func.now()
    )


class ClientePessoa(Cliente):
    __tablename__ = "clientes_pf"

    id: Mapped[int] = mapped_column(
        ForeignKey("clientes.id", ondelete="CASCADE"),
        primary_key=True,
    )

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    first_name: Mapped[str] = mapped_column(String(120), nullable=False)
    last_name: Mapped[str] = mapped_column(String(120), nullable=False)

    telefone: Mapped[int] = mapped_column(Integer(), nullable=True)
    email: Mapped[str] = mapped_column(
        String(100), nullable=True, index=True, unique=True
    )

    cpf: Mapped[int] = mapped_column(Integer(), nullable=False, unique=True)

    __mapper_args__ = {"polymorphic_identity": TipoCliente.PF}


class ClienteEmpresa(Cliente):
    __tablename__ = "clientes_pj"

    id: Mapped[int] = mapped_column(
        ForeignKey("clientes.id", ondelete="CASCADE"),
        primary_key=True,
    )

    razao_social: Mapped[str] = mapped_column(String(255), nullable=False)
    cnpj: Mapped[str] = mapped_column(String(18), nullable=False, unique=True)

    contatos: Mapped[list["ClienteEmpresaContato"]] = relationship(
        back_populates="empresa",
        cascade="all, delete-orphan",
    )

    telefone: Mapped[int] = mapped_column(Integer(), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=True, index=True)

    __mapper_args__ = {"polymorphic_identity": TipoCliente.PJ}


class ClienteEmpresaContato(BaseORM):
    __tablename__ = "clientes_pj_contatos"

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    empresa_id: Mapped[int] = mapped_column(
        ForeignKey("clientes_pj.id", ondelete="CASCADE"), nullable=False
    )

    first_name: Mapped[str] = mapped_column(String(120), nullable=False)
    last_name: Mapped[str] = mapped_column(String(120), nullable=False)
    telefone: Mapped[int] = mapped_column(Integer(), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=True, index=True)

    empresa: Mapped["ClienteEmpresa"] = relationship(back_populates="contatos")


class ClienteEndereco(BaseORM):
    __tablename__ = "clientes_enderecos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    cliente_id: Mapped[int] = mapped_column(
        ForeignKey("clientes.id", ondelete="CASCADE"),
        nullable=False,
    )

    logradouro: Mapped[str | None] = mapped_column(String(255))
    numero: Mapped[int | None] = mapped_column(Integer)
    complemento: Mapped[str | None] = mapped_column(String(255))
    bairro: Mapped[str | None] = mapped_column(String(255))
    cidade: Mapped[str | None] = mapped_column(String(255))
    estado: Mapped[str | None] = mapped_column(String(255))
    cep: Mapped[int | None] = mapped_column(Integer)

    cliente: Mapped["Cliente"] = relationship(back_populates="enderecos")

    latitude: Mapped[float] = mapped_column(Float, nullable=True)
    longitude: Mapped[float] = mapped_column(Float, nullable=True)
