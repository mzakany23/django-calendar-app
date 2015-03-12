# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20150221_2127'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalendarEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('start', models.DateField()),
                ('end', models.DateField(null=True, blank=True)),
                ('color', models.ForeignKey(blank=True, to='events.EventColor', null=True)),
                ('type', models.ForeignKey(to='events.EventType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='event',
            name='color',
        ),
        migrations.RemoveField(
            model_name='event',
            name='type',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
    ]
