# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-04 11:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20170104_1059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='created_date',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='modified_date',
            new_name='modified',
        ),
    ]
