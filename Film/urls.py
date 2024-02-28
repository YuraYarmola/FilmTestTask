from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path, include

from Film import settings
from django.views.static import serve
from django.views.static import serve

# from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('films.urls')),
    path('', include('actors.urls')),
    path('', include('directors.urls')),

] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
