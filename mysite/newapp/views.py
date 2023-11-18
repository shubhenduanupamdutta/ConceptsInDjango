# from django.shortcuts import render
from django.views.generic import ListView
from .models import Movie
# from django.core.paginator import Paginator
# Create your views here.


class MovieListView(ListView):
    model = Movie
    template_name = 'newapp/movie_list.html'
    context_object_name = 'movies'
    paginate_by = 3
