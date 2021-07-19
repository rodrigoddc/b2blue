from operator import itemgetter
from typing import List

from django.conf import settings

from apps.core.ext.tmdb_api_call import outbound_api_call_get
from apps.core.models import Show

api_key_url = settings.TMDB_API_KEY
base_url = settings.TMDB_BASE_URL


def _sort_by_popularity(resp: List[dict]) -> List[dict]:

    result = sorted(resp, key=itemgetter('popularity'), reverse=True)

    return result


def _handle_response_top_100(resp: List[dict]) -> List[dict]:
    unordered_list = []
    for i in resp:
        for j in i.get("results"):
            unordered_list.append(j)
    ordered = _sort_by_popularity(unordered_list)
    return ordered


def _format_dict_list(data: List[dict]) -> List[Show]:
    formatted_dict = [
        Show(**{"show_id": item.get("id"),
                "name": item.get("original_name"),
                "description": item.get("overview"),
                "release_year": item.get("first_air_date").split('-')[0],
                "poster": settings.TMDB_BASE_IMG_URL + str(item.get("poster_path")),
                "votes": item.get("vote_count"),
                "popularity": item.get("popularity")}) for item in data]

    return formatted_dict


def get_show_list():
    url = base_url + f"3/tv/popular?api_key={api_key_url}&page="

    response = []
    # TODO: change to use aiohttp with async!!!
    for i in range(1, 6):
        response.append(outbound_api_call_get(url=url + str(i)))

    unformatted_result = _handle_response_top_100(response)

    result = _format_dict_list(unformatted_result)

    return result
