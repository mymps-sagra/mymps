# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('refer', '0012_auto_20160401_1128'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypePart',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message='Текст не должен начинаться пробелом', regex='^\\S+'), django.core.validators.RegexValidator(message='Текст не должен оканчиваться пробелом', regex='\\S+$')], verbose_name='Название', unique=True)),
                ('accessability', models.BooleanField(default=False, verbose_name='Доступно')),
                ('comment', models.TextField(max_length=1000, blank=True, verbose_name='Примечание')),
                ('order', models.FloatField(default=0, verbose_name='Порядок')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано', db_index=True)),
                ('modifyed', models.DateTimeField(auto_now=True, verbose_name='Изменено', db_index=True)),
                ('code', models.SlugField(verbose_name='Код', unique=True)),
            ],
            options={
                'verbose_name_plural': 'Типы партий',
                'verbose_name': 'Тип партии',
            },
        ),
    ]
