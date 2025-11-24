from typing import Annotated, List, Literal, Union

from pydantic import ConfigDict, EmailStr, Field, constr

from core.schema import BaseSchema, ModelSchema


class ClienteEnderecoOut(ModelSchema):
    # id: int
    logradouro: str | None
    numero: int | None
    # complemento: str | None
    bairro: str | None
    cidade: str | None
    estado: str | None
    cep: str | None
    # latitude: float | None
    # longitude: float | None


# Cliente Pessoa de retorno
class NewClientePessoa(ModelSchema):
    id: int
    first_name: str
    last_name: str
    cpf: str
    telefone: str | None
    email: EmailStr | None
    # enderecos: list[ClienteEnderecoOut] | None = []


class ClienteEnderecoCreate(BaseSchema):
    logradouro: str | None = Field(..., max_length=255)
    numero: int | None = Field(...)
    # complemento: str | None = Field(..., max_length=255)
    bairro: str | None = Field(..., max_length=255)
    cidade: str | None = Field(..., max_length=255)
    estado: str | None = Field(..., max_length=255)

    cep: str | None = Field(..., min_length=8, max_length=8, pattern=r"^\d{8}$")

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

    endereco: ClienteEnderecoCreate | None = None


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

    enderecos: ClienteEnderecoCreate | None = None
    contatos: list[ClienteEmpresaContatoCreate] | None = []


class ClienteList(BaseSchema): ...


class ClientePessoaOut(ModelSchema):
    # model_config = {"use_enum_values": True}
    ...
    tipo: Literal["pf"]
    id: int
    first_name: str
    last_name: str
    telefone: str | None
    email: str | None
    cpf: str

    # enderecos: list[ClienteEnderecoOut]


class ClienteBaseOut(ModelSchema):
    model_config = {"populate_by_name": True}
    tipo: str


class ClienteEmpresaContatoOut(ClienteBaseOut):
    id: int
    first_name: str
    last_name: str
    telefone: str | None
    email: str | None


class ClienteEmpresaOut(ClienteBaseOut):
    # model_config = {"use_enum_values": True}
    ...
    tipo: Literal["pj"]
    id: int
    razao_social: str
    cnpj: str
    telefone: str | None
    email: str | None
    contatos: list[ClienteEmpresaContatoOut]
    enderecos: list[ClienteEnderecoOut]


ClienteOut = Annotated[
    Union[ClientePessoaOut, ClienteEmpresaOut],
    Field(discriminator="tipo"),
]
