from django.shortcuts import render, redirect
from photo.forms import PhotoForm
from photo.models import Album, Photo, PhotoLike, PhotoDisLike
__all__ = [
    'photo_new',
    'photo_like',
]


def photo_new(request, album_pk):
    context = {}
    user = request.user
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)

        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            img = form.cleaned_data['img']

            album = Album.objects.get(pk=album_pk)
            album.photo_set.create(
                album=album,
                owner=user,
                title=title,
                description=description,
                img=img,
            )
        return redirect('photo:album_detail', pk=album_pk)
    else:
        form = PhotoForm()
        context['form'] = form
    return render(request, 'photo/photo_edit.html', context)


def photo_like(request, photo_pk):
    user = request.user
    photo = Photo.objects.get(pk=photo_pk)
    if PhotoLike.objects.filter(photo=photo, user=user).exists():
        PhotoLike.objects.get(photo=photo, user=user).delete()
    else:
        PhotoLike.objects.create(photo=photo, user=user)
    return redirect('photo:album_detail', pk=photo.album.id)
