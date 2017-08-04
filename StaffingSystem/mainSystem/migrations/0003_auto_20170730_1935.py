# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainSystem', '0002_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='dpt',
            field=models.ForeignKey(default=1, to='mainSystem.Department'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='ptn',
            field=models.ForeignKey(default=1, to='mainSystem.Position'),
            preserve_default=False,
        ),
    ]
