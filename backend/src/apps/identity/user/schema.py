from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator

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

    """ @field_validator("password")
    @classmethod
    def validate_password(cls, v: str) -> str:
        if len(v) < 8:
            raise ValueError("A senha deve ter pelo menos 8 caracteres.")

        if not re.search(r"[A-Za-z]", v):
            raise ValueError("A senha deve conter pelo menos uma letra.")

        if not re.search(r"\d", v):
            raise ValueError("A senha deve conter pelo menos um número.")

        return v

    @field_validator("username")
    @classmethod
    def validate_username(cls, v: str) -> str:
        if not re.match(r"^[a-zA-Z][a-zA-Z0-9._]{2,29}$", v):
            raise ValueError("Username inválido. Use letras, números, . ou _, começando com letra (3-30 chars).")
        return v

    @field_validator("telefone")
    @classmethod
    def validate_phone(cls, v: int | None) -> int | None:
        if v is None:
            return v

        digits = str(v)
        if not digits.isdigit() or len(digits) < 8 or len(digits) > 13:
            raise ValueError("Telefone inválido. Deve conter entre 8 e 13 dígitos numéricos.")
        return v """


class UserResponse(ModelSchema):
    id: UUID
    username: str
    # email: str


class NewUserResponse(UserResponse): ...


class UserIsMe(UserResponse):
    password: str
