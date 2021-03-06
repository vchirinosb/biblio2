# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-05 01:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0007_auto_20161103_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='biblioteca.Autor'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='editorial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='biblioteca.Editorial'),
        ),
    ]
