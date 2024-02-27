from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Film, Actor
from django.urls import reverse_lazy
from .forms import *


class FilmListView(ListView):
    model = Film
    template_name = 'films/film_list.html'
    context_object_name = 'films'
    paginate_by = 25

    def get_queryset(self):
        return Film.objects.all().order_by('-release_date')


class FilmDetailView(DetailView):
    model = Film
    template_name = 'films/film_detail.html'
    context_object_name = 'film'



class FilmCreateView(CreateView):
    model = Film
    template_name = 'films/film_form.html'
    fields = ['title', 'description', 'release_date', 'language', 'country', 'plot', 'rating', 'actors', 'director', 'poster']
    success_url = reverse_lazy('film_list')
