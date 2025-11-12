import asyncio
from functools import partial

from ldap3 import ALL, Connection, Server

from core.config import (
    LDAP_BASE_DN,
    LDAP_BIND_PASSWORD,
    LDAP_BIND_USER,
    LDAP_SERVER,
    LDAP_USE_SSL,
)


def _sync_lookup_user(username: str):
    """Busca o DN completo do usuário usando a conta de serviço."""
    server = Server(LDAP_SERVER, get_info=ALL, use_ssl=LDAP_USE_SSL)  # pyright: ignore[reportArgumentType]
    conn = Connection(
        server,
        user=LDAP_BIND_USER,
        password=LDAP_BIND_PASSWORD,
        authentication="SIMPLE",
        auto_bind=True,
    )

    search_filter = f"(sAMAccountName={username})"
    conn.search(
        search_base=LDAP_BASE_DN,  # pyright: ignore[reportArgumentType]
        search_filter=search_filter,
        attributes=["distinguishedName", "displayName", "mail", "memberOf"],
    )
    if not conn.entries:
        conn.unbind()
        return None
    entry = conn.entries[0]
    result = {
        "dn": entry.distinguishedName.value,
        "displayName": entry.displayName.value if "displayName" in entry else None,
        "mail": entry.mail.value if "mail" in entry else None,
        "memberOf": entry.memberOf.values if "memberOf" in entry else [],
    }
    conn.unbind()
    return result


def _sync_bind_user(user_dn: str, password: str):
    """Tenta autenticar o usuário diretamente no AD via bind NTLM."""
    server = Server(LDAP_SERVER, get_info=ALL, use_ssl=LDAP_USE_SSL)  # pyright: ignore[reportArgumentType]
    conn = Connection(
        server,
        user=user_dn,
        password=password,
        authentication="SIMPLE",
        auto_bind=True,
    )
    conn.unbind()
    return True


async def find_user(username: str):
    loop = asyncio.get_running_loop()
    func = partial(_sync_lookup_user, username)
    return await loop.run_in_executor(None, func)


async def bind_user(user_dn: str, password: str):
    loop = asyncio.get_running_loop()
    func = partial(_sync_bind_user, user_dn, password)
    return await loop.run_in_executor(None, func)


async def authenticate_user(username: str, password: str):
    """Fluxo completo: busca DN com conta de serviço e tenta bind com credenciais do usuário."""
    user_info = await find_user(username)
    if not user_info:
        print("Usuário não encontrado no AD.")
        return None
    try:
        await bind_user(user_info["dn"], password)
        print("Autenticação bem-sucedida!")
        return user_info
    except Exception as e:
        print("Falha na autenticação:", e)
        return None
