# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 03:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20171009_0316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='combineIdList',
            field=models.TextField(default=None, unique=True),
        ),
    ]
