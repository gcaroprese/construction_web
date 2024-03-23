# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_slideshowimage_cropping_settings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slideshowimage',
            name='cropping_settings',
            field=models.CharField(default=b'center_center_cover', max_length=50, verbose_name='Cropping Settings', choices=[(b'center_center_contain', 'Center Center - No Crop'), (b'left_top_cover', 'Left Top - Crop'), (b'left_center_cover', 'Left Center - Crop'), (b'left_bottom_cover', 'Left Bottom - Crop'), (b'right_top_cover', 'Right Top - Crop'), (b'right_center_cover', 'Right Center - Crop'), (b'right_bottom_cover', 'Right Bottom - Crop'), (b'center_top_cover', 'Center Top - Crop'), (b'center_center_cover', 'Center Center - Crop'), (b'center_bottom_cover', 'Center Bottom - Crop')]),
        ),
    ]
