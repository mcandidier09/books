# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-06 00:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_user_favorites'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='users/cover/'),
        ),
    ]