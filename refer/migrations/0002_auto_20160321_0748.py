# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('refer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypesBase',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название', unique=True)),
                ('accessability', models.BooleanField(verbose_name='Доступность', default=False)),
                ('comment', models.TextField(max_length=1000, verbose_name='Примечание', blank=True)),
                ('code', models.SlugField(verbose_name='Код', unique=True)),
                ('order', models.FloatField(verbose_name='Порядок', unique=True, default=0)),
                ('created', models.DateTimeField(db_index=True, verbose_name='Создано', auto_now_add=True)),
                ('modifyed', models.DateTimeField(db_index=True, verbose_name='Изменено', auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Типы обоснований',
                'verbose_name': 'Тип обоснования',
            },
        ),
        migrations.AlterField(
            model_name='typesinput',
            name='comment',
            field=models.TextField(max_length=1000, verbose_name='Примечание', blank=True),
        ),
        migrations.AlterField(
            model_name='typesinput',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название', unique=True),
        ),
    ]
