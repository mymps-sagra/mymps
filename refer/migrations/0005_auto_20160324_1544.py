# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('refer', '0004_auto_20160323_1315'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bases',
            options={'verbose_name': 'Обоснование', 'verbose_name_plural': 'Обоснования'},
        ),
        migrations.RenameField(
            model_name='bases',
            old_name='DateFrom',
            new_name='date_from',
        ),
        migrations.RenameField(
            model_name='bases',
            old_name='DateTo',
            new_name='date_to',
        ),
        migrations.RenameField(
            model_name='bases',
            old_name='Type',
            new_name='type',
        ),
        migrations.AlterField(
            model_name='bases',
            name='name',
            field=models.CharField(verbose_name='Название', validators=[django.core.validators.RegexValidator(regex='^\\S+', message='Текст не должен начинаться пробелом'), django.core.validators.RegexValidator(regex='\\S+$', message='Текст не должен оканчиваться пробелом')], unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='typesbase',
            name='name',
            field=models.CharField(verbose_name='Название', validators=[django.core.validators.RegexValidator(regex='^\\S+', message='Текст не должен начинаться пробелом'), django.core.validators.RegexValidator(regex='\\S+$', message='Текст не должен оканчиваться пробелом')], unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='typesinput',
            name='name',
            field=models.CharField(verbose_name='Название', validators=[django.core.validators.RegexValidator(regex='^\\S+', message='Текст не должен начинаться пробелом'), django.core.validators.RegexValidator(regex='\\S+$', message='Текст не должен оканчиваться пробелом')], unique=True, max_length=100),
        ),
    ]
