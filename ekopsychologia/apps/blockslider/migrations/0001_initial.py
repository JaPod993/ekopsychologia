# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlockSlider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='Tytu\u0142')),
                ('content', models.TextField(verbose_name='Tre\u015b\u0107 w HTML')),
                ('background', models.ImageField(upload_to=b'blockslider', verbose_name='Obrazek t\u0142a')),
                ('url', models.CharField(help_text='Dla przycisku wi\u0119cje', max_length=255, null=True, verbose_name='Link', blank=True)),
                ('visible', models.BooleanField(default=True, verbose_name='Widoczny na stronie')),
                ('box_size', models.PositiveSmallIntegerField(default=1, verbose_name='Rozmiar na stronie', choices=[(1, b'12/276'), (2, b'9/276'), (3, b'6/276'), (4, b'3/276')])),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Slider blokowy',
                'verbose_name_plural': 'Slider blokowy',
            },
        ),
    ]
