# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name=b'cropped',
            field=image_cropping.fields.ImageRatioField(b'bio_image', '400x400', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='cropped'),
            preserve_default=True,
        ),
    ]
