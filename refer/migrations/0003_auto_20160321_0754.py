# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('refer', '0002_auto_20160321_0748'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='typesinput',
            options={'verbose_name_plural': 'Типы поставок', 'verbose_name': 'Тип поставки'},
        ),
    ]
