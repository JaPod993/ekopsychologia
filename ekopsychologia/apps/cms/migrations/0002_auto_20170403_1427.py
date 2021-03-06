# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2017-04-03 14:27
from __future__ import unicode_literals

import corecms.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='main_image',
            field=corecms.fields.Base64ImageField(blank=True, null=True, upload_to=b'article/images/', verbose_name='Obrazek przewodni'),
        ),
        migrations.AlterField(
            model_name='article',
            name='shortcut',
            field=corecms.fields.CMSTextField(blank=True, default=b'', verbose_name='Skr\xf3t'),
        ),
        migrations.AlterField(
            model_name='article',
            name='thumbnail',
            field=corecms.fields.Base64ImageField(blank=True, null=True, upload_to=b'article/images/', verbose_name='Miniaturka'),
        ),
        migrations.AlterField(
            model_name='site',
            name='main_image',
            field=corecms.fields.Base64ImageField(blank=True, null=True, upload_to=b'site/images/', verbose_name='Obrazek przewodni'),
        ),
        migrations.AlterField(
            model_name='site',
            name='thumbnail',
            field=corecms.fields.Base64ImageField(blank=True, null=True, upload_to=b'site/images/', verbose_name='Miniaturka'),
        ),
    ]
