from django.conf import settings

from apps.core.ext.tmdb_api_call import outbound_api_call_get
from apps.core.models import ShowDetail, Reviews

base_url = settings.TMDB_BASE_URL


def _handle_detail_response(item):
    result = ShowDetail(**{
            "show_id": item.get("id"),
            "name": item.get("original_name"),
            "description": item.get("overview"),
            "release_year": item.get("first_air_date").split('-')[0],
            "poster": settings.TMDB_BASE_IMG_URL + str(item.get("poster_path")),
            "popularity": item.get("popularity"),
            "gender": ', '.join([i.get('name') for i in item.get("genres")]),
            "release_date_first_epi": item.get("first_air_date"),
            "total_epi": item.get("number_of_episodes")
        })
    return result


def get_show_detail(pk: int):
    url = base_url + f"3/tv/{pk}"

    response = outbound_api_call_get(url=url)
    result = _handle_detail_response(response)
    return result


def _handle_review_response(response):

    result = [Reviews(name=item.get("author"),
                      description=item.get("content"),
                      rating=item.get("author_details").get("rating"),
                      avatar_path=settings.TMDB_BASE_IMG_URL + str(item.get("author_details").get("avatar_path")))
              for item in response.get("results")]

    return result


def get_show_reviews(pk: int):
    url = base_url + f"3/tv/{pk}/reviews"

    response = outbound_api_call_get(url=url)

    result = _handle_review_response(response)

    return result
