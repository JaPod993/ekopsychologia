# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockslider', '0005_blockslider_more_button_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockSliderFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_file', models.FileField(upload_to=b'blockslider_files', verbose_name='Plik')),
                ('block', models.ForeignKey(to='blockslider.BlockSlider')),
            ],
        ),
    ]
