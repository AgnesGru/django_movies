from django.contrib import admin
from core.models import Movie, Genre, Director

# Register your models here.

admin.site.register(Movie) #  rejestruje moj model zawsze
admin.site.register(Genre)
admin.site.register(Director)