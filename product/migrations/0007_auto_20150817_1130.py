# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        ('product', '0006_auto_20150810_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(related_name=b'original_user', primary_key=True, serialize=False,
                                       to=settings.AUTH_USER_MODEL),
        ),
    ]
