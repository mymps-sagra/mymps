# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0002_auto_20160418_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='positionexp',
            name='quantity',
            field=models.DecimalField(default=0, decimal_places=6, max_digits=20, verbose_name='Количество'),
        ),
    ]
