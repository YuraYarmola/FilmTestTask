
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DeleteView

from directors.models import Director
from .models import Actor
from .forms import ActorForm


class ActorListView(ListView):
    # pass
    model = Actor
    template_name = 'films/actor_list.html'
    context_object_name = 'actors'
    paginate_by = 2  # Adjust as needed

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