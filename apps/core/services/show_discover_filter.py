from django.conf import settings

from apps.core.ext.tmdb_api_call import outbound_api_call_get

base_url = settings.TMDB_BASE_URL


def _handle_response(response):
    return response


def get_show_discover_filter(*,
                             show_name: str = None,
                             release_year: str = None,
                             popularity: str = None,
                             ):
    url = base_url + "3/discover/tv?query="

    response = outbound_api_call_get(url=url)

    result = _handle_response(response)

    return result
