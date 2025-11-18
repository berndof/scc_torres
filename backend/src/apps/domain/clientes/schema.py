from validate_docbr import CNPJ, CPF

from core.schema import BaseSchema, ModelSchema, OptionalEnderecoSchema

from .model import Cliente


class ClienteResponse(ModelSchema):
    name: str
    tipo: Cliente.TipoClienteEnum


class ClienteCreate(BaseSchema):
    name: str
    tipo: Cliente.TipoClienteEnum = Cliente.TipoClienteEnum.PF
    cpf: int | None
    cnpj: int | None
    endereco: OptionalEnderecoSchema

    # TODO validate documentos
