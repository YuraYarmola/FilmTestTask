from django.forms import ModelForm

from films.models import Film


class FilmCreateForm(ModelForm):
    class Meta:
        model = Film
        fields = "__all__"
