# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-12-19 08:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xproject', '0002_auto_20181219_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='ss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pasz', models.CharField(max_length=10, validators=['s', 's'])),
            ],
        ),
    ]