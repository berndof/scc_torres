from fastapi import APIRouter, Depends

from core.db import get_db_session

# from .repository import UserRepository
from .schema import ClienteOut, ClientePessoaCreate, NewClientePessoa
from .service import ClienteService

router = APIRouter(prefix="/clientes", tags=["clientes"])


@router.post("/create/pf", response_model=NewClientePessoa)
async def create_cliente(data: ClientePessoaCreate, dbSession=Depends(get_db_session)):
    service = ClienteService(dbSession)
    return await service.cliente_pessoa_create(data)


@router.get("/list", response_model=list[ClienteOut])
async def list_cliente(dbSession=Depends(get_db_session)):
    service = ClienteService(dbSession)
    return await service.list_clientes()
