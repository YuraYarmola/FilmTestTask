from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DeleteView, UpdateView

from .models import Director
from .forms import DirectorForm


class DirectorCreateView(ListView):
    template_name = 'films/director_form.html'

    def get(self, request):
        form = DirectorForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = DirectorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('director_list')  # Redirect to a page displaying a list of actors
        return render(request, self.template_name, {'form': form})


class DirectorDeleteView(DeleteView):
    model = Director
    success_url = reverse_lazy('director_list')
    template_name = 'films/director_delete_confirmation.html'


class DirectorListView(ListView):
    # pass
    model = Director
    template_name = 'films/director_list.html'
    context_object_name = 'directors'
    paginate_by = 2  # Adjust as needed

    def get_queryset(self):
        return Director.objects.all()



class DirectorUpdateView(UpdateView):
    model = Director
    template_name = 'films/director_form.html'
    fields = ['name', 'last_name']
    success_url = reverse_lazy('director_list')