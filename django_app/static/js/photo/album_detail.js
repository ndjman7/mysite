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
        var spanLikeCount = $('#photo-' + photoPk +'-like-count');
        spanLikeCount.text(likeCount);
        var spanDisLikeCount = $('#photo-' + photoPk +'-dislike-count');
        spanDisLikeCount.text(dislikeCount);

    })
    .fail(function(response) {
        console.log(response);
    });
}