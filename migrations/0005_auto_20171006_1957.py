# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 19:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20171006_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyword',
            name='expression',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
