# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.projects.fields
import easy_thumbnails.fields
import django.core.validators
import apps.projects.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=512, verbose_name='Name')),
                ('slug', models.SlugField(unique=True, max_length=512, verbose_name='Slug')),
                ('program', models.TextField(verbose_name='Program', blank=True)),
                ('work', models.TextField(verbose_name='Work', blank=True)),
                ('authors', models.TextField(default='Aulet Abiega Arquitectos', verbose_name='Authors', blank=True)),
                ('location', models.TextField(verbose_name='Location', blank=True)),
                ('year', apps.projects.fields.YearField(blank=True, null=True, verbose_name='Year', validators=[django.core.validators.RegexValidator(b'^\\d{4}$', 'Enter a valid year.', b'invalid')])),
                ('surface', models.PositiveIntegerField(null=True, verbose_name='Surface', blank=True)),
                ('grid_x', models.PositiveIntegerField(max_length=512, verbose_name='Grid X')),
                ('grid_y', models.PositiveIntegerField(max_length=512, verbose_name='Grid Y')),
                ('grid_w', models.PositiveIntegerField(max_length=512, verbose_name='Grid W')),
                ('grid_h', models.PositiveIntegerField(max_length=512, verbose_name='Grid H')),
                ('grid_image', easy_thumbnails.fields.ThumbnailerImageField(upload_to=b'', verbose_name='Grid Image')),
                ('grid_badge_position', models.CharField(default='Bottom Left', max_length=12, verbose_name='Bagde Position', choices=[(b'bottom_left', 'Bottom Left'), (b'bottom_right', 'Bottom Right'), (b'top_left', 'Top Left'), (b'top_right', 'Top Right')])),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
            bases=(apps.projects.models.NameHandler, models.Model),
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', easy_thumbnails.fields.ThumbnailerImageField(upload_to=b'projects/', verbose_name='File')),
                ('position', models.PositiveSmallIntegerField(default=0, verbose_name='Position')),
                ('project', models.ForeignKey(related_name=b'images', verbose_name='Project', to='projects.Project')),
            ],
            options={
                'ordering': ['position'],
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
            bases=(models.Model,),
        ),
    ]
