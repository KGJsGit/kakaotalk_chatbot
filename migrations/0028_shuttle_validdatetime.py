# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-01 23:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_auto_20171016_0925'),
    ]

    operations = [
        migrations.AddField(
            model_name='shuttle',
            name='validDateTime',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 14, 23, 11, 11, 244394)),
            preserve_default=False,
        ),
    ]
