from core.schema import BaseSchema, ModelSchema, OptionalEnderecoSchema

from .model import TipoCliente


class ClienteResponse(ModelSchema):
    name: str
    tipo: TipoCliente


class ClienteCreate(BaseSchema):
    name: str
    tipo: TipoCliente = TipoCliente.PF
    cpf: int | None
    cnpj: int | None
    endereco: OptionalEnderecoSchema

    # TODO validate documentos
