from pydantic import ConfigDict, EmailStr, Field, constr

from core.schema import BaseSchema, ModelSchema

from .model import TipoCliente


class ClienteEnderecoOut(ModelSchema):
    id: int
    logradouro: str | None
    numero: int | None
    complemento: str
    bairro: str | None
    cidade: str | None
    estado: str | None
    cep: str | None
    latitude: float | None
    longitude: float | None


# Cliente Pessoa de retorno
class NewClientePessoa(ModelSchema):
    id: int
    first_name: str
    last_name: str
    cpf: str
    telefone: str | None
    email: EmailStr | None
    enderecos: list[ClienteEnderecoOut] = []


class ClienteEnderecoCreate(BaseSchema):
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "logradouro": "Av Paulista",
                "numero": 1000,
                "complemento": "Ap 12",
                "bairro": "Bela Vista",
                "cidade": "São Paulo",
                "estado": "SP",
                "cep": "01311000",
                "latitude": -23.561684,
                "longitude": -46.656139,
            }
        }
    )

    logradouro: str | None = Field(None, max_length=255)
    numero: int | None = None
    complemento: str | None = Field(None, max_length=255)
    bairro: str | None = Field(None, max_length=255)
    cidade: str | None = Field(None, max_length=255)
    estado: str | None = Field(None, max_length=255)

    cep: str | None = Field(None, min_length=8, max_length=8, pattern=r"^\d{8}$")

    # latitude: float | None = None
    # longitude: float | None = None


class ClientePessoaCreate(BaseSchema):
    first_name: str = Field(..., min_length=1, max_length=120, examples=["Ana"])
    last_name: str = Field(..., min_length=1, max_length=120, examples=["Silva"])

    cpf: str = Field(
        ..., min_length=11, max_length=11, pattern=r"^\d{11}$", examples=["12345678910"]
    )
    telefone: str | None = Field(
        ..., min_length=8, max_length=20, pattern=r"^\d+$", examples=[11987654321]
    )
    email: EmailStr | None = Field(..., examples=["example@exam.com"])

    endereco: ClienteEnderecoCreate | None = Field(...)


class ClienteEmpresaContatoCreate(BaseSchema):
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "first_name": "João",
                "last_name": "Campos",
                "telefone": "11999998888",
                "email": "joao.campos@example.com",
            }
        }
    )

    first_name: str = Field(..., min_length=1, max_length=120)
    last_name: str = Field(..., min_length=1, max_length=120)
    telefone: str | None = Field(None, min_length=8, max_length=20, pattern=r"^\d+$")
    email: EmailStr | None = None


class ClienteEmpresaCreate(BaseSchema):
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "tipo": "pj",
                "razao_social": "Acme Ltda",
                "cnpj": "12345678000199",
                "telefone": "1133334444",
                "email": "contato@acme.com",
            }
        }
    )

    razao_social: str = Field(..., min_length=1, max_length=255)
    cnpj: str = Field(..., min_length=14, max_length=14, pattern=r"^\d{14}$")

    telefone: str | None = Field(None, min_length=8, max_length=20, pattern=r"^\d+$")
    email: EmailStr | None = None

    enderecos: ClienteEnderecoCreate | None = Field(...)
    contatos: list[ClienteEmpresaContatoCreate] | None = []
