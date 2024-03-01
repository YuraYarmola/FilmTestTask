from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path, include, re_path

from Film import settings
from django.views.static import serve
from django.views.static import serve
print("123", settings.MEDIA_ROOT)
# from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('films.urls')),
    path('', include('actors.urls')),
    path('', include('directors.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),


] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
