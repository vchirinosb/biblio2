# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-04 04:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0006_auto_20161103_2258'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='editorial',
            options={'ordering': ['editorial']},
        ),
        migrations.AlterModelOptions(
            name='libro',
            options={'ordering': ['titulo', 'autor', 'editorial']},
        ),
    ]
