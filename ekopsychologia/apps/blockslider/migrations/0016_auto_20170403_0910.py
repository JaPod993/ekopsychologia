# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockslider', '0015_blockslider_without_margins'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blockslider',
            name='background_color_en',
        ),
        migrations.RemoveField(
            model_name='blockslider',
            name='background_en',
        ),
        migrations.RemoveField(
            model_name='blockslider',
            name='box_size_en',
        ),
        migrations.RemoveField(
            model_name='blockslider',
            name='content_en',
        ),
        migrations.RemoveField(
            model_name='blockslider',
            name='full_height_en',
        ),
        migrations.RemoveField(
            model_name='blockslider',
            name='more_button_text_en',
        ),
        migrations.RemoveField(
            model_name='blockslider',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='blockslider',
            name='url_en',
        ),
        migrations.RemoveField(
            model_name='blockslider',
            name='visible_en',
        ),
    ]
