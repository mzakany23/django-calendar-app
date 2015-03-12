# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20150222_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendarevent',
            name='title',
            field=models.CharField(max_length=40, null=True, blank=True),
            preserve_default=True,
        ),
    ]
