# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-10 15:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_auto_20160210_1518'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectimage',
            name='desc',
        ),
    ]
