# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 08:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_auto_20161025_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='img_thumbnail',
            field=models.ImageField(blank=True, upload_to='photo/thumbnail'),
        ),
    ]
