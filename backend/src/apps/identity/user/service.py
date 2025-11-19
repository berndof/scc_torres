from core.security import hash_password

from .model import User
from .schema import NewUserResponse, UserCreate


class UserService:
    def __init__(self, dbSession):
        self.dbSession = dbSession

    async def create(self, data: UserCreate):
        payload = data.model_dump()

        raw_pass = payload.pop("password")
        hashed_pass = hash_password(raw_pass)

        new_user = User(**payload, password=hashed_pass)
        # Handle erro de repetidos
        # TODO
        self.dbSession.add(new_user)
        await self.dbSession.commit()
        await self.dbSession.refresh(new_user)

        response = NewUserResponse.model_validate(new_user)
        return response
