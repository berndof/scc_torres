from uuid import UUID

from pydantic import ConfigDict, EmailStr, Field

from core.schema import BaseSchema, ModelSchema


class UserCreate(BaseSchema):
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "username": "berndof",
                "first_name": "Bernd",
                "last_name": "Of",
                "telefone": "11987654321",
                "password": "S3nh@Fort3",
                "email": "bernd@example.com",
            }
        }
    )

    username: str = Field(
        ...,
        min_length=3,
        max_length=50,
        pattern=r"^[a-zA-Z0-9_.-]+$",
        description="Identificador único. Aceita letras, números e _ . -",
    )

    first_name: str = Field(
        ...,
        min_length=1,
        max_length=120,
    )

    last_name: str = Field(
        ...,
        min_length=1,
        max_length=120,
    )

    telefone: str | None = Field(
        default=None,
        min_length=8,
        max_length=20,
        pattern=r"^\d+$",
        description="Telefone sem máscara (apenas dígitos).",
    )

    password: str = Field(
        ...,
        min_length=8,
        max_length=128,
    )

    email: EmailStr | None = Field(
        default=None,
    )


class UserResponse(ModelSchema):
    id: UUID
    username: str
    # email: str


class NewUserResponse(UserResponse): ...


class UserIsMe(UserResponse):
    password: str
