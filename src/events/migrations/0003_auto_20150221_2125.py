# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_eventtype_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='color',
            field=models.ForeignKey(blank=True, to='events.EventColor', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='end',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
