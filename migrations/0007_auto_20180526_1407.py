# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-26 14:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0006_profile_profile_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile_photo',
            new_name='user_photo',
        ),
    ]
