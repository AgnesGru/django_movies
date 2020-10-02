import pytest
from rest_framework.test import APIClient
from core.models import Director, Genre, Movie

@pytest.fixture
def director():
    return Director.objects.create(name="Mateusz", second_name="Gorski")
# definiujemy fixture który bedziemy korzystać w testach


@pytest.fixture
def genre():
    return Genre.objects.create(name="action", age_limit=15)

@pytest.fixture
def api_client():
    return APIClieent

@pytest.fixture
def movies(director, genre):
    return Movie.objects.bulk_create(
        Movie(
            director=director,
            genre=genre,
            title="Title1",
            releaded='2020-08-20',
        ),
        Movie(
            director=director,
            genre=genre,
            title="Title1",
            releaded='2020-08-20',
        ),
        Movie(
            director=director,
            genre=genre,
            title="Title1",
            releaded='2020-08-20',
        ),
    )
