from contextlib import asynccontextmanager

import uvicorn
from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

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

api_root_router = APIRouter(prefix="/v1")
api_root_router.include_router(identity_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_root_router)

""" if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host=APP_LISTEN_ADDR,
        port=APP_LISTEN_PORT,
        # log_config=LOGGING_CONFIG,
        reload=True,
        loop="uvloop",
        reload_dirs=["src/"],
        reload_delay=1.0,
    ) """
