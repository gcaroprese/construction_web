# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slideshow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
            ],
            options={
                'verbose_name': 'Slideshow',
                'verbose_name_plural': 'Slideshows',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SlideshowImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(upload_to=b'slideshows/', verbose_name='File')),
                ('position', models.PositiveSmallIntegerField(default=0, verbose_name='Position')),
                ('slideshow', models.ForeignKey(related_name=b'images', verbose_name='Slideshow', to='website.Slideshow')),
            ],
            options={
                'ordering': ['position'],
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
            bases=(models.Model,),
        ),
    ]
