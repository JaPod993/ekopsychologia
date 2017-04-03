# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockslider', '0012_auto_20170118_0830'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blockslider',
            name='order_en',
        ),
        migrations.RemoveField(
            model_name='blockslider',
            name='order_pl',
        ),
    ]
