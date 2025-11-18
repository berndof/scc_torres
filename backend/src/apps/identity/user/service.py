from .model import User
from .schema import NewUserResponse, UserCreate


class UserService:
    def __init__(self, dbSession):
        self.dbSession = dbSession

    async def create(self, data: UserCreate):
        new_user = User(**data.model_dump())
        # Handle erro de repetidos
        # TODO
        self.dbSession.add(new_user)

        await self.dbSession.commit()
        await self.dbSession.refresh(new_user)

        response = NewUserResponse.model_validate(new_user)
        return response
