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


class FilmDetailView(DetailView):
    model = Film
    template_name = 'films/film_list.html'
    context_object_name = 'film'


class ActorListView(ListView):
    model = Actor
    template_name = 'films/actor_list.html'
    context_object_name = 'actors'


class FilmCreateView(CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': FilmCreateForm()}
        return render(request, 'films/film_form.html', context)

    def post(self, request, *args, **kwargs):
        form = FilmCreateForm(request.POST)
        if form.is_valid():
            print("ok")
            film = form.save()
            film.save()
            return HttpResponseRedirect(reverse_lazy('film_detail', args=[film.id]))

        return render(request, 'films/film_form.html', {'form': form})
