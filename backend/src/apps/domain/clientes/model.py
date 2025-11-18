# import uuid
import enum

from sqlalchemy import Boolean, Enum, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from core.orm import BaseORM, OptionalEnderecoMixin, StatusMixin, TimeStampMixin


class Cliente(BaseORM, OptionalEnderecoMixin, StatusMixin, TimeStampMixin):
    class TipoClienteEnum(enum.Enum):
        PF = "pf"
        PJ = "pj"

    def validate(self):
        if self.tipo == self.TipoClienteEnum.PF:
            if not self.cpf:
                raise ValueError("CPF obrigatório para tipo PF")
            if self.cnpj:
                raise ValueError("CNPJ não permitido para PF")

        if self.tipo == self.TipoClienteEnum.PJ:
            if not self.cnpj:
                raise ValueError("CNPJ obrigatório para tipo PJ")
            if self.cpf:
                raise ValueError("CPF não permitido para PJ")

    __tablename__ = "clientes"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(
        String(100), nullable=False, unique=True, index=True
    )
    tipo: Mapped[TipoClienteEnum] = mapped_column(Enum(TipoClienteEnum), nullable=False)
    cpf: Mapped[int] = mapped_column(Integer, unique=True, nullable=True)
    cnpj: Mapped[int] = mapped_column(Integer, unique=True, nullable=True)

    # TODO add contato info
