# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainSystem', '0008_employee_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name=b'\xe7\xa4\xbe\xe5\x9b\xa2\xe5\x90\x8d\xe7\xa7\xb0')),
            ],
            options={
                'verbose_name': '\u793e\u56e2',
                'verbose_name_plural': '\u793e\u56e2',
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='group',
            field=models.ManyToManyField(to='mainSystem.Group'),
        ),
    ]
