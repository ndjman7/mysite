from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from photo.models import Album
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

    album = Album.objects.get(pk=pk)
    photo_list = album.photo_set.all()
    #template_file = 'photo/album_detail.html'

    paginator = Paginator(photo_list, 3)
    page = request.GET.get('page')
    try:
        photos = paginator.page(page)
    except PageNotAnInteger:
        photos = paginator.page(1)
    except EmptyPage:
        photos = paginator.num_pages
    context = {'album': album,
               'photos': photos}
    template_file = 'photo/ajax_album_detail.html'

    return render(request, template_file, context)

