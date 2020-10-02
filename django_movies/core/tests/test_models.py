import pytest
from core.models import Genre, Movie, Director
from django.db import IntegrityError
from django.urls import reverse

@pytest.fixture
def genre():
    return Genre.objects.create(name="action", age_limit=15)

@pytest.fixture
def api_client():
    return APIClieent

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


@pytest.mark.django_db
def test_genre_creation():
    initial_count = Genre.objects.count()
    Genre.objects.create(name='action')
    count = Genre.objects.count()
    assert initial_count + 1 == count


@pytest.mark.django_db
def test_movie(director, genre):
    print(director, '/n', genre)


@pytest.mark.django_db
def test_movie_creation(director, genre):
    initial_count = Movie.objects.all().count()
    movie = Movie(
        title='Indiana Jones',
        genre=genre,
        director=director,
        released='1994-11-04',
    )
    movie.save()
    assert Movie.objects.all().count() == 1


@pytest.mark.django_db
def test_director_create_fields():
    with pytest.raises(IntegrityError):
        Director.objects.create()

@pytest.mark.django_db
def test_movie_list(api_client, movies):
    url = reverse('core:movie_list')
    response = api_client.get(url, follow=True, format='json')
    assert response.status_code == 200
    data = response.context_data
    objects = data['object_list']
    object_titles = [obj.title for obj in objects]
    for movie in movies:
        assert movie.title in object_titles