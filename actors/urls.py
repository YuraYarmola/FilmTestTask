# films/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('actors/', ActorListView.as_view(), name='actor_list'),
    path('actors/add/', ActorCreateView.as_view(), name='add_actor'),
    path('actors/<int:pk>/delete/', ActorDeleteView.as_view(), name='delete_actor'),
    path('actors/<int:pk>/edit/', ActorUpdateView.as_view(), name='edit_actor'),

    path('api/actors/', ActorListAPIView.as_view(), name='actor_list_api'),
    path('api/actors/<int:pk>/', ActorDetailAPIView.as_view(), name='actor_detail_api'),

]
