# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-26 09:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0005_profile_email_confirmed'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='pics/'),
        ),
    ]
