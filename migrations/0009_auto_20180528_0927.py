# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-28 09:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0008_auto_20180527_0817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='business_name',
            field=models.CharField(max_length=80),
        ),
    ]
