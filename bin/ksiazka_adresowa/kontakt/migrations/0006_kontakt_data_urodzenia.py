# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-17 14:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kontakt', '0005_auto_20151217_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='kontakt',
            name='data_urodzenia',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
    ]
