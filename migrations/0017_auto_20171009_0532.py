# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 05:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20171009_0429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='combine',
            name='keyword',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Keyword'),
        ),
    ]