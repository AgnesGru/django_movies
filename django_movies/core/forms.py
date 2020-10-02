from django import forms
import re
from django.db import models
from django.core.exceptions import ValidationError
from core.models import Genre, Movie, Director, Country
from datetime import date
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import FormActions
from crispy_forms.layout import Layout, Submit, Row, Column, Div, Button

def capitalized_vlaidator(value: str):  # funkcja walidacyjna
    if value[0].islower():
        raise ValidationError('Value must be capitalized.')


class PastMonthField(forms.DateField):

    def validate(self, value):
        super().validate(value)
        if value >= date.today():
            raise ValidationError('only past dates allowed here.')

    def clean(self, value):
        result = super().clean(value)
        return date(year=result.year, month=result.month, day=1) # tu zawsze będzie 1 dzien miesiaca

class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = '__all__'  # tu można wpisać w tupili albo liscie nazwy fiildsów, żeby kontrolować z pozycji back-end
        # fields = ('title', 'rating', 'released',)

    title = forms.CharField(max_length=100)
    genre = forms.ModelChoiceField(queryset=Genre.objects.all())
    rating = forms.IntegerField(min_value =1, max_value=10)
    released = PastMonthField()
    description = forms.CharField(widget=forms.Textarea, required=False)
    created = models.DateTimeField(auto_now_add=True)
    director = models.ForeignKey(Director, null=True, on_delete=models.SET_NULL)
    countries = models.ManyToManyField(Country, null=True, related_name='movies')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper() # from crispy_forms.helper
        self.helper.layout = Layout(
            'title',
            Row(Column('genre'), Column('rating'), Column('released')),
            Row(Column('director'), Column('released')),
            'description',
            Div('countries', css_id='black-fields'),
            FormActions(
                Submit('submit', 'Submit'),
                Button('cancel', 'Cancel'),
            ))

    def clean_description(self):
        initial = self.cleaned_data['description']
        sentences = re.sub(r'\s*\.s*', '.', initial).split('.')
        cleaned='.'.join(sentence.capitalize() for sentence in sentences)
        return cleaned

    def clean(self):
        result = super().clean()
        if result['genre'].name == 'comedy' and result['rating'] >5:
            raise ValidationError('The best comedy is worth a 4.')
        return result