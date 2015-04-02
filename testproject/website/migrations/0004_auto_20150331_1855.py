# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_simplepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='simplepage',
            name='header_text',
            field=models.CharField(default=1, help_text=b'The text that will be shown bold at the top of the page', max_length=45),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body',
            field=models.TextField(help_text=b'The body of the page'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='url',
            field=models.CharField(help_text=b'The url to use (everything after ltjjc.com).', max_length=100),
            preserve_default=True,
        ),
    ]
