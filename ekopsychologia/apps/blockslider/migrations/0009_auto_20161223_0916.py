# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockslider', '0008_auto_20161222_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='blockslider',
            name='background_color_en',
            field=models.CharField(default=b'#FFFFFF', max_length=50, null=True, verbose_name='Kolor t\u0142a', choices=[(b'#FFFFFF', b'Bia\xc5\x82y'), (b'#2d3234', b'Ciemno szary')]),
        ),
        migrations.AddField(
            model_name='blockslider',
            name='background_color_pl',
            field=models.CharField(default=b'#FFFFFF', max_length=50, null=True, verbose_name='Kolor t\u0142a', choices=[(b'#FFFFFF', b'Bia\xc5\x82y'), (b'#2d3234', b'Ciemno szary')]),
        ),
        migrations.AddField(
            model_name='blockslider',
            name='background_en',
            field=models.ImageField(upload_to=b'blockslider', null=True, verbose_name='Obrazek t\u0142a', blank=True),
        ),
        migrations.AddField(
            model_name='blockslider',
            name='background_pl',
            field=models.ImageField(upload_to=b'blockslider', null=True, verbose_name='Obrazek t\u0142a', blank=True),
        ),
        migrations.AddField(
            model_name='blockslider',
            name='box_size_en',
            field=models.PositiveSmallIntegerField(default=1, help_text=b"Ilo\xc5\x9b\xc4\x87 kolumn Bootstrap'a / wysoko\xc5\x9b\xc4\x87 w px.", null=True, verbose_name='Rozmiar na stronie', choices=[(12, b'12/276'), (9, b'9/276'), (6, b'6/276'), (3, b'3/276')]),
        ),
        migrations.AddField(
            model_name='blockslider',
            name='box_size_pl',
            field=models.PositiveSmallIntegerField(default=1, help_text=b"Ilo\xc5\x9b\xc4\x87 kolumn Bootstrap'a / wysoko\xc5\x9b\xc4\x87 w px.", null=True, verbose_name='Rozmiar na stronie', choices=[(12, b'12/276'), (9, b'9/276'), (6, b'6/276'), (3, b'3/276')]),
        ),
        migrations.AddField(
            model_name='blockslider',
            name='content_en',
            field=models.TextField(null=True, verbose_name='Tre\u015b\u0107 w HTML', blank=True),
        ),
        migrations.AddField(
            model_name='blockslider',
            name='content_pl',
            field=models.TextField(null=True, verbose_name='Tre\u015b\u0107 w HTML', blank=True),
        ),
        migrations.AddField(
            model_name='blockslider',
            name='full_height_en',
            field=models.BooleanField(default=False, verbose_name='Pe\u0142na wysoko\u015b\u0107'),
        ),
        migrations.AddField(
            model_name='blockslider',
            name='full_height_pl',
            field=models.BooleanField(default=False, verbose_name='Pe\u0142na wysoko\u015b\u0107'),
        ),
        migrations.AddField(
            model_name='blockslider',
            name='more_button_text_en',
            field=models.CharField(help_text='Domy\u015blnie "zobacz"', max_length=100, null=True, verbose_name='Tekst przycisku wi\u0119cej', blank=True),
        ),
        migrations.AddField(
            model_name='blockslider',
            name='more_button_text_pl',
            field=models.CharField(help_text='Domy\u015blnie "zobacz"', max_length=100, null=True, verbose_name='Tekst przycisku wi\u0119cej', blank=True),
        ),
        migrations.AddField(
            model_name='blockslider',
            name='order_en',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='blockslider',
            name='order_pl',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='blockslider',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Tytu\u0142'),
        ),
        migrations.AddField(
            model_name='blockslider',
            name='title_pl',
            field=models.CharField(max_length=255, null=True, verbose_name='Tytu\u0142'),
        ),
        migrations.AddField(
            model_name='blockslider',
            name='url_en',
            field=models.CharField(help_text='Dla przycisku wi\u0119cje', max_length=255, null=True, verbose_name='Link', blank=True),
        ),
        migrations.AddField(
            model_name='blockslider',
            name='url_pl',
            field=models.CharField(help_text='Dla przycisku wi\u0119cje', max_length=255, null=True, verbose_name='Link', blank=True),
        ),
        migrations.AddField(
            model_name='blockslider',
            name='visible_en',
            field=models.BooleanField(default=True, verbose_name='Widoczny na stronie'),
        ),
        migrations.AddField(
            model_name='blockslider',
            name='visible_pl',
            field=models.BooleanField(default=True, verbose_name='Widoczny na stronie'),
        ),
    ]
