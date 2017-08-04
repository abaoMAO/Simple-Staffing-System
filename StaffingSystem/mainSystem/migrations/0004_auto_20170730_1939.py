# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainSystem', '0003_auto_20170730_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='telphone',
            field=models.IntegerField(verbose_name=b'\xe6\x89\x8b\xe6\x9c\xba'),
        ),
    ]
