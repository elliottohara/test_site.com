# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_staff_cropped'),
    ]

    operations = [
        migrations.CreateModel(
            name='SimplePage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to=b'spi')),
                (b'cropped', image_cropping.fields.ImageRatioField(b'image', '400x400', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='cropped')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
