# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-01 21:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0002_editorial_libro_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='descripcion',
            field=models.CharField(max_length=450, null=True),
        ),
        migrations.AlterField(
            model_name='libro',
            name='imagenportada',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
