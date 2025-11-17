from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordRequestFormStrict
from sqlalchemy.ext.asyncio import AsyncSession

from apps.identity.user.model import User
from apps.identity.user.schema import UserIsMe
from core.db import get_db_session

from .dependencies import get_current_user
from .schemas import AccessToken, UserLoginRequest
from .service import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/token", response_model=AccessToken)
async def login(
    form_data: OAuth2PasswordRequestFormStrict = Depends(),
    dbSession: AsyncSession = Depends(get_db_session),
):
    #    login_type = data.grant_type or "password"

    service = AuthService(dbSession)
    return await service.login(form_data)


@router.get("/me")
async def get_me(user=Depends(get_current_user)):
    return UserIsMe.model_validate(user)
