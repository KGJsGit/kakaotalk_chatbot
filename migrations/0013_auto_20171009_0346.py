# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 03:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20171009_0331'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mailCheck',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='response',
            name='combineIdList',
            field=models.CharField(default=[0], max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='combineIdList',
            field=models.CharField(default='[0]', max_length=50, null=True),
        ),
    ]
