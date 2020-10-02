from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from model_utils import Choices

AGE_LIMITS = Choices((0,'kids', "kids"), (1,'teens', 'kids'), (2, 'adults', 'kids'),)

class Genre(models.Model):
    name = models.CharField(max_length=20, unique=True)
    age_limit = models.IntegerField(null=True, blank=True,
                                    choices=AGE_LIMITS,
                                    default = 2)

    def __str__(self):
        return self.name

class Director(models.Model):  #  to jest model reżysera
    name = models.CharField(max_length=100, default = None)
    second_name = models.CharField(max_length=100, default = None)

    def __str__(self):
        return f'{self.second_name} {self.name}'

class Country(models.Model):
    name = models.CharField(max_length=50, null=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}'


class Movie(models.Model):  #  to jest podstawowy model models.Model
    genre = models.ForeignKey(Genre, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    rating = models.IntegerField(null=True, validators=[MaxValueValidator(10), MinValueValidator(1)])
    released = models.DateField(null=True)
    description = models.TextField(null=True, blank=True)   # null = True, czy zazwalasz danemu rekordowi być zerowym, blank odnosie się do formularzy
    created = models.DateTimeField(auto_now_add=True)
    director=models.ForeignKey(Director,null=True,on_delete=models.SET_NULL)
    countries = models.ManyToManyField(Country, null = True, related_name = 'movies')

    class Meta:
        unique_together = ('title', 'released')


    def __str__(self):  # print movies, ont number of objects
        return f"{self.title} from {self.released}"

