# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-05 10:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]