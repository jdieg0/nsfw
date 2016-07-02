# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-01 21:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nsfw', '0006_auto_20160701_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='report',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nsfw.Report'),
        ),
        migrations.AlterField(
            model_name='alert',
            name='station',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nsfw.Station'),
        ),
    ]