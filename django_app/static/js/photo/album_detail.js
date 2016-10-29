/**
 * Created by pando on 10/28/16.
 */
function photolike(photoPk, likeType) {
  $.ajax({

    method: 'POST',
    url: '/photo/ajax/photo/' + photoPk +'/' + likeType + '/',
  })
    .done(function(response, textStatus) {
        var likeCount =response.like_count;
        var dislikeCount = response.dislike_count;
        var userLike = response.user_like;
        var userDislike = response.user_dislike;

        var spanLikeCount = $('#photo-' + photoPk +'-like-count');
        spanLikeCount.text(likeCount);
        var spanDisLikeCount = $('#photo-' + photoPk +'-dislike-count');
        spanDisLikeCount.text(dislikeCount);

        var btnLike = $('#btn-photo-' + photoPk + '-like');
        var btnDislike = $('#btn-photo-' + photoPk + '-dislike');
        if(userLike) {
            btnLike.addClass('label-info');
            btnLike.removeClass('label-default');
        } else {
            btnLike.removeClass('label-info');
            btnLike.addClass('label-default');
        }
        if(userDislike) {
            btnDislike.addClass('label-danger');
            btnDislike.removeClass('label-default');
        } else {
            btnDislike.removeClass('label-danger');
            btnDislike.addClass('label-default');
        }

    })
    .fail(function(response) {
        console.log(response);
    });
}