# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=25)),
                ('description', models.TextField(null=True)),
                ('sort_order', models.PositiveSmallIntegerField(default=500)),
            ],
            options={
                'verbose_name_plural': 'Classes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=50)),
                ('bio', models.TextField(null=True)),
                ('sort_order', models.PositiveSmallIntegerField(default=500)),
                ('bio_image', models.ImageField(null=True, upload_to=b'')),
            ],
            options={
                'verbose_name_plural': 'Staff',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='class',
            name='instructor',
            field=models.ForeignKey(to='website.Staff'),
            preserve_default=True,
        ),
    ]
