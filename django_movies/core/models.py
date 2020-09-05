from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Movie(models.Model):  #  to jest podstawowy model models.Model
    title = models.CharField(max_length=100)
    rating = models.IntegerField(null=True, validators=[MaxValueValidator(10), MinValueValidator(1)])
    released = models.DateField(null=True)
    description = models.TextField(null=True, blank=True)   # null = True, czy zazwalasz danemu rekordowi być zerowym, blank odnosie się do formularzy
    created = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50, null=True)

    def __str__(self):  # metofa reprezentuje w ten sposób nowe filmy
        return f"{self.title} from {self.released}"

