# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-01-18 08:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xproject', '0005_auto_20181221_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='normaluser',
            name='OrganizationID',
            field=models.IntegerField(max_length=50, null=True, verbose_name='OrganizationID'),
        ),
    ]