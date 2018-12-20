# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-12-20 03:06
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='NormalUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('mob', models.CharField(max_length=30, null=True, verbose_name='mob')),
                ('QQ', models.CharField(max_length=20, null=True, verbose_name='QQ')),
                ('Weixin', models.CharField(max_length=20, null=True, verbose_name='Weixin')),
                ('email', models.EmailField(max_length=50, null=True, verbose_name='email')),
                ('AlarmMOB', models.IntegerField(max_length=11, verbose_name='AlarmMOB')),
                ('AlarmMail', models.EmailField(max_length=50, verbose_name='AlarmMail')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
                'db_table': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='DeviceInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DeviceID', models.CharField(max_length=20, unique=True, verbose_name='DeviceID')),
                ('Eey', models.CharField(max_length=30, verbose_name='Eey')),
                ('eKey', models.CharField(max_length=30, verbose_name='eKey')),
                ('ADDR', models.CharField(max_length=30, verbose_name='ADDR')),
                ('MACaddress', models.CharField(max_length=30, null=True, verbose_name='MACaddress')),
                ('CCID', models.CharField(max_length=30, null=True, verbose_name='CCID')),
                ('RegTimes', models.DateTimeField(auto_now_add=True, verbose_name='RegTimes')),
                ('RecTimes', models.DateTimeField(auto_now=True, verbose_name='RecTimes')),
                ('BeatTimes', models.DateTimeField(auto_now=True, verbose_name='BeatTimes')),
            ],
            options={
                'verbose_name': 'deviceInfo',
                'verbose_name_plural': 'deviceInfo',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=50, null=True, verbose_name='name')),
                ('ename', models.CharField(max_length=50, null=True, verbose_name='English Name')),
                ('country', models.CharField(max_length=20, null=True, verbose_name='Country')),
                ('province', models.CharField(max_length=20, null=True, verbose_name='Province')),
                ('city', models.CharField(max_length=50, null=True, verbose_name='city')),
                ('district', models.CharField(max_length=50, null=True, verbose_name='district')),
                ('address', models.CharField(max_length=50, null=True, verbose_name='address')),
                ('website', models.URLField(null=True, verbose_name='website')),
                ('telphone', models.CharField(max_length=30, null=True, verbose_name='telphone')),
                ('room', models.IntegerField(max_length=8, null=True, verbose_name='room')),
                ('device', models.IntegerField(max_length=8, null=True, verbose_name='device')),
            ],
            options={
                'verbose_name': 'organization',
                'verbose_name_plural': 'organization',
            },
        ),
        migrations.CreateModel(
            name='subclass_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=30, unique=True, verbose_name='Serial number')),
                ('name', models.CharField(max_length=120, verbose_name='name')),
                ('State', models.CharField(choices=[('to poy', 'to poy '), ('To be paid', 'To be paid'), ('Refund', 'Refund')], default='To be paid', max_length=10, verbose_name='State')),
                ('Type', models.CharField(choices=[('BANK', 'bank'), ('Alipay', 'alipay'), ('WeChat', 'wechat')], default='BANK', max_length=10, verbose_name='Transaction type')),
                ('Money', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Amount of money')),
                ('Duration', models.IntegerField(max_length=10, verbose_name='Transaction duration')),
                ('paymenttime', models.DateTimeField(auto_now_add=True, verbose_name='Payment time')),
                ('endtime', models.DateTimeField(auto_now=True, verbose_name='Payment time')),
                ('POnumber', models.IntegerField(max_length=20, verbose_name='Payment order number')),
                ('deviceInfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xproject.DeviceInfo')),
                ('normalUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xproject.Organization')),
            ],
            options={
                'verbose_name': 'subclass details',
                'verbose_name_plural': 'subclass details',
            },
        ),
        migrations.AddField(
            model_name='deviceinfo',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xproject.Organization'),
        ),
        migrations.AddField(
            model_name='normaluser',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xproject.Organization'),
        ),
        migrations.AddField(
            model_name='normaluser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
