# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-02 00:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_shuttle_validdatetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shuttle',
            name='validDateTime',
            field=models.DateField(),
        ),
    ]
