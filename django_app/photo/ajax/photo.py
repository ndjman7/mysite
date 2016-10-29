import json
from django.shortcuts import get_object_or_404, redirect, HttpResponse
from photo.models import PhotoDisLike, PhotoLike, Photo
from django.views.decorators.csrf import csrf_exempt

__all__ = [
    'photo_like',
]

@csrf_exempt
def photo_like(request, photo_pk, like_type='like'):
    """
    1. 요청한 유저가 이 사진에 좋아요(또는 싫어요)를 눌렀는가?
    2. 이미 좋아요를 눌렀는데 다시 좋아요를 누른 경우
    3. 이미 좋아요를 눌렀는데 싫어요를 누른 경우
    """
    photo = get_object_or_404(Photo, pk=photo_pk)
    album = photo.album
    next_path = request.GET.get('next')
    like_model = PhotoLike if like_type == 'like' else PhotoDisLike
    opposite_model = PhotoDisLike if like_type == 'like' else PhotoLike

    user_like_exist = like_model.objects.filter(
        user=request.user,
        photo=photo
    )

    is_delete = False
    # 요청한 유저가 이미 좋아요(또는 싫어요)를 했는가?
    if user_like_exist.exists():
        user_like_exist.delete()
        is_delete = True
    # 이미 누르지 않은 경우, 좋아요 처리를 해준다
    else:
        like_model.objects.create(
            user=request.user,
            photo=photo
        )
        # 근데 이사람이 싫어요(또는 반대모델)를 눌러놨을 경우
        # 해당하는 경우를 지워준다`
        opposite_model.objects.filter(
            user=request.user,
            photo=photo
        ).delete()

    ret = {
        'like_count': photo.like_users.count(),
        'dislike_count': photo.dislike_user.count(),
        'user_like': False,
        'user_dislike': False,
    }
    if not is_delete:
        ret['user_like'] = True if like_type == 'like' else False
        ret['user_dislike'] = True if like_type != 'like' else False


    #content_type 어떤 리퀘스트에 대해서 온 요청에 대해 타입을 정할 수 있다.
    return HttpResponse(json.dumps(ret), content_type='application/json')
