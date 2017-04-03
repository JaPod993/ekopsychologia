# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockslider', '0009_auto_20161223_0916'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockSliderCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identity', models.SlugField(verbose_name=b'Identyfikator')),
                ('name', models.CharField(max_length=200, verbose_name=b'Nazwa')),
            ],
            options={
                'verbose_name': 'Kategoria',
                'verbose_name_plural': 'Kategoria',
            },
        ),
        migrations.AddField(
            model_name='blockslider',
            name='category',
            field=models.ForeignKey(verbose_name='Kategoria', blank=True, to='blockslider.BlockSliderCategory', null=True),
        ),
    ]
