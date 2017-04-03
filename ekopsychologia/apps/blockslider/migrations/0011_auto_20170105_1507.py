# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockslider', '0010_auto_20170105_1154'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blockslidercategory',
            options={'verbose_name': 'kategori\u0119', 'verbose_name_plural': 'Kategorie'},
        ),
        migrations.AlterField(
            model_name='blockslider',
            name='box_size',
            field=models.PositiveSmallIntegerField(default=1, help_text=b"Ilo\xc5\x9b\xc4\x87 kolumn Bootstrap'a / wysoko\xc5\x9b\xc4\x87 w px.", verbose_name='Rozmiar na stronie', choices=[(12, b'12/276'), (9, b'9/276'), (6, b'6/276'), (3, b'3/276'), (2, b'2/276')]),
        ),
        migrations.AlterField(
            model_name='blockslider',
            name='box_size_en',
            field=models.PositiveSmallIntegerField(default=1, help_text=b"Ilo\xc5\x9b\xc4\x87 kolumn Bootstrap'a / wysoko\xc5\x9b\xc4\x87 w px.", null=True, verbose_name='Rozmiar na stronie', choices=[(12, b'12/276'), (9, b'9/276'), (6, b'6/276'), (3, b'3/276'), (2, b'2/276')]),
        ),
        migrations.AlterField(
            model_name='blockslider',
            name='box_size_pl',
            field=models.PositiveSmallIntegerField(default=1, help_text=b"Ilo\xc5\x9b\xc4\x87 kolumn Bootstrap'a / wysoko\xc5\x9b\xc4\x87 w px.", null=True, verbose_name='Rozmiar na stronie', choices=[(12, b'12/276'), (9, b'9/276'), (6, b'6/276'), (3, b'3/276'), (2, b'2/276')]),
        ),
    ]
