from django.db import models

from actors.models import Actor
from directors.models import Director


# Create your models here.
class Film(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    language = models.TextField(null=True, blank=True)
    country = models.TextField(null=True, blank=True)
    plot = models.TextField()
    rating = models.FloatField(default=50)

    actors = models.ManyToManyField(Actor, null=True, blank=True)
    director = models.ManyToManyField(Director, null=True, blank=True)

    poster = models.ImageField(upload_to='posters/%m-%d/', null=True, blank=True)

    def __str__(self):
        return self.title