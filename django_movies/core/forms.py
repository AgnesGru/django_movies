from django import forms

from core.models import Genre, Movie

class MovieForm(forms.Form):
    title = forms.CharField(max_length=100)
    genre = forms.ModelChoiceField(queryset=Genre.objects.all())
    rating = forms.IntegerField(min_value =1, max_value=10)
    released = forms.DateField()
    description = forms.CharField(widget=forms.Textarea, required=False)
    # created = models.DateTimeField(auto_now_add=True)
    # director = models.ForeignKey(Director, null=True, on_delete=models.SET_NULL)
    # countries = models.ManyToManyField(Country, null=True, related_name='movies')