from fastapi import APIRouter

from .clientes.routes import router as clientes_routes
from .terrenos.routes import router as terrenos_router

# from .user.routes import router as user_router

app_router = APIRouter()  # tags=["domain"]
app_router.include_router(terrenos_router)
app_router.include_router(clientes_routes)
# app_router.include_router(auth_router)
