# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 05:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsandupdate',
            name='NU_Content',
            field=models.TextField(),
        ),
    ]
