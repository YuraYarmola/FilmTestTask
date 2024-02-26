# films/urls.py
from django.urls import path
from .views import FilmListView, FilmDetailView, ActorListView, FilmCreateView

urlpatterns = [
    path('films/', FilmListView.as_view(), name='film_list'),
    path('films/<int:pk>/', FilmDetailView.as_view(), name='film_detail'),
    path('actors/', ActorListView.as_view(), name='actor_list'),
    path('films/create/', FilmCreateView.as_view(), name='film_create'),
]
