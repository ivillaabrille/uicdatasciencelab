# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-25 09:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20170625_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsandupdate',
            name='NU_Logo',
            field=models.FileField(upload_to=''),
        ),
    ]
