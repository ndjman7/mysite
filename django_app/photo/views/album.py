from django.shortcuts import render
from photo.models import Album
__all__ = [
    'album_list',
]


def album_list(request):
    albums = Album.objects.all()
    return render(request, 'photo/album_list.html', {'albums': albums})