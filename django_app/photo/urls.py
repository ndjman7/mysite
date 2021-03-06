from django.conf.urls import url
from . import views
from photo.ajax.photo import photo_like



urlpatterns = [
    url(r'^album/$', views.album_list, name='album_list'),
    url(r'^album/new/$', views.album_new, name='album_new'),
    url(r'^album/(?P<pk>[0-9]+)/$', views.album_detail, name='album_detail'),

    #url(r'^album/(?P<album_pk>[0-9]+)/new/$', views.photo_new, name='photo_new'),
    url(r'^album/(?P<album_pk>[0-9]+)/multi_new/$', views.photo_multi_new, name='photo_multi_new'),
    url(r'^photo/(?P<photo_pk>[0-9]+)/(?P<user_like>\w+)', views.photo_like_dislike, name='photo_like_dislike'),

    url(r'^ajax/photo/(?P<photo_pk>[0-9]+)/(?P<like_type>\w+)', photo_like, name='ajax_photo_like'),
]
