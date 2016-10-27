from django.shortcuts import render, redirect
from photo.models import Album , PhotoLike , Photo
from photo.forms import AlbumModelForm
__all__ = [
    'album_list',
    'album_new',
    'album_detail',
]


def album_list(request):
    albums = Album.objects.all()
    return render(request, 'photo/album_list.html', {'albums': albums})


def album_new(request):
    if request.method == 'POST':
        form = AlbumModelForm(request.POST)
        if form.is_valid():
            album = form.save(commit=False)
            album.owner = request.user
            album.save()
            return redirect('photo:album_list')
    else:
        form = AlbumModelForm()
        return render(request, 'photo/album_edit.html', {'form': form})


def album_detail(request, pk):
    context = {}
    album = Album.objects.get(pk=pk)
    context['album'] = album

    return render(request, 'photo/album_detail.html', context)

