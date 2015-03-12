# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20150221_2125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventtype',
            old_name='type',
            new_name='name',
        ),
    ]
