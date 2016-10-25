from django.shortcuts import render, redirect, get_object_or_404
from video.models import Video
from django.contrib import messages


__all__ = ['bookmark_add',
           'bookmark_list',
           'bookmark_detail',
           ]


def bookmark_add(request):
    if request.method == 'POST':
        try:
            path = request.POST.get('path')
            Video.objects.create(
                kind=request.POST['kind'],
                youtube_id=request.POST['videoid'],
                title=request.POST['title'],
                description=request.POST['description'],
                published_date=request.POST['published_date'],
                thumbnail=request.POST['thumbnails']
            )
            msg = 'bookmark success'
        except Exception as e:
            msg = 'Exceptions! %s (%s)' % (e, e.args)
        messages.success(request, msg)
        if path:
            return redirect(path)
        else:
            return redirect('video:bookmark_list')


def bookmark_list(request):
    videos = Video.objects.all()
    return render(request, 'video/bookmark_list.html', {'videos': videos})


def bookmark_detail(request, pk):
    video = get_object_or_404(Video, pk=pk)
    return render(request, 'video/bookmark_detail.html', {'video': video})