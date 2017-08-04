# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainSystem', '0005_auto_20170730_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=30, null=True, verbose_name=b'\xe9\x83\xa8\xe9\x97\xa8\xe5\x90\x8d\xe7\xa7\xb0', blank=True),
        ),
    ]
