from .model import User
from .repository import UserRepository
from .schema import UserCreate


class UserService:
    def __init__(self, dbSession):
        self.dbSession = dbSession
        self.user_repo = UserRepository(dbSession)

    async def create(self, data: UserCreate):
        user = User(**data.model_dump())
        return await self.user_repo.create(user)
        # Handle erro de repetidos
