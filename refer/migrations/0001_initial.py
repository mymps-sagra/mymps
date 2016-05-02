# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TypesInput',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, verbose_name='Наименование', max_length=100)),
                ('accessability', models.BooleanField(default=False, verbose_name='Доступность')),
                ('comment', models.TextField(verbose_name='Примечание', max_length=1000)),
                ('code', models.SlugField(unique=True, verbose_name='Код')),
                ('order', models.FloatField(default=0, unique=True, verbose_name='Порядок')),
                ('created', models.DateTimeField(verbose_name='Создано', auto_now_add=True, db_index=True)),
                ('modifyed', models.DateTimeField(auto_now=True, verbose_name='Изменено', db_index=True)),
            ],
            options={
                'verbose_name': 'Тип поставки',
                'verbose_name_plural': 'Типы поставок',
                'ordering': ['order'],
            },
        ),
    ]
