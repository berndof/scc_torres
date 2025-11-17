from contextlib import asynccontextmanager

from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from apps.domain.app import app_router as domain_router
from apps.identity.app import app_router as identity_router
from core.config import APP_ENV


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        ...
        yield
    except:
        raise


docs_url = "/docs" if APP_ENV == "dev" else None

app = FastAPI(lifespan=lifespan, docs_url=docs_url)

root_api_router = APIRouter(prefix="/v1")
root_api_router.include_router(identity_router)
root_api_router.include_router(domain_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(root_api_router)
