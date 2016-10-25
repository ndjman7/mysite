from django.shortcuts import render
from photo.models import Album
__all__ = [
    'album_list',
    'album_new',
]


def album_list(request):
    albums = Album.objects.all()
    return render(request, 'photo/album_list.html', {'albums': albums})


def album_new(request):
    return render(request,'photo/album_edit.html', {})
