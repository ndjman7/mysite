from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^album/$', views.album_list, name='album_list'),
    url(r'^album/new/$', views.album_new, name='album_new'),
]