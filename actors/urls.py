# films/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('actors/', ActorListView.as_view(), name='actor_list'),
    path('actors/add/', ActorCreateView.as_view(), name='add_actor'),
    path('actors/<int:pk>/delete/', ActorDeleteView.as_view(), name='delete_actor'),

]
