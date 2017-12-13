# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-18 02:11
from __future__ import unicode_literals

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20171118_0956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='profile_image',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=imagekit.models.fields.ProcessedImageField(default='avatar/default.png', upload_to='avatar', verbose_name='头像'),
        ),
    ]
