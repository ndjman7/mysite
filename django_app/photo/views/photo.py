from django.shortcuts import render
__all__ = [
    'photo_new',
]


def photo_new(request):
    return render(request, 'photo/photo_edit.html', {})
