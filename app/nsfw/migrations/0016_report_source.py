# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-02 17:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nsfw', '0015_auto_20161123_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='source',
            field=models.CharField(default='uba', max_length=3),
            preserve_default=False,
        ),
    ]
