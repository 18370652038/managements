# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-12-20 03:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xproject', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='normaluser',
            name='AlarmMOB',
            field=models.IntegerField(max_length=11, null=True, verbose_name='AlarmMOB'),
        ),
        migrations.AlterField(
            model_name='normaluser',
            name='AlarmMail',
            field=models.EmailField(max_length=50, null=True, verbose_name='AlarmMail'),
        ),
    ]
