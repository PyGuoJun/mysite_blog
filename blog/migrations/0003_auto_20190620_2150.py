# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-06-20 21:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190619_0757'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='download',
            field=models.FileField(blank=True, null=True, upload_to='resource/%Y%m', verbose_name='资源文件'),
        ),
        migrations.AddField(
            model_name='entry',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='资料名称'),
        ),
    ]
