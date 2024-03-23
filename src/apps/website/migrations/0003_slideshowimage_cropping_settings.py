# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20141203_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='slideshowimage',
            name='cropping_settings',
            field=models.CharField(default=b'center_center_cover', max_length=50, verbose_name='Cropping Settings'),
            preserve_default=True,
        ),
    ]
