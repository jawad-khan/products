# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_auto_20150824_1136'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Detail',
            new_name='detail',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Price',
            new_name='price',
        ),
    ]
