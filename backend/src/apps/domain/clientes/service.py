from sqlalchemy.ext.asyncio import AsyncSession

from .model import Cliente
from .schema import ClienteCreate, ClienteResponse


class ClienteService:
    def __init__(self, dbSession: AsyncSession):
        self.dbSession: AsyncSession = dbSession

    async def create(self, data: ClienteCreate):
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
        return response
