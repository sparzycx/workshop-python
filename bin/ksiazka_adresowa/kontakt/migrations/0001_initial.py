# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-17 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kontakt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=30)),
                ('nazwisko', models.CharField(max_length=50)),
                ('telefon', models.IntegerField()),
                ('zdjecie', models.ImageField(upload_to='')),
            ],
        ),
    ]
