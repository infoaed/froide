# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-07 18:50
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bounce', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bounce',
            name='bounces',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=list),
        ),
    ]
