from django.shortcuts import render
from .models import Movie
from django.utils import timezone


def hello(request):
    # return HttpResponse('Hello World')
    return render(request, template_name = 'hello.html', context = {'adjectives':['beautiful', 'cruel', 'wonderful']},)


def movies(request):
    # movies = Movie.objects.filter(released__lte=timezone.now()).order_by('released')
    return render(request, template_name ='list_of_movies.html', context={'movies': Movie.objects.all()},)