# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventtype',
            name='description',
            field=models.TextField(max_length=500, null=True),
            preserve_default=True,
        ),
    ]
