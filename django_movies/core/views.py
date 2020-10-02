from django.shortcuts import render
# from django.utils import timezone
from .models import Movie #, AGE_LIMITS
from django import views
from django.contrib.auth.mixins import (LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin)
from django.views.generic import (TemplateView, ListView, FormView,
                                  CreateView, UpdateView, DeleteView, DetailView)
from core.forms import MovieForm
from django.urls import reverse_lazy
import logging


#
# logging.basicConfig(
#     filename='log.txt',
#     filemode = 'w',
#     level = logging.INFO,
# )
LOGGER = logging.getLogger(__name__)

# def movies(request): # to jest widok!
#     # movies = Movie.objects.filter(released__lte=timezone.now()).order_by('released')
#     # return render(request, template_name ='movies.html', context={'movies': Movie.objects.filter().order_by('-rating')},)
#     return render(request, template_name ='movies.html',
#                   context={'movies': Movie.objects.filter().order_by('-rating'), 'age_limit' : AGE_LIMITS})
# CBV
# class MovieView(views.View):
#     def get(self, request):
#         return render(request,
#                       template_name ='movies.html',
#                       context={'movies': Movie.objects.filter().order_by('-rating'), 'age_limit' : AGE_LIMITS})

# class MovieView(TemplateView):
#     template_name = 'movies.html'
#     extra_context = {'movies': Movie.objects.filter().order_by('-rating'), 'age_limit' : AGE_LIMITS}

# class MovieView(ListView):  # jeszcze upraszczamy
#     template_name = 'movies.html'
#     model = Movie
#
# nadpisywanie

# class MovieCreateView(FormView):  # formularz jest tylko do update i create
#     template_name = 'form.html'
#     form_class = MovieForm


class MovieCreateView(CreateView, LoginRequiredMixin, PermissionRequiredMixin):
    # model = Movie
    title = "Add Movie"
    template_name = 'form.html'
    form_class = MovieForm
    success_url = reverse_lazy('core:movie_list') #success_url  przekieruje użytkownika po poprawnym zatwierdzeniu formularza na inną stronę.

    def form_invalid(self, form):
        LOGGER.warning('Invalid data provided.')
        return super().form_invalid(form)

def hello(request):
    LOGGER.warning("\n\nCos smiesznego")
    return render(request, template_name = 'hello.html',
                  context = {'adjectives':['beautiful', 'cruel', 'wonderful']},)
#
# przekazywanie kontextu w ListView
# class MovieView(ListView):  # to jest do updetowania obiektów
#     template_name = 'movies.html'
#     model = Movie
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs )
#         context['age_limit'] = AGE_LIMITS
#         return context

class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class MovieUpdateView(UpdateView, LoginRequiredMixin,
                      PermissionRequiredMixin, StaffRequiredMixin):
    template_name = 'form.html'
    model = Movie
    form_class = MovieForm
    success_url= reverse_lazy('core:movie_list')

    def form_invalid(self,form):
        LOGGER.warning('Invalid data provided.')
        return super().form_invalid(form)

    # def post(self, request, * args, **kwargs):
    #     result = super().post(request, *args, **kwargs)
    #     print(request)
    #     LOGGER.info(f"Successfully added new movie: {self.request.POST.get('title')}")
    #     return

class MovieDeleteView(DeleteView, LoginRequiredMixin,
                      PermissionRequiredMixin, StaffRequiredMixin):
    template_name = 'movie_confirm_delete.html'
    model=Movie
    # form_class = MovieForm
    success_url= reverse_lazy('core:movie_list') # ??

    def test_func(self):
        return super().test_func() and self.request.user.is_superuser

#  to jest praca domowa jak umożliwić userowi sortowanie czyli sortowanie po director
class MovieListView(ListView):
    template_name = "movie_list.html"
    model = Movie

class MovieDetailView(DetailView):
    template_name = "movie_detail.html"
    model = Movie


