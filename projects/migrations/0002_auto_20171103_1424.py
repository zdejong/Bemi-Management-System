# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 07:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(help_text='Describe what the client wants', max_length=120),
        ),
    ]
