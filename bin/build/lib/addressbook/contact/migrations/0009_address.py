# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-07 13:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0008_auto_20160707_1301'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=50, verbose_name='Street')),
                ('city', models.CharField(max_length=50, verbose_name='City')),
                ('zip_code', models.CharField(max_length=10, verbose_name='Zip Code')),
                ('country', models.CharField(max_length=40, verbose_name='Country')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.Contact', verbose_name='Address')),
            ],
        ),
    ]