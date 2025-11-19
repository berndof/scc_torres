from logging import getLogger

from sqlalchemy.ext.asyncio import AsyncSession

from .model import ClienteEndereco, ClientePessoa
from .schema import ClientePessoaCreate

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
        data_endereco = payload.pop("endereco")

        cliente_pessoa = ClientePessoa(**payload)
        self.dbSession.add(cliente_pessoa)
        await self.dbSession.flush()
        # logger.debug(cliente_pessoa)

        # nderecos_criados = []
        if data_endereco:
            cliente_endereco = ClienteEndereco(
                **data_endereco, cliente_id=cliente_pessoa.id
            )
            # enderecos_criados.append(cliente_endereco)
            # relacionar o endereco com o cliente aqui
            self.dbSession.add(cliente_endereco)

        await self.dbSession.commit()
        await self.dbSession.refresh(cliente_pessoa, attribute_names=["enderecos"])

        # provavelmente fazer so um commit aqui

        return cliente_pessoa
