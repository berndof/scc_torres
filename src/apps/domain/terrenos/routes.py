from fastapi import APIRouter, Depends

from core.db import get_db_session

# from .repository import UserRepository
# from .schema import UserCreate, UserResponse
# from .service import UserService

router = APIRouter(prefix="/terrenos", tags=["terrenos"])


@router.post("/create")
async def create_user():
    return "Hello"
