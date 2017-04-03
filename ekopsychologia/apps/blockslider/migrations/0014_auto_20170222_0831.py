# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockslider', '0013_auto_20170124_1053'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blockslidercategory',
            options={'verbose_name': 'Kategoria slidera', 'verbose_name_plural': 'Kategorie slidera'},
        ),
    ]
