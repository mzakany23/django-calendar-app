# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_calendarevent_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendarevent',
            name='color',
            field=models.ForeignKey(to='events.EventColor', null=True),
            preserve_default=True,
        ),
    ]
