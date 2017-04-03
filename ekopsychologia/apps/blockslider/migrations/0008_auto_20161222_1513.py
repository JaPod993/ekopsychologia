# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockslider', '0007_auto_20161222_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blockslider',
            name='more_button_text',
            field=models.CharField(help_text='Domy\u015blnie "zobacz"', max_length=100, null=True, verbose_name='Tekst przycisku wi\u0119cej', blank=True),
        ),
    ]
