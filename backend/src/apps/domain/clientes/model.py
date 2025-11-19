# import uuid
import enum

from sqlalchemy import Boolean, Enum, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.orm import BaseORM, StatusMixin, TimeStampMixin


class TipoCliente(enum.Enum):
    PF = "pf"
    PJ = "pj"


class Cliente(BaseORM, StatusMixin, TimeStampMixin):
    __tablename__ = "clientes"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    # property name = fullname se pf razao_social se pj
    """  name: Mapped[str] = mapped_column(
        String(100), nullable=False, unique=True, index=True
    ) """

    tipo: Mapped[TipoCliente] = mapped_column(Enum(TipoCliente), nullable=False)

    # Define polimorfismo
    __mapper_args__ = {
        "polymorphic_on": tipo,
        "polymorphic_identity": "cliente",  # opcional, mas deixa explicito
    }

    # Endereços (mesmo para PF e PJ)
    enderecos: Mapped[list["ClienteEndereco"]] = relationship(
        back_populates="cliente",
        cascade="all, delete-orphan",
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
    telefone: Mapped[str | None]
    email: Mapped[str | None]

    cpf: Mapped[str] = mapped_column(String(14), nullable=False, unique=True)

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

    telefone: Mapped[str | None]
    email: Mapped[str | None]

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
    telefone: Mapped[str | None]
    email: Mapped[str | None]

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
