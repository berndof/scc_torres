from sqlalchemy import not_, select
from sqlalchemy.ext.asyncio import AsyncSession

from .model import User


class UserRepository:
    def __init__(self, dbSession):
        self.dbSession: AsyncSession = dbSession

    async def get_one_by(self, key, value):
        if hasattr(User, key):
            attr = getattr(User, key)
            result = await self.dbSession.execute(select(User).where(attr == value))
        return result.scalar_one_or_none

    async def get_by_username(self, username: str, from_ad: bool = False):
        if from_ad:  # somente do ad
            result = await self.dbSession.execute(
                select(User).where(User.username == username, User.from_ad)
            )

        else:
            result = await self.dbSession.execute(  # default user local
                select(User).where(User.username == username, not_(User.from_ad))
            )

        return result.scalar_one_or_none()

    async def get_by_id(self, id):
        result = await self.dbSession.execute(select(User).where(User.id == id))
        return result.scalar_one_or_none()

    async def create(self, user: User):
        self.dbSession.add(user)
        await self.dbSession.commit()
        await self.dbSession.refresh(user)
        return user
