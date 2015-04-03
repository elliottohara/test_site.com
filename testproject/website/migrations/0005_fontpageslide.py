# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20150331_1855'),
    ]

    operations = [
        migrations.CreateModel(
            name='FontPageSlide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('header', models.CharField(help_text=b'The large text displayed on the slide.', max_length=50, null=True, blank=True)),
                ('subtext', models.CharField(help_text=b'The smaller text shown under the largetext on the slide.', max_length=100, null=True, blank=True)),
                ('navigate_to', models.CharField(help_text=b'The link to display with the "continue reading" sign. Can be blank', max_length=50, null=True, blank=True)),
                ('image', models.ImageField(upload_to=b'slide')),
                (b'cropped', image_cropping.fields.ImageRatioField(b'image', '900x600', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='cropped')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
