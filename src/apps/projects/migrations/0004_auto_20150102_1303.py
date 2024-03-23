# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20150102_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='grid_h',
            field=models.PositiveIntegerField(default=0, max_length=512, verbose_name='Grid H'),
        ),
        migrations.AlterField(
            model_name='project',
            name='grid_w',
            field=models.PositiveIntegerField(default=0, max_length=512, verbose_name='Grid W'),
        ),
    ]
