# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20150102_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='grid_badge_position',
            field=models.CharField(default='Bottom Left', max_length=12, verbose_name='Badge Position', choices=[(b'bottom_left', 'Bottom Left'), (b'bottom_right', 'Bottom Right'), (b'top_left', 'Top Left'), (b'top_right', 'Top Right')]),
        ),
        migrations.AlterField(
            model_name='project',
            name='grid_h',
            field=models.PositiveIntegerField(default=1, max_length=512, verbose_name='Grid H'),
        ),
        migrations.AlterField(
            model_name='project',
            name='grid_w',
            field=models.PositiveIntegerField(default=1, max_length=512, verbose_name='Grid W'),
        ),
        migrations.AlterField(
            model_name='project',
            name='grid_x',
            field=models.PositiveIntegerField(default=0, max_length=512, verbose_name='Grid X'),
        ),
        migrations.AlterField(
            model_name='project',
            name='grid_y',
            field=models.PositiveIntegerField(default=0, max_length=512, verbose_name='Grid Y'),
        ),
    ]
