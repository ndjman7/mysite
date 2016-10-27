from django.db import models
from django.conf import settings
from mysite.utils.models import BaseModel


class Album(BaseModel):
    title = models.CharField(max_length=30)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    description = models.CharField(max_length=80, blank=True)

    def __str__(self):
        return self.title


class Photo(BaseModel):
    album = models.ForeignKey(Album)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=80, blank=True)
    img = models.ImageField(upload_to='photo')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, through='PhotoLike', related_name='photo_like_users')
    dislike_user = models.ManyToManyField(settings.AUTH_USER_MODEL, through='PhotoDisLike', related_name='photo_dislike_users')
    img_thumbnail = models.ImageField(upload_to='photo/thumbnail', blank=True)

    def save(self, *args, **kargs):
        image_changed = False

        if self.pk is not None:
            ori = Photo.objects.get(pk=self.pk)
            if ori.img != self.img:
                image_changed = True

        if self.img and not self.img_thumbnail:
            image_changed = True

        super().save(*args, **kargs)
        if image_changed:
            self.make_thumbnail()

    def make_thumbnail(self):
        from PIL import Image, ImageOps
        #파일을 만들기 싫어서 파일 인 척 하는 것
        from io import BytesIO
        from django.core.files.base import ContentFile
        #로컬이아닌다른스테이지를가져올수있도록해주는것
        from django.core.files.storage import default_storage
        import os
        size = (300, 300)
        f = default_storage.open(self.img)
        image = Image.open(f)
        ftype = image.format
        image = ImageOps.fit(image, size, Image.ANTIALIAS) #안티앨리어스는사진의계단현상을없애준다.

        path, ext = os.path.splitext(self.img.name)
        name = os.path.basename(path)

        thumbnail_name = '%s_thumb%s' % (name, ext)

        temp_file = BytesIO()
        image.save(temp_file, ftype)
        temp_file.seek(0)


        content_file = ContentFile(temp_file.read())
        self.img_thumbnail.save(thumbnail_name, content_file)
        temp_file.close()
        content_file.close()
        f.close()

    def __str__(self):
        return self.title


class PhotoLike(BaseModel):
    photo = models.ForeignKey(Photo)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)


class PhotoDisLike(BaseModel):
    photo = models.ForeignKey(Photo)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
