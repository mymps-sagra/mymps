# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import income.models


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0002_auto_20160404_1200'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='position',
            options={'verbose_name': 'Позиция поставки', 'verbose_name_plural': 'Позиции поставок', 'ordering': ['number']},
        ),
        migrations.AlterField(
            model_name='position',
            name='packing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='refer.Packing', verbose_name='Фасовка', null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='quantity',
            field=models.DecimalField(default=0, decimal_places=6, verbose_name='Количество', max_digits=20),
        ),
        migrations.AlterField(
            model_name='position',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='refer.Unit', verbose_name='Единица', null=True),
        ),
    ]
