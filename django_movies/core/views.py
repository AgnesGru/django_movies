from django.shortcuts import render
from .models import Movie, AGE_LIMITS
# from django.utils import timezone
from core.models import Movie
from django import views
from django.views.generic import TemplateView

def hello(request):
    # return HttpResponse('Hello World')
    return render(request, template_name = 'hello.html', context = {'adjectives':['beautiful', 'cruel', 'wonderful']},)


def movies(request): # to jest widok!
    # movies = Movie.objects.filter(released__lte=timezone.now()).order_by('released')
    # return render(request, template_name ='movies.html', context={'movies': Movie.objects.filter().order_by('-rating')},)
    return render(request, template_name ='movies.html',
                  context={'movies': Movie.objects.filter().order_by('-rating'), 'age_limit' : AGE_LIMITS})

# class MovieView(views.View):
#     def get(self, request):
#         return render(request,
#                       template_name ='movies.html',
#                       context={'movies': Movie.objects.filter().order_by('-rating'), 'age_limit' : AGE_LIMITS})

class MovieView(TemplateView):
    template_name = 'movies.html'
    extra_context = {'movies': Movie.objects.filter().order_by('-rating'), 'age_limit' : AGE_LIMITS}

