# filters.py
import django_filters
from .models import Film

class FilmFilter(django_filters.FilterSet):
    class Meta:
        model = Film
        fields = {
            'release_date': ['exact', 'year__gt', 'year__lt'],
            'actors': ['exact'],
            'director': ['exact'],
        }
