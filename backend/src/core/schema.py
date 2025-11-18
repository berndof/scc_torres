from pydantic import BaseModel, ConfigDict


class BaseSchema(BaseModel): ...


class ModelSchema(BaseSchema):
    model_config = ConfigDict(from_attributes=True)


class OptionalEnderecoSchema(BaseSchema):
    logradouro: str | None
    numero: int | None
    complemento: str | None
    bairro: str | None
    cidade: str | None
    estado: str | None
    cep: int | None

    # TODO validate
