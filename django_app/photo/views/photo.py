from django.shortcuts import render, redirect, get_object_or_404
from photo.forms import PhotoForm, PhotoMultiForm
from photo.models import Album, Photo, PhotoLike, PhotoDisLike
__all__ = [
    'photo_new',
    'photo_multi_new',
    'photo_like_dislike',
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


def photo_multi_new(request, album_pk):
    album = get_object_or_404(Album, pk=album_pk)
    if request.method == 'POST':
        form = PhotoMultiForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            imgs = request.FILES.getlist('img')
            for index, img in enumerate(imgs):
                Photo.objects.create(
                    album=album,
                    owner=request.user,
                    title='{title}({index})'.format(title=title, index=index),
                    description='{description}({index})'.format(description=description, index=index),
                    img=img,
                )
            return redirect('photo:album_detail', pk=album_pk)
    else:
        form = PhotoMultiForm()
    return render(request, 'photo/photo_multi_new.html', {'form': form})


def photo_like_dislike(request, photo_pk, user_like='like'):

    photo = Photo.objects.get(pk=photo_pk)
    choice_photo = PhotoLike if user_like == 'like' else PhotoDisLike
    opposite_photo = PhotoDisLike if user_like == 'like' else PhotoLike

    like_exist = choice_photo.objects.filter(user=request.user, photo=photo)
    if like_exist.exists():
        like_exist.delete()
    else:
        choice_photo.objects.create(user=request.user, photo=photo)
        opposite_photo.objects.filter(user=request.user, photo=photo).delete()

    return redirect('photo:album_detail', pk=photo.album.pk)
