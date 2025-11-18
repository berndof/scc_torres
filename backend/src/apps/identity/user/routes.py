from fastapi import APIRouter, Depends

from core.db import get_db_session

from .repository import UserRepository
from .schema import UserCreate, UserResponse
from .service import UserService

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/create", response_model=UserResponse)
async def create_user(data: UserCreate, dbSession=Depends(get_db_session)):
    service = UserService(dbSession)
    return await service.create(data)


@router.post("/register", response_model=UserResponse)
async def register_user(data: UserCreate, dbSession=Depends(get_db_session)):
    service = UserService(dbSession)
    return await service.create(data)
