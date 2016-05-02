# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('refer', '0010_auto_20160331_1545'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturers',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, validators=[django.core.validators.RegexValidator(message='Текст не должен начинаться пробелом', regex='^\\S+'), django.core.validators.RegexValidator(message='Текст не должен оканчиваться пробелом', regex='\\S+$')], verbose_name='Название')),
                ('accessability', models.BooleanField(default=False, verbose_name='Доступно')),
                ('comment', models.TextField(max_length=1000, blank=True, verbose_name='Примечание')),
                ('order', models.FloatField(default=0, verbose_name='Порядок')),
                ('created', models.DateTimeField(db_index=True, verbose_name='Создано', auto_now_add=True)),
                ('modifyed', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Изменено')),
                ('bases', models.ManyToManyField(to='refer.Bases', blank=True, verbose_name='Обоснования')),
            ],
            options={
                'verbose_name_plural': 'Производители',
                'verbose_name': 'Производитель',
            },
        ),
        migrations.CreateModel(
            name='Stores',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, validators=[django.core.validators.RegexValidator(message='Текст не должен начинаться пробелом', regex='^\\S+'), django.core.validators.RegexValidator(message='Текст не должен оканчиваться пробелом', regex='\\S+$')], verbose_name='Название')),
                ('accessability', models.BooleanField(default=False, verbose_name='Доступно')),
                ('comment', models.TextField(max_length=1000, blank=True, verbose_name='Примечание')),
                ('order', models.FloatField(default=0, verbose_name='Порядок')),
                ('created', models.DateTimeField(db_index=True, verbose_name='Создано', auto_now_add=True)),
                ('modifyed', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Изменено')),
                ('bases', models.ManyToManyField(to='refer.Bases', blank=True, verbose_name='Обоснования')),
            ],
            options={
                'verbose_name_plural': 'Хранилища',
                'verbose_name': 'Хранилище',
            },
        ),
        migrations.CreateModel(
            name='Targets',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, validators=[django.core.validators.RegexValidator(message='Текст не должен начинаться пробелом', regex='^\\S+'), django.core.validators.RegexValidator(message='Текст не должен оканчиваться пробелом', regex='\\S+$')], verbose_name='Название')),
                ('accessability', models.BooleanField(default=False, verbose_name='Доступно')),
                ('comment', models.TextField(max_length=1000, blank=True, verbose_name='Примечание')),
                ('order', models.FloatField(default=0, verbose_name='Порядок')),
                ('created', models.DateTimeField(db_index=True, verbose_name='Создано', auto_now_add=True)),
                ('modifyed', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Изменено')),
                ('bases', models.ManyToManyField(to='refer.Bases', blank=True, verbose_name='Обоснования')),
            ],
            options={
                'verbose_name_plural': 'Цели',
                'verbose_name': 'Цель',
            },
        ),
        migrations.CreateModel(
            name='TypesManufacturer',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, validators=[django.core.validators.RegexValidator(message='Текст не должен начинаться пробелом', regex='^\\S+'), django.core.validators.RegexValidator(message='Текст не должен оканчиваться пробелом', regex='\\S+$')], verbose_name='Название')),
                ('accessability', models.BooleanField(default=False, verbose_name='Доступно')),
                ('comment', models.TextField(max_length=1000, blank=True, verbose_name='Примечание')),
                ('order', models.FloatField(default=0, verbose_name='Порядок')),
                ('created', models.DateTimeField(db_index=True, verbose_name='Создано', auto_now_add=True)),
                ('modifyed', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Изменено')),
                ('code', models.SlugField(unique=True, verbose_name='Код')),
            ],
            options={
                'verbose_name_plural': 'Типы изготовителей',
                'verbose_name': 'Тип изготовителя',
            },
        ),
        migrations.CreateModel(
            name='TypesStore',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, validators=[django.core.validators.RegexValidator(message='Текст не должен начинаться пробелом', regex='^\\S+'), django.core.validators.RegexValidator(message='Текст не должен оканчиваться пробелом', regex='\\S+$')], verbose_name='Название')),
                ('accessability', models.BooleanField(default=False, verbose_name='Доступно')),
                ('comment', models.TextField(max_length=1000, blank=True, verbose_name='Примечание')),
                ('order', models.FloatField(default=0, verbose_name='Порядок')),
                ('created', models.DateTimeField(db_index=True, verbose_name='Создано', auto_now_add=True)),
                ('modifyed', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Изменено')),
                ('code', models.SlugField(unique=True, verbose_name='Код')),
            ],
            options={
                'verbose_name_plural': 'Типы хранилищ',
                'verbose_name': 'Тип хранилища',
            },
        ),
        migrations.CreateModel(
            name='TypesTarget',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, validators=[django.core.validators.RegexValidator(message='Текст не должен начинаться пробелом', regex='^\\S+'), django.core.validators.RegexValidator(message='Текст не должен оканчиваться пробелом', regex='\\S+$')], verbose_name='Название')),
                ('accessability', models.BooleanField(default=False, verbose_name='Доступно')),
                ('comment', models.TextField(max_length=1000, blank=True, verbose_name='Примечание')),
                ('order', models.FloatField(default=0, verbose_name='Порядок')),
                ('created', models.DateTimeField(db_index=True, verbose_name='Создано', auto_now_add=True)),
                ('modifyed', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Изменено')),
                ('code', models.SlugField(unique=True, verbose_name='Код')),
            ],
            options={
                'verbose_name_plural': 'Типы целей',
                'verbose_name': 'Тип цели',
            },
        ),
        migrations.AddField(
            model_name='targets',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Тип', null=True, blank=True, to='refer.TypesTarget'),
        ),
        migrations.AddField(
            model_name='stores',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Тип', null=True, blank=True, to='refer.TypesStore'),
        ),
        migrations.AddField(
            model_name='manufacturers',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Тип', null=True, blank=True, to='refer.TypesManufacturer'),
        ),
    ]
