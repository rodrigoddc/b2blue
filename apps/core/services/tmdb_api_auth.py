from django.conf import settings

from apps.core.ext.tmdb_api_call import outbound_api_call_get

base_url = settings.TMDB_BASE_URL


def get_request_token() -> str:
    url = base_url + "3/authentication/token/new"
    response = outbound_api_call_get(url=url)

    return response.get("request_token")


def autenticate_request_token_with_user(*, username: str, pwd: str, token: str):
    url = base_url + "3/authentication/token/validate_with_login"
    headers = {
        "Content-Type": "application/json;charset=utf-8",
    }
    params = {
        "username": username,
        "password": pwd,
        "request_token": token
    }
    outbound_api_call_get(url=url, headers=headers, params=params)


def create_session(token: str) -> str:
    url = base_url + "3/authentication/session/new"
    headers = {
        "Content-Type": "application/json;charset=utf-8",
    }
    params = {
        "request_token": token
    }

    response = outbound_api_call_get(url=url, headers=headers, params=params)

    return response.get("session_id")


def get_user_account_id(se_id: str):
    url = base_url + "3/account?"
    params = {"session_id": se_id}
    response = outbound_api_call_get(url=url, params=params)

    return response.get("id")


def chain_auth(*, username: str, password: str):
    token = get_request_token()
    autenticate_request_token_with_user(token=token,
                                        username=username,
                                        pwd=password)
    session_id = create_session(token=token)
    return session_id
