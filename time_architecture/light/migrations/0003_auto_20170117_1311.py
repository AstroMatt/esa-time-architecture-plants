# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-17 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('light', '0002_auto_20170117_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='led',
            name='name',
            field=models.CharField(choices=[('UVA1', 'UVA1 395nm'), ('UVA2', 'UVA2 415nm'), ('UVA3', 'UVA3 495nm'), ('IR', 'IR 740nm'), ('Red', 'Red')], db_index=True, max_length=50, verbose_name='Name'),
        ),
    ]
