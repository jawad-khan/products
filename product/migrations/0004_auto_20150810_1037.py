# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        ('product', '0003_auto_20150810_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_product',
            name='user',
            field=models.ForeignKey(related_name=b'product', to=settings.AUTH_USER_MODEL),
        ),
    ]
