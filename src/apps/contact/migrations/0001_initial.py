# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=255, verbose_name='Full Name')),
                ('email', models.EmailField(max_length=75, verbose_name=b'Email')),
                ('message', models.TextField(verbose_name='Message')),
                ('cv', models.FileField(upload_to=b'cvs/', null=True, verbose_name='CV', blank=True)),
                ('status', models.PositiveSmallIntegerField(default=0, verbose_name='Status', choices=[(0, 'Pending'), (1, 'Answered')])),
                ('date', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='Date', editable=False)),
            ],
            options={
                'ordering': ['-date'],
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recipient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('email', models.EmailField(max_length=75, verbose_name='Email')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
            ],
            options={
                'verbose_name': 'Recipient',
                'verbose_name_plural': 'Recipients',
            },
            bases=(models.Model,),
        ),
    ]
