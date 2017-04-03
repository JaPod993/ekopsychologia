# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockslider', '0002_auto_20161222_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='blockslider',
            name='background_color',
            field=models.CharField(default=b'#FFFFFF', max_length=50, verbose_name='Kolor t\u0142a', choices=[(b'#FFFFFF', b'Bia\xc5\x82y'), (b'#2d3234', b'Ciemno szary')]),
        ),
    ]
