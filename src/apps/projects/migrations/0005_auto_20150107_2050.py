# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20150102_1303'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['grid_x', 'grid_y'], 'verbose_name': 'Project', 'verbose_name_plural': 'Projects'},
        ),
        migrations.AddField(
            model_name='projectimage',
            name='cropping_settings',
            field=models.CharField(default=b'center_center_cover', max_length=50, verbose_name='Cropping Settings'),
            preserve_default=True,
        ),
    ]
