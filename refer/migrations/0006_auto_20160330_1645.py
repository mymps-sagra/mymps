# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('refer', '0005_auto_20160324_1544'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Название', unique=True, max_length=100, validators=[django.core.validators.RegexValidator(message='Текст не должен начинаться пробелом', regex='^\\S+'), django.core.validators.RegexValidator(message='Текст не должен оканчиваться пробелом', regex='\\S+$')])),
                ('accessability', models.BooleanField(verbose_name='Доступно', default=False)),
                ('comment', models.TextField(blank=True, verbose_name='Примечание', max_length=1000)),
                ('order', models.FloatField(verbose_name='Порядок', default=0)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано', db_index=True)),
                ('modifyed', models.DateTimeField(verbose_name='Изменено', auto_now=True, db_index=True)),
                ('bases', models.ManyToManyField(blank=True, verbose_name='Обоснования', to='refer.Bases')),
            ],
            options={
                'verbose_name': 'Поставщик',
                'verbose_name_plural': 'Поставщики',
            },
        ),
        migrations.CreateModel(
            name='TypesSupplier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Название', unique=True, max_length=100, validators=[django.core.validators.RegexValidator(message='Текст не должен начинаться пробелом', regex='^\\S+'), django.core.validators.RegexValidator(message='Текст не должен оканчиваться пробелом', regex='\\S+$')])),
                ('accessability', models.BooleanField(verbose_name='Доступно', default=False)),
                ('comment', models.TextField(blank=True, verbose_name='Примечание', max_length=1000)),
                ('order', models.FloatField(verbose_name='Порядок', default=0)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано', db_index=True)),
                ('modifyed', models.DateTimeField(verbose_name='Изменено', auto_now=True, db_index=True)),
                ('code', models.SlugField(verbose_name='Код', unique=True)),
            ],
            options={
                'verbose_name': 'Тип поставшика',
                'verbose_name_plural': 'Типы поставщиков',
            },
        ),
        migrations.AddField(
            model_name='suppliers',
            name='type',
            field=models.ForeignKey(blank=True, to='refer.TypesSupplier', null=True, on_delete=django.db.models.deletion.PROTECT, verbose_name='Тип'),
        ),
    ]
