from fastapi import APIRouter, Depends

from core.db import get_db_session

# from .repository import UserRepository
from .schema import ClienteCreate
from .service import ClienteService

router = APIRouter(prefix="/clientes", tags=["clientes"])


@router.post("/create")
async def create_cliente(data: ClienteCreate, dbSession=Depends(get_db_session)):
    service = ClienteService(dbSession)
    return await service.create(data)
