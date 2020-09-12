"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from core.views import hello, MovieView, MovieCreateView # to są widoki
from core.models import Movie, Genre # to jest klasa z models

admin.register(Movie)  # to nie musie tu być bo to powino działać w pliku admin.py
admin.register(Genre)  # to nie musie tu być bo to powino działać w pliku admin.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),  # ten 'hello/' to jest endpoint a hello widok
    # path('movies/', movies, name='index'),
    path('', MovieView.as_view(), name = 'index'),
    path('movie/create', MovieCreateView.as_view(), name = 'movie_create'),
]
