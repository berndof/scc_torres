from uuid import UUID

from pydantic import EmailStr, field_validator

from core.schema import BaseSchema, ModelSchema


class UserCreate(BaseSchema):
    username: str
    first_name: str
    last_name: str
    telefone: int | None = None
    password: str
    email: EmailStr | None = None

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
