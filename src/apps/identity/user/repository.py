from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .model import User


class UserRepository:
    def __init__(self, dbSession):
        self.dbSession: AsyncSession = dbSession

    async def get_by_username(self, username):
        result = await self.dbSession.execute(
            select(User).where(User.username == username)
        )
        return result.scalar_one_or_none()

    async def create(self, user: User):
        self.dbSession.add(user)
        await self.dbSession.commit()
        await self.dbSession.refresh(user)
        return user
