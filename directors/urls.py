# films/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('directors/add/', DirectorCreateView.as_view(), name='add_director'),
    path('directors/', DirectorListView.as_view(), name='director_list'),
    path('directors/delete/<int:pk>',DirectorDeleteView.as_view(), name='delete_director')

]
