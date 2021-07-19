import requests
from django.conf import settings

api_key_url = settings.TMDB_API_KEY


def outbound_api_call_get(*, url, headers: dict = None, params: dict = None) -> dict:

    default_params = {"api_key": api_key_url}
    if params is not None:
        default_params.update(**params)

    response = requests.get(url=url, headers=headers, params=default_params)

    if not response.ok:
        response.raise_for_status()

    return response.json()


def outbound_api_call_post(*, url, headers: dict = None, params: dict = None, payload: dict = None) -> dict:

    default_params = {"api_key": api_key_url}
    if params is not None:
        default_params.update(**params)

    response = requests.post(url=url, headers=headers, params=default_params, json=payload)

    if not response.ok:
        response.raise_for_status()

    return response.json()
