from django.shortcuts import render
from .models import Movie
from django.utils import timezone


def hello(request):
    # return HttpResponse('Hello World')
    return render(request, template_name = 'hello.html', context = {'adjectives':['beautiful', 'cruel', 'wonderful']},)


def movies(request): # to jest widok!
    # movies = Movie.objects.filter(released__lte=timezone.now()).order_by('released')
    return render(request, template_name ='movies.html', context={'movies': Movie.objects.filter().order_by('-rating')},)