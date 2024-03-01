from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DeleteView, UpdateView
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.permissions import AllowAny
from .models import Actor
from .forms import ActorForm
from .serializers import ActorSerializer


class ActorListView(ListView):
    # pass
    model = Actor
    template_name = 'films/actor_list.html'
    context_object_name = 'actors'
    paginate_by = 25  # Adjust as needed

    def get_queryset(self):
        return Actor.objects.all()


class ActorDeleteView(DeleteView):
    model = Actor
    success_url = reverse_lazy('actor_list')
    template_name = 'films/actor_confirm_delete.html'


class ActorCreateView(View):
    template_name = 'films/actor_form.html'

    def get(self, request):
        form = ActorForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ActorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('actor_list')  # Redirect to a page displaying a list of actors
        return render(request, self.template_name, {'form': form})


class ActorUpdateView(UpdateView):
    model = Actor
    template_name = 'films/actor_form.html'
    fields = ['name', 'last_name']
    success_url = reverse_lazy('actor_list')


class ActorListAPIView(generics.ListCreateAPIView, PageNumberPagination):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = [AllowAny]
    pagination_class = LimitOffsetPagination
    page_size = 25
    max_page_size = 50
    page_size_query_param = 'page_size'


class ActorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = [AllowAny]
