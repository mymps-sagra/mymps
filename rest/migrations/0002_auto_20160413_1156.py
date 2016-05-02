# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TotalPeriod',
            new_name='Period',
        ),
        migrations.RenameField(
            model_name='turnover',
            old_name='total_period',
            new_name='period',
        ),
    ]
