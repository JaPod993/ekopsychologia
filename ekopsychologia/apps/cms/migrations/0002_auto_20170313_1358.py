# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import corecms.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='for_lang',
            field=models.BooleanField(default=True, verbose_name='Dost\u0119pne w wybranym j\u0119zyku'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=corecms.fields.CMSTextField(default=b'', verbose_name='Tre\u015b\u0107', blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='content_pl',
            field=corecms.fields.CMSTextField(default=b'', null=True, verbose_name='Tre\u015b\u0107', blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='shortcut',
            field=corecms.fields.CMSTextField(verbose_name='Skr\xf3t'),
        ),
        migrations.AlterField(
            model_name='mediafile',
            name='path',
            field=models.FilePathField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='site',
            name='content',
            field=corecms.fields.CMSTextField(default=b'', verbose_name='Tre\u015b\u0107', blank=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='content_pl',
            field=corecms.fields.CMSTextField(default=b'', null=True, verbose_name='Tre\u015b\u0107', blank=True),
        ),
    ]
