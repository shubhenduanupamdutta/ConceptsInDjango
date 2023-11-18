# from django.shortcuts import render
from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView
from .models import Movie
from django.db.models import Q
# from django.core.paginator import Paginator
# Create your views here.


class MovieListView(ListView):
    model = Movie
    template_name = 'newapp/movie_list.html'
    context_object_name = 'movies'
    paginate_by = 3

    def get_queryset(self) -> QuerySet[Any]:
        search_param = self.request.GET.get('movie_name', "")
        queryset = Movie.objects.filter(Q(name__icontains=search_param))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Add the search parameter to the context for use in the template
        context['search_param'] = self.request.GET.get('movie_name', '')

        return context
