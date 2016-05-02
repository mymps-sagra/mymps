# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('refer', '0006_auto_20160330_1645'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypesIncome',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(validators=[django.core.validators.RegexValidator(regex='^\\S+', message='Текст не должен начинаться пробелом'), django.core.validators.RegexValidator(regex='\\S+$', message='Текст не должен оканчиваться пробелом')], max_length=100, verbose_name='Название', unique=True)),
                ('accessability', models.BooleanField(default=False, verbose_name='Доступно')),
                ('comment', models.TextField(max_length=1000, blank=True, verbose_name='Примечание')),
                ('order', models.FloatField(default=0, verbose_name='Порядок')),
                ('created', models.DateTimeField(db_index=True, auto_now_add=True, verbose_name='Создано')),
                ('modifyed', models.DateTimeField(db_index=True, auto_now=True, verbose_name='Изменено')),
                ('code', models.SlugField(verbose_name='Код', unique=True)),
            ],
            options={
                'verbose_name_plural': 'Типы поставок',
                'verbose_name': 'Тип поставки',
            },
        ),
        migrations.DeleteModel(
            name='TypesInput',
        ),
    ]
