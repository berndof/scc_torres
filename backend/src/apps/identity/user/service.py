from .model import User
from .repository import UserRepository
from .schema import UserCreate


class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    async def create(self, data: UserCreate):
        user = User(**data.model_dump())
        return await self.repo.create(user)
        # Handle erro de repetidos
