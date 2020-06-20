# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20150914_0648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userproduct',
            name='product',
            field=models.ForeignKey(related_name=b'product', to='product.Product'),
        ),
    ]
