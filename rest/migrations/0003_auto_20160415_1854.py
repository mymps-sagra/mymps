# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0002_auto_20160413_1156'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='period',
            options={'verbose_name_plural': 'Периоды', 'ordering': ['-date', 'name'], 'verbose_name': 'Период'},
        ),
        migrations.AddField(
            model_name='period',
            name='stores_only_blank',
            field=models.BooleanField(verbose_name='Только неопределенные хранилища', default=False),
        ),
        migrations.AddField(
            model_name='period',
            name='targets_only_blank',
            field=models.BooleanField(verbose_name='Только неопределенные цели', default=False),
        ),
        migrations.AlterField(
            model_name='turnover',
            name='period',
            field=models.ForeignKey(verbose_name='Период', to='rest.Period', on_delete=django.db.models.deletion.PROTECT, null=True),
        ),
    ]
