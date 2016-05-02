# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0004_auto_20160407_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='quantity',
            field=models.DecimalField(decimal_places=6, verbose_name='Количество', default=0, max_digits=20),
        ),
    ]
