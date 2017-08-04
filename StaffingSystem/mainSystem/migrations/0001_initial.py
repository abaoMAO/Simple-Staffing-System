# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name=b'\xe9\x83\xa8\xe9\x97\xa8\xe5\x90\x8d\xe7\xa7\xb0')),
            ],
            options={
                'verbose_name': '\u90e8\u95e8\u4fe1\u606f',
                'verbose_name_plural': '\u90e8\u95e8\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d')),
                ('age', models.IntegerField(verbose_name=b'\xe5\xb9\xb4\xe9\xbe\x84')),
                ('telphone', models.IntegerField(max_length=13, verbose_name=b'\xe6\x89\x8b\xe6\x9c\xba')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1', blank=True)),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'verbose_name': '\u5458\u5de5\u4fe1\u606f',
                'verbose_name_plural': '\u5458\u5de5\u4fe1\u606f',
            },
        ),
    ]
