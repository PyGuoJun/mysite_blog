# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-06-26 22:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190623_1947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='download_num',
        ),
    ]
