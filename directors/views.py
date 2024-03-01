from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination

from .models import Director
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Director
from .serializers import DirectorSerializer

from .forms import DirectorForm


class DirectorCreateView(CreateView):
    model = Director
    template_name = 'films/director_form.html'
    fields = ['name', 'last_name']
    success_url = reverse_lazy('director_list')


class DirectorDeleteView(DeleteView):
    model = Director
    success_url = reverse_lazy('director_list')
    template_name = 'films/director_delete_confirmation.html'


class DirectorListView(ListView):
    # pass
    model = Director
    template_name = 'films/director_list.html'
    context_object_name = 'directors'
    paginate_by = 25

    def get_queryset(self):
        return Director.objects.all()


class DirectorUpdateView(UpdateView):
    model = Director
    template_name = 'films/director_form.html'
    fields = ['name', 'last_name']
    success_url = reverse_lazy('director_list')


class DirectorListAPIView(generics.ListCreateAPIView, PageNumberPagination):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    permission_classes = [AllowAny]
    pagination_class = LimitOffsetPagination
    page_size = 25
    max_page_size = 50
    page_size_query_param = 'page_size'

class DirectorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    permission_classes = [AllowAny]