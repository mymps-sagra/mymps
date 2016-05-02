# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0003_auto_20160418_1142'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='positionexp',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='positionexp',
            name='design',
        ),
        migrations.RemoveField(
            model_name='positionexp',
            name='issue',
        ),
        migrations.RemoveField(
            model_name='positionexp',
            name='item',
        ),
        migrations.RemoveField(
            model_name='positionexp',
            name='packing',
        ),
        migrations.RemoveField(
            model_name='positionexp',
            name='part',
        ),
        migrations.RemoveField(
            model_name='positionexp',
            name='unit',
        ),
        migrations.DeleteModel(
            name='PositionExp',
        ),
    ]
