# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-11 13:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luftdaten', '0004_sensorvalue_device'),
    ]

    operations = [
        migrations.CreateModel(
            name='SensorValueAggregated',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device', models.CharField(db_index=True, max_length=100)),
                ('SDS_P1', models.FloatField(null=True)),
                ('SDS_P2', models.FloatField(null=True)),
                ('temperature', models.FloatField(null=True)),
                ('humidity', models.FloatField(null=True)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]