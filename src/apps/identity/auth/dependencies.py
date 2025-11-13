from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from apps.identity.user.repository import UserRepository
from core.db import AsyncSession, get_db_session
from core.security import decode_token

oauth2_schema = OAuth2PasswordBearer(
    tokenUrl="/v1/auth/token",
    scopes={
        "ldap": "Autenticação via AD",
        "local": "Autenticação com usuário do sistema",
    },
)


async def get_current_user(
    token: str = Depends(oauth2_schema),
    dbSession: AsyncSession = Depends(get_db_session),
):
    print(f"aaaaaa {token}")
    payload = decode_token(token)
    if not payload or "sub" not in payload:
        raise HTTPException(401, "Invalid token")

    user_repo = UserRepository(dbSession)
    user = await user_repo.get_by_id(payload["sub"])
    if not user:
        raise HTTPException(401, "User not found")

    return user
