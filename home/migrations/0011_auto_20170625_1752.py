# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-25 09:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_newsandupdate_nu_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsandupdate',
            name='NU_Posted',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]
