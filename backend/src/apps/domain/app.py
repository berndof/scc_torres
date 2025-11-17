from fastapi import APIRouter

from .terrenos.routes import router as terrenos_router

# from .user.routes import router as user_router

app_router = APIRouter()  # tags=["domain"]
app_router.include_router(terrenos_router)
# app_router.include_router(auth_router)
