# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-17 21:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_pushnotification_recipients'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pushnotification',
            options={'verbose_name': 'Push Notification', 'verbose_name_plural': 'Push Notifications'},
        ),
    ]
