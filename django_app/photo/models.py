from django.db import models
from django.conf import settings
"""
Album

Photo
"""


class Album(models.Model):
    title = models.CharField(max_length=30)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    description = models.CharField(max_length=80, blank=True)

    def __str__(self):
        return self.title


class Photo(models.Model):
    album = models.ForeignKey(Album)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=80, blank=True)
    img = models.ImageField(upload_to='photo')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, through='PhotoLike', related_name='photo_like_users')
    dislike_user = models.ManyToManyField(settings.AUTH_USER_MODEL, through='PhotoDisLike', related_name='photo_dislike_users')

    def __str__(self):
        return self.title


class PhotoLike(models.Model):
    photo = models.ForeignKey(Photo)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_date = models.DateTimeField(auto_now_add=True)


class PhotoDisLike(models.Model):
    photo = models.ForeignKey(Photo)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_date= models.DateTimeField(auto_now_add=True)