from django.conf import settings

from apps.core.ext.tmdb_api_call import outbound_api_call_post
from apps.core.services.tmdb_api_auth import chain_auth

base_url = settings.TMDB_BASE_URL
api_key_url = settings.TMDB_API_KEY


def set_show_vote(obj_id: int, username: str, password: str, rating):
    url = base_url + f"3/tv/{obj_id}/rating?"

    session_id = chain_auth(username=username, password=password)

    headers = {
        "Content-Type": "application/json;charset=utf-8",
    }

    params = {"session_id": session_id}
    payload = {"value": rating}

    outbound_api_call_post(url=url, headers=headers, payload=payload, params=params)
