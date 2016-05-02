# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('refer', '0016_auto_20160404_1200'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consumer',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('accessability', models.BooleanField(verbose_name='Доступно', default=False)),
                ('comment', models.TextField(verbose_name='Примечание', max_length=1000, blank=True)),
                ('created', models.DateTimeField(verbose_name='Создано', db_index=True, auto_now_add=True)),
                ('modifyed', models.DateTimeField(verbose_name='Изменено', db_index=True, auto_now=True)),
                ('name', models.CharField(verbose_name='Название', max_length=100, validators=[django.core.validators.RegexValidator(message='Текст не должен начинаться пробелом', regex='^\\S+'), django.core.validators.RegexValidator(message='Текст не должен оканчиваться пробелом', regex='\\S+$')], unique=True)),
                ('order', models.FloatField(verbose_name='Порядок', default=0)),
                ('bases', models.ManyToManyField(verbose_name='Обоснование', blank=True, to='refer.Base')),
            ],
            options={
                'verbose_name': 'Получатель',
                'verbose_name_plural': 'Получатели',
            },
        ),
        migrations.CreateModel(
            name='TypeConsumer',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('accessability', models.BooleanField(verbose_name='Доступно', default=False)),
                ('comment', models.TextField(verbose_name='Примечание', max_length=1000, blank=True)),
                ('created', models.DateTimeField(verbose_name='Создано', db_index=True, auto_now_add=True)),
                ('modifyed', models.DateTimeField(verbose_name='Изменено', db_index=True, auto_now=True)),
                ('name', models.CharField(verbose_name='Название', max_length=100, validators=[django.core.validators.RegexValidator(message='Текст не должен начинаться пробелом', regex='^\\S+'), django.core.validators.RegexValidator(message='Текст не должен оканчиваться пробелом', regex='\\S+$')], unique=True)),
                ('order', models.FloatField(verbose_name='Порядок', default=0)),
                ('code', models.SlugField(verbose_name='Код', unique=True)),
            ],
            options={
                'verbose_name': 'Тип получателя',
                'verbose_name_plural': 'Типы получателей',
            },
        ),
        migrations.AddField(
            model_name='consumer',
            name='type',
            field=models.ForeignKey(verbose_name='Тип', blank=True, on_delete=django.db.models.deletion.PROTECT, to='refer.TypeConsumer', null=True),
        ),
    ]
