# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 14:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0003_stationlocations'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StationLocations',
            new_name='Location',
        ),
    ]