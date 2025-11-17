# from fastapi.security import O

from core.schema import BaseSchema


class UserLoginRequest(BaseSchema):
    username: str
    password: str


class AccessToken(BaseSchema):
    access_token: str
    token_type: str = "bearer"
