# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-03 07:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_taskshandle_is_finish'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskshandle',
            name='delay_end_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='\u4efb\u52a1\u8bbe\u7f6e\u5ef6\u8fdf\u65f6\u7684\u7ed3\u675f\u65f6\u95f4'),
        ),
        migrations.AddField(
            model_name='taskshandle',
            name='delay_start_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='\u4efb\u52a1\u8bbe\u7f6e\u5ef6\u8fdf\u65f6\u7684\u5f00\u59cb\u65f6\u95f4'),
        ),
    ]