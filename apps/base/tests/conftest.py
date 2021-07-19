import pytest
from django.urls import reverse


@pytest.fixture(scope="function", autouse=True)
def response(client, db):
    response = client.get(reverse('base:home'))
    return response
