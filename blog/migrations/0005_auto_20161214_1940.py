# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-14 14:10
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20161210_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(default='Your text here'),
        ),
        migrations.AlterField(
            model_name='post',
            name='sticky',
            field=models.BooleanField(default=False, help_text='If checked this post will appear on top of list', verbose_name='Sticky'),
        ),
    ]
