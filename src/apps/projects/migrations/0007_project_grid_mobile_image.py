# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20150107_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='grid_mobile_image',
            field=easy_thumbnails.fields.ThumbnailerImageField(upload_to=b'', null=True, verbose_name='Grid Mobile Image', blank=True),
            preserve_default=True,
        ),
    ]
