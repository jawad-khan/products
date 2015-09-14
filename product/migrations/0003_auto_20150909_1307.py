# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('product', '0002_auto_20150908_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=b'default_product.jpg', upload_to=b''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='cover',
            field=models.ImageField(default=b'default_cover.jpg', upload_to=b''),
            preserve_default=True,
        ),
    ]
