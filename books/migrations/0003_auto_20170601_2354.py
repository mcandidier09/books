# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-01 23:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0002_book_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='interested',
            field=models.ManyToManyField(blank=True, related_name='interested', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL),
        ),
    ]
