# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slideshowimage',
            name='file',
            field=easy_thumbnails.fields.ThumbnailerImageField(upload_to=b'slideshows/', verbose_name='File'),
        ),
    ]
