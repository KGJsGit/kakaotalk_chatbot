# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 09:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_shuttle_week'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shuttle',
            old_name='Time',
            new_name='Time_End',
        ),
    ]
