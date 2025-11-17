from fastapi import APIRouter

from .auth.routes import router as auth_router
from .user.routes import router as user_router

app_router = APIRouter()  # tags=["identity"]
app_router.include_router(user_router)
app_router.include_router(auth_router)
