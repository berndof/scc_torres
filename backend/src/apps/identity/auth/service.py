from logging import getLogger

from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from ldap3.core.exceptions import LDAPBindError
from sqlalchemy.ext.asyncio import AsyncSession

from apps.identity.user.model import User
from apps.identity.user.service import UserService
from core.ldap_client import ldap_get_user_info
from core.security import create_access_token, verify_password

from .schemas import AccessToken

logger = getLogger("app.auth.service")
logger.setLevel("DEBUG")


class AuthService:
    def __init__(self, dbSession: AsyncSession):
        self.dbSession = dbSession
        self.user_service = UserService(self.dbSession)

    async def login(self, data: OAuth2PasswordRequestForm) -> AccessToken:
        login_type = "local"
        if data.scopes and len(data.scopes) >= 0:
            login_type = data.scopes[0]
        logger.debug(f"login type: {login_type}")
        if login_type == "local":
            return await self.local_login(data)
        if login_type == "ldap":
            return await self.ldap_login(data)
        else:
            raise HTTPException(401, "metodo de login nao é suportado")

    async def local_login(self, data: OAuth2PasswordRequestForm) -> AccessToken:
        user = await self.user_service.get_by_username(username=data.username)
        if user:
            if not verify_password(data.password, user.password):
                raise HTTPException(401, "Wrong password")
        else:
            raise HTTPException(401, "User Not Found")

        return self.get_access_token(user.id)

    async def ldap_login(self, data: OAuth2PasswordRequestForm) -> AccessToken:
        if not data.username and not data.password:
            raise Exception("NUNCA DEVERIA TER CHEGO AQUI")

        username = str(data.username).lower()
        password = str(data.password)

        try:
            ldap_user_data = await ldap_get_user_info(username, password)
            logger.debug(ldap_user_data)
            # LDAPBindError: automatic bind not successful - invalidCredentials
        except LDAPBindError:
            raise HTTPException(401, "Credencias Incorretas")

        except:
            # logger.error("PROBLEMA COLETANDO OS DADOS DO USUARIO")
            raise

        user = await self.user_service.get_by_username(username, from_ad=True)
        if not user:
            # logger.debug("VAI TER QUE CRIAR USUARIO")
            # TODO pegar dados novos do usuário

            full_name = str(ldap_user_data.get("displayName"))
            """ # Validação crítica: Se não tiver nome, é melhor levantar um erro ou usar um fallback.
            if not full_name:
                # Se for realmente necessário, você pode tentar parsear o DN como fallback.
                # Ex: "CN=Bernardo Busin Guimarães,..."
                dn_name_part = ldap_entry["dn"].split(',')[0].replace('CN=', '')
                full_name = dn_name_part if dn_name_part else "Nome Desconhecido" """
            name_parts = full_name.split(maxsplit=1)
            first_name = name_parts[0] if name_parts else ""
            # Se houver mais de uma parte (sobrenome), pega o resto; senão, usa a primeira parte como sobrenome (fallback)
            last_name = name_parts[1] if len(name_parts) > 1 else first_name

            ##TODO
            telefone = None
            email = ldap_user_data.get("mail")

            new_user = User(
                username=username,
                password="stored_on_ad",
                from_ad=True,
                first_name=first_name,
                last_name=last_name,
                telefone=telefone,
                email=email,
            )

            # Handle erro de repetidos
            # TODO
            self.dbSession.add(new_user)

            await self.dbSession.commit()
            await self.dbSession.refresh(new_user)
            # logger.debug("USUÁRIO DO AD CRIADO NO SISTEMA")
            # TODO
            # se o user ja existir, atualizar as informações consumindo o ldap_user_data

        if type(user) is not User:
            raise Exception("USER NAO FOI CRIADO ")
        # logger.debug("ACHOU USUARIO")
        return self.get_access_token(user.id)

    def get_access_token(self, user_id):
        session_payload = {"sub": str(user_id)}
        token = create_access_token(session_payload)
        return AccessToken(access_token=token)
