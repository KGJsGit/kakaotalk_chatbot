# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-14 20:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_shuttle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shuttle',
            name='dateTime',
        ),
        migrations.AddField(
            model_name='shuttle',
            name='Time',
            field=models.TimeField(default=None),
        ),
    ]
