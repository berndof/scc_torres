from fastapi import APIRouter

from .user.routes import router as user_router

app_router = APIRouter(tags=["identity"])


app_router.include_router(user_router)
