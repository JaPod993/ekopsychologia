# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockslider', '0011_auto_20170105_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blockslider',
            name='background_color',
            field=models.CharField(default=b'#FFFFFF', max_length=50, verbose_name='Kolor t\u0142a', choices=[(b'#FFFFFF', b'Bia\xc5\x82y'), (b'#2d3234', b'Ciemno szary'), (b'#1f2224', b'Ciemniejszy szary'), (b'#e74a05', b'Pomara\xc5\x84czowy')]),
        ),
        migrations.AlterField(
            model_name='blockslider',
            name='background_color_en',
            field=models.CharField(default=b'#FFFFFF', max_length=50, null=True, verbose_name='Kolor t\u0142a', choices=[(b'#FFFFFF', b'Bia\xc5\x82y'), (b'#2d3234', b'Ciemno szary'), (b'#1f2224', b'Ciemniejszy szary'), (b'#e74a05', b'Pomara\xc5\x84czowy')]),
        ),
        migrations.AlterField(
            model_name='blockslider',
            name='background_color_pl',
            field=models.CharField(default=b'#FFFFFF', max_length=50, null=True, verbose_name='Kolor t\u0142a', choices=[(b'#FFFFFF', b'Bia\xc5\x82y'), (b'#2d3234', b'Ciemno szary'), (b'#1f2224', b'Ciemniejszy szary'), (b'#e74a05', b'Pomara\xc5\x84czowy')]),
        ),
        migrations.AlterField(
            model_name='blockslider',
            name='box_size',
            field=models.PositiveSmallIntegerField(default=1, help_text=b"Ilo\xc5\x9b\xc4\x87 kolumn Bootstrap'a / wysoko\xc5\x9b\xc4\x87 w px.", verbose_name='Rozmiar na stronie', choices=[(12, b'12/276'), (9, b'9/276'), (8, b'8/276'), (7, b'7/276'), (6, b'6/276'), (5, b'5/276'), (4, b'4/276'), (3, b'3/276'), (2, b'2/276')]),
        ),
        migrations.AlterField(
            model_name='blockslider',
            name='box_size_en',
            field=models.PositiveSmallIntegerField(default=1, help_text=b"Ilo\xc5\x9b\xc4\x87 kolumn Bootstrap'a / wysoko\xc5\x9b\xc4\x87 w px.", null=True, verbose_name='Rozmiar na stronie', choices=[(12, b'12/276'), (9, b'9/276'), (8, b'8/276'), (7, b'7/276'), (6, b'6/276'), (5, b'5/276'), (4, b'4/276'), (3, b'3/276'), (2, b'2/276')]),
        ),
        migrations.AlterField(
            model_name='blockslider',
            name='box_size_pl',
            field=models.PositiveSmallIntegerField(default=1, help_text=b"Ilo\xc5\x9b\xc4\x87 kolumn Bootstrap'a / wysoko\xc5\x9b\xc4\x87 w px.", null=True, verbose_name='Rozmiar na stronie', choices=[(12, b'12/276'), (9, b'9/276'), (8, b'8/276'), (7, b'7/276'), (6, b'6/276'), (5, b'5/276'), (4, b'4/276'), (3, b'3/276'), (2, b'2/276')]),
        ),
    ]
