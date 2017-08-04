# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainSystem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name=b'\xe8\x81\x8c\xe4\xbd\x8d')),
            ],
            options={
                'verbose_name': '\u804c\u4f4d\u4fe1\u606f',
                'verbose_name_plural': '\u804c\u4f4d\u4fe1\u606f',
            },
        ),
    ]
