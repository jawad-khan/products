# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('product', '0004_address_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(default=b'PK', max_length=2,
                                   choices=[(b'PK', b'Pakistan'), (b'US', b'USA'), (b'UK', b'England'),
                                            (b'AS', b'Australia'), (b'NZ', b'NewZeland')]),
        ),
    ]
