from logging import getLogger

from sqlalchemy.ext.asyncio import AsyncSession

from .model import ClientePessoa
from .schema import ClientePessoaCreate, ClienteResponse

logger = getLogger("app.cliente.service")
# logger.setLevel("DEBUG")


class ClienteService:
    def __init__(self, dbSession: AsyncSession):
        self.dbSession: AsyncSession = dbSession

    """ async def create(self, data: ClienteCreate):
        payload = data.model_dump()
        endereco = payload.pop("endereco", None)
        if endereco:
            for key, value in endereco.items():
                payload[key] = value

        cliente = Cliente(**payload)

        self.dbSession.add(cliente)

        await self.dbSession.commit()
        await self.dbSession.refresh(cliente)

        response = ClienteResponse.model_validate(cliente)
        return response """

    async def cliente_pessoa_create(self, data: ClientePessoaCreate):
        payload = data.model_dump()
        data_enderecos = payload.pop("enderecos")

        cliente_pessoa = ClientePessoa(**payload)
        self.dbSession.add(cliente_pessoa)
        await self.dbSession.commit()
        await self.dbSession.refresh(cliente_pessoa)

        logger.debug(cliente_pessoa)
        logger.debug(f"endereço {data_enderecos}")

        return
