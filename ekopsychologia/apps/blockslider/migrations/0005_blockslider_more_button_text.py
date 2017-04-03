# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockslider', '0004_blockslider_full_height'),
    ]

    operations = [
        migrations.AddField(
            model_name='blockslider',
            name='more_button_text',
            field=models.CharField(max_length=100, null=True, verbose_name='Tekst przycisku wi\u0119cej', blank=True),
        ),
    ]
