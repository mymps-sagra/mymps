# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import common.models


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0005_auto_20160418_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='quantity',
            field=models.DecimalField(verbose_name='Количество', validators=[common.models.CommonPositionModel.clean_quantity], decimal_places=6, max_digits=20, default=0),
        ),
    ]
