# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-25 09:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20170625_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsandupdate',
            name='NU_Category',
            field=models.CharField(choices=[('News', 'News'), ('Update', 'Update'), ('Event', 'Event'), ('Article', 'Article')], default='News', max_length=100),
        ),
        migrations.AlterField(
            model_name='newsandupdate',
            name='NU_Poster',
            field=models.CharField(choices=[('Glenn Paul Gara', 'ggara'), ('Isaiah Evans Villa Abrille', 'ivillaabrille'), ('Seth Jasper Napalit', 'snapalit'), ('Neil Ivan Palacios', 'npalacios'), ('Christine Joy Busalanan', 'cbusalanan'), ('Jesmar James Rama', 'jrama'), ('Reno Marco Fandiño', 'rfandino'), ('Quinn Intrepido', 'qintrepido'), ('Mark Kenneth Jimenez', 'mjimenez'), ('Arch Falconi', 'afalconi'), ('Elven Earl Tsuruoka', 'etsuruoka'), ('Nikko Tulang', 'ntulang')], default='Glenn Paul Gara', max_length=100),
        ),
    ]
