# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-08 02:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20171007_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='messageList',
            field=models.TextField(default=[]),
            preserve_default=False,
        ),
    ]