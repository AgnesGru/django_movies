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
from django.urls import path, include
from .views import IndexView

from core.views import hello, MovieCreateView, MovieUpdateView, MovieDeleteView # IndexView # to są widoki
from core.models import Movie, Genre # to jest klasa z models

admin.register(Movie)  # to nie musie tu być bo to powino działać w pliku admin.py
admin.register(Genre)  # to nie musie tu być bo to powino działać w pliku admin.py

urlpatterns = [
    path('hello/', hello),  # ten 'hello/' to jest endpoint a hello widok
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name = 'index'),
    path('', IndexView.as_view(), name = 'index'),
    path('core/', include('core.urls', namespace = 'core')),
    path('accounts/', include('accounts.urls', namespace = 'accounts')),


]
