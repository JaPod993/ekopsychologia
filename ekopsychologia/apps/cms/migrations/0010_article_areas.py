# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-15 12:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0009_site_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='areas',
            field=models.ManyToManyField(blank=True, related_name='_article_areas_+', to='cms.Site', verbose_name=b'Obszary dzia\xc5\x82ania'),
        ),
    ]
