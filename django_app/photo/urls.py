from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^album/$', views.album_list, name='album_list'),
    url(r'^album/new/$', views.album_new, name='album_new'),
    url(r'^album/(?P<pk>[0-9]+)/$', views.album_detail, name='album_detail'),
    url(r'^album/(?P<album_pk>[0-9]+)/new/$', views.photo_new, name='photo_new'),
    url(r'^photo/(?P<photo_pk>[0-9]+)/like/$', views.photo_like, name='photo_like'),
    url(r'^photo/(?P<photo_pk>[0-9]+)/dislike/$', views.photo_dislike, name='photo_dislike'),
]
