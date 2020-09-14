from django.urls import path

from core.views import hello, MovieCreateView, MovieUpdateView, MovieDeleteView, MovieDetailView, MovieListView # to są widoki


app_name = 'core'
urlpatterns = [

    path('hello/', hello),  # ten 'hello/' to jest endpoint a hello widok
    # path('movies/', movies, name='index'),
    path('movie/create', MovieCreateView.as_view(), name = 'movie_create'),
    path('movie/update/<pk>', MovieUpdateView.as_view(), name='movie_update'),
    path('movie/delete/<pk>', MovieDeleteView.as_view(), name='movie_delete'),
    path('movie/detail/<pk>', MovieDetailView.as_view(), name='movie_detail'),
    path('movie/list', MovieListView.as_view(), name='movie_list'),
    ]
