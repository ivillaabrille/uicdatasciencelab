# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-25 09:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20170623_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsandupdate',
            name='NU_Category',
            field=models.CharField(choices=[('news', 'News'), ('update', 'Update'), ('event', 'Event'), ('article', 'Article')], default='News', max_length=10),
        ),
        migrations.AddField(
            model_name='newsandupdate',
            name='NU_Poster',
            field=models.CharField(choices=[('ggara', 'Glenn Paul Gara'), ('ivillaabrille', 'Isaiah Evans Villa Abrille'), ('snapalit', 'Seth Jasper Napalit'), ('npalacios', 'Neil Ivan Palacios'), ('cbusalanan', 'Christine Joy Busalanan'), ('jrama', 'Jesmar James Rama'), ('rfandino', 'Reno Marco Fandiño'), ('qintrepido', 'Quinn Intrepido'), ('mjimanez', 'Mark Kenneth Jimenez'), ('afalconi', 'Arch Falconi'), ('etsuruoka', 'Elven Earl Tsuruoka'), ('ntulang', 'Nikko Tulang')], default='Glenn Paul Gara', max_length=100),
        ),
        migrations.AlterField(
            model_name='newsandupdate',
            name='NU_Logo',
            field=models.FileField(upload_to=''),
        ),
    ]
