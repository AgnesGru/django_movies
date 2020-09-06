from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

STATUS_CHOICES = ((1,10), (2,13), (3, 16), (4,18))  # tu może być string gdzie 10, 12

class Genre(models.Model):
    name = models.CharField(max_length=20, unique=True)
    # age_limit = models.IntegerField(
    #     null=True, blank=True, validators=[MaxValueValidator(99), MinValueValidator(1)]
    # )
    age_limit = models.IntegerField(null=True, blank=True,choices=STATUS_CHOICES, default=10)

    def __str__(self):
        return self.name

class Movie(models.Model):  #  to jest podstawowy model models.Model
    genre = models.ForeignKey(Genre, null=True, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    rating = models.IntegerField(null=True, validators=[MaxValueValidator(10), MinValueValidator(1)])
    released = models.DateField(null=True)
    description = models.TextField(null=True, blank=True)   # null = True, czy zazwalasz danemu rekordowi być zerowym, blank odnosie się do formularzy
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):  # metofa reprezentuje w ten sposób nowe filmy
        return f"{self.title} from {self.released}"

