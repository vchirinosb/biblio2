# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-04 03:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0005_auto_20161103_1117'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'ordering': ['nombre']},
        ),
    ]
