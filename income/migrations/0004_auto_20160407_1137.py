# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0003_auto_20160406_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='name',
            field=models.CharField(validators=[django.core.validators.RegexValidator(regex='^\\S+', message='Текст не должен начинаться пробелом'), django.core.validators.RegexValidator(regex='\\S+$', message='Текст не должен оканчиваться пробелом')], unique_for_date='date', verbose_name='Название', max_length=100),
        ),
        migrations.AlterField(
            model_name='position',
            name='number',
            field=models.CharField(validators=[django.core.validators.RegexValidator(regex='^\\S+', message='Текст не должен начинаться пробелом'), django.core.validators.RegexValidator(regex='\\S+$', message='Текст не должен оканчиваться пробелом')], verbose_name='Номер', max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name='position',
            unique_together=set([('delivery', 'number')]),
        ),
    ]
