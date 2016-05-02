# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('refer', '0009_formats'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Название', validators=[django.core.validators.RegexValidator(regex='^\\S+', message='Текст не должен начинаться пробелом'), django.core.validators.RegexValidator(regex='\\S+$', message='Текст не должен оканчиваться пробелом')], unique=True)),
                ('accessability', models.BooleanField(default=False, verbose_name='Доступно')),
                ('comment', models.TextField(max_length=1000, verbose_name='Примечание', blank=True)),
                ('order', models.FloatField(default=0, verbose_name='Порядок')),
                ('created', models.DateTimeField(verbose_name='Создано', auto_now_add=True, db_index=True)),
                ('modifyed', models.DateTimeField(verbose_name='Изменено', auto_now=True, db_index=True)),
                ('bases', models.ManyToManyField(to='refer.Bases', verbose_name='Обоснования', blank=True)),
                ('formats', models.ManyToManyField(to='refer.Formats', verbose_name='Форматы', blank=True)),
            ],
            options={
                'verbose_name': 'Медсредство',
                'verbose_name_plural': 'Медсредства',
            },
        ),
        migrations.CreateModel(
            name='TypesItem',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Название', validators=[django.core.validators.RegexValidator(regex='^\\S+', message='Текст не должен начинаться пробелом'), django.core.validators.RegexValidator(regex='\\S+$', message='Текст не должен оканчиваться пробелом')], unique=True)),
                ('accessability', models.BooleanField(default=False, verbose_name='Доступно')),
                ('comment', models.TextField(max_length=1000, verbose_name='Примечание', blank=True)),
                ('order', models.FloatField(default=0, verbose_name='Порядок')),
                ('created', models.DateTimeField(verbose_name='Создано', auto_now_add=True, db_index=True)),
                ('modifyed', models.DateTimeField(verbose_name='Изменено', auto_now=True, db_index=True)),
                ('code', models.SlugField(verbose_name='Код', unique=True)),
            ],
            options={
                'verbose_name': 'Тип медсредства',
                'verbose_name_plural': 'Типы медсредств',
            },
        ),
        migrations.AddField(
            model_name='items',
            name='type',
            field=models.ForeignKey(verbose_name='Тип', blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='refer.TypesItem'),
        ),
    ]
