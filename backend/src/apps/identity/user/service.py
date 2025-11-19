from sqlalchemy import not_, select

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

    async def get_by_id(self, id: str):
        stmt = select(User).where(User.id == id)
        result = await self.dbSession.execute(stmt)
        user = result.scalar_on_or_none()
        return user

    async def get_by_username(self, username: str, from_ad: bool = False):
        stmt = select(User).where(User.username == username)
        if from_ad:
            stmt = stmt.where(User.from_ad)
        else:
            stmt = stmt.where(not_(User.from_ad))
        result = await self.dbSession.execute(stmt)
        user = result.scalar_one_or_none()
        return user
