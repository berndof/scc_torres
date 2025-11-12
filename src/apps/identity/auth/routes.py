from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from apps.identity.user.model import User
from apps.identity.user.schema import UserIsMe
from core.db import get_db_session

from .dependencies import get_current_user
from .schemas import AccessToken
from .service import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/token", response_model=AccessToken)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    dbSession: AsyncSession = Depends(get_db_session),
):
    service = AuthService(dbSession)
    return await service.login(form_data)


@router.get("/me")
async def get_me(user=Depends(get_current_user)):
    return UserIsMe.model_validate(user)
