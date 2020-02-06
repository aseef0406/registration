# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-02-06 17:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20200206_0152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('O', 'Organizer'), ('V', 'Volunteer'), ('H', 'Hacker'), ('M', 'Mentor'), ('S', 'Sponsor'), ('U', 'Unaccepted')], default='U', max_length=2),
        ),
    ]