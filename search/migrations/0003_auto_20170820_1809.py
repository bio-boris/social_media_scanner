# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-20 18:09
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20170820_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchjob',
            name='sites',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), size=None),
        ),
    ]
