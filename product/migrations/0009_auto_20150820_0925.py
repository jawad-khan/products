# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20150818_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(related_name=b'phone', primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
