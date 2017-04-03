# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockslider', '0014_auto_20170222_0831'),
    ]

    operations = [
        migrations.AddField(
            model_name='blockslider',
            name='without_margins',
            field=models.BooleanField(default=False, verbose_name='Bez margines\xf3w'),
        ),
    ]
