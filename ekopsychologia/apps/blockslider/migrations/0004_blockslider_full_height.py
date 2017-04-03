# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockslider', '0003_blockslider_background_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='blockslider',
            name='full_height',
            field=models.BooleanField(default=False, verbose_name='Pe\u0142na wysoko\u015b\u0107'),
        ),
    ]
