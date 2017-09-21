# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-21 05:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='views',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]