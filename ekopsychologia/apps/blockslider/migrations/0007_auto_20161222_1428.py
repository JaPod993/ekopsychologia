# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockslider', '0006_blocksliderfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blockslider',
            name='content',
            field=models.TextField(null=True, verbose_name='Tre\u015b\u0107 w HTML', blank=True),
        ),
    ]
