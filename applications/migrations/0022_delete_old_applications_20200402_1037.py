# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-04-02 17:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0021_new_applications_20200402_1036'),
        ('checkin', '0002_to_new_applications_20200402_1036'),
        ('organizers', '0002_to_new_applications_20200402_1036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='contacted_by',
        ),
        migrations.RemoveField(
            model_name='application',
            name='invited_by',
        ),
        migrations.RemoveField(
            model_name='application',
            name='user',
        ),
        migrations.DeleteModel(
            name='Application',
        ),
    ]