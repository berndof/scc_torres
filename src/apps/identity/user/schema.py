from uuid import UUID

from pydantic import EmailStr, field_validator

from core.schema import BaseSchema, ModelSchema
from core.security import hash_password


class UserCreate(BaseSchema):
    username: str
    password: str
    from_ad: bool = False
    # email: EmailStr

    @field_validator("password")
    @classmethod
    def validate_password(cls, password: str) -> str:
        password.encode("utf-8")
        return hash_password(password)


class UserResponse(ModelSchema):
    id: UUID
    username: str
    from_ad: bool
    # email: str


class UserIsMe(UserResponse):
    password: str
