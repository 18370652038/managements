# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-12-11 05:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='subclass_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=30, unique=True, verbose_name='Serial number')),
                ('name', models.CharField(max_length=120, verbose_name='name')),
                ('Devicename', models.CharField(max_length=30, verbose_name='Device name')),
                ('Areaname', models.CharField(max_length=120, verbose_name='Area name')),
                ('Devicenumber', models.IntegerField(max_length=10, verbose_name='Device number')),
                ('State', models.CharField(choices=[('TP', 'to poy '), ('TBP', 'To be paid'), ('R', 'Refund')], default='TBP', max_length=10, verbose_name='State')),
                ('Type', models.CharField(choices=[('BANK', 'bank'), ('Alipay', 'alipay'), ('WeChat', 'wechat')], default='BANK', max_length=10, verbose_name='Transaction type')),
                ('Money', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Amount of money')),
                ('Duration', models.IntegerField(max_length=10, verbose_name='Transaction duration')),
                ('paymenttime', models.TimeField(auto_now_add=True, verbose_name='Payment time')),
                ('endtime', models.TimeField(auto_now=True, verbose_name='Payment time')),
                ('POnumber', models.IntegerField(max_length=20, verbose_name='Payment order number')),
                ('Remarks', models.TextField(blank=True, max_length=100, null=True, verbose_name='Remarks')),
            ],
            options={
                'verbose_name': 'subclass details',
                'verbose_name_plural': 'subclass details',
            },
        ),
    ]
