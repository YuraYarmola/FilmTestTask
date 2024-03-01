# films/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('directors/add/', DirectorCreateView.as_view(), name='add_director'),
    path('directors/', DirectorListView.as_view(), name='director_list'),
    path('directors/<int:pk>/delete/',DirectorDeleteView.as_view(), name='delete_director'),
    path('directors/<int:pk>/edit/', DirectorUpdateView.as_view(), name='edit_director'),
    path('api/directors/', DirectorListAPIView.as_view(), name='director_list_api'),
    path('api/directors/<int:pk>/', DirectorDetailAPIView.as_view(), name='director_detail_api'),
]
