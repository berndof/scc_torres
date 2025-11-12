from uuid import uuid4

from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from ldap3 import ALL, NTLM, Connection, Server
from sqlalchemy.ext.asyncio import AsyncSession

from apps.identity.user.repository import UserRepository
from core import ldap_client
from core.security import create_access_token, verify_password

from .schemas import AccessToken


class AuthService:
    def __init__(self, dbSession: AsyncSession):
        self.dbSession = dbSession
        self.user_repo = UserRepository(self.dbSession)

    async def login(self, data: OAuth2PasswordRequestForm) -> AccessToken:
        user = await self.user_repo.get_by_username(username=data.username)
        if not user:
            # raise HTTPException(401, "User not found")
            # tenta buscar o user no ad
            user = await ldap_client.authenticate_user(data.username, data.password)
            print(user)
            raise HTTPException(401, "User not found")

        if not verify_password(data.password, user.password):
            raise HTTPException(401, "Wrong password")

        # se passou cria a sessão
        # session_id: str = str(uuid4().hex)
        session_payload = {"sub": str(user.id)}
        token = create_access_token(session_payload)
        return AccessToken(token=token)
