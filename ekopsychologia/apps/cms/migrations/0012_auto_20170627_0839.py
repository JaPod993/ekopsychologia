# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-27 08:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0011_site_archived'),
    ]

    operations = [
        migrations.AddField(
            model_name='configcms',
            name='events',
            field=models.IntegerField(default=0, verbose_name='Ilo\u015b\u0107 wydarze\u0144'),
        ),
        migrations.AddField(
            model_name='configcms',
            name='experts',
            field=models.IntegerField(default=0, verbose_name='Ekspert\xf3w'),
        ),
        migrations.AddField(
            model_name='configcms',
            name='founds',
            field=models.IntegerField(default=0, verbose_name='Milion\xf3w z\u0142otych pozyskanych na dzia\u0142ania'),
        ),
        migrations.AddField(
            model_name='configcms',
            name='institutions',
            field=models.IntegerField(default=0, verbose_name='Inistytucji w Porozumieniu Karpackim'),
        ),
        migrations.AddField(
            model_name='configcms',
            name='participants',
            field=models.IntegerField(default=0, verbose_name='Uczestnicy'),
        ),
        migrations.AddField(
            model_name='configcms',
            name='projects',
            field=models.IntegerField(default=0, verbose_name='Zrealizowane Projekty'),
        ),
    ]
