from fastapi import APIRouter, Depends

from core.db import get_db_session

from .schema import NewUserResponse, UserCreate
from .service import UserService

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/create", response_model=NewUserResponse)
async def create_user(data: UserCreate, dbSession=Depends(get_db_session)):
    service = UserService(dbSession)
    return await service.create(data)
