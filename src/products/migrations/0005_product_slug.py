# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-03-31 06:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210330_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='uncategorized'),
        ),
    ]
