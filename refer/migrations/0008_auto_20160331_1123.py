# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('refer', '0007_auto_20160330_2118'),
    ]

    operations = [
        migrations.CreateModel(
            name='Designs',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название', validators=[django.core.validators.RegexValidator(regex='^\\S+', message='Текст не должен начинаться пробелом'), django.core.validators.RegexValidator(regex='\\S+$', message='Текст не должен оканчиваться пробелом')])),
                ('accessability', models.BooleanField(default=False, verbose_name='Доступно')),
                ('comment', models.TextField(max_length=1000, blank=True, verbose_name='Примечание')),
                ('order', models.FloatField(default=0, verbose_name='Порядок')),
                ('created', models.DateTimeField(db_index=True, verbose_name='Создано', auto_now_add=True)),
                ('modifyed', models.DateTimeField(db_index=True, auto_now=True, verbose_name='Изменено')),
                ('bases', models.ManyToManyField(blank=True, verbose_name='Обоснования', to='refer.Bases')),
            ],
            options={
                'verbose_name_plural': 'Формы',
                'verbose_name': 'Форма',
            },
        ),
        migrations.CreateModel(
            name='Packings',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название', validators=[django.core.validators.RegexValidator(regex='^\\S+', message='Текст не должен начинаться пробелом'), django.core.validators.RegexValidator(regex='\\S+$', message='Текст не должен оканчиваться пробелом')])),
                ('accessability', models.BooleanField(default=False, verbose_name='Доступно')),
                ('comment', models.TextField(max_length=1000, blank=True, verbose_name='Примечание')),
                ('order', models.FloatField(default=0, verbose_name='Порядок')),
                ('created', models.DateTimeField(db_index=True, verbose_name='Создано', auto_now_add=True)),
                ('modifyed', models.DateTimeField(db_index=True, auto_now=True, verbose_name='Изменено')),
                ('bases', models.ManyToManyField(blank=True, verbose_name='Обоснования', to='refer.Bases')),
            ],
            options={
                'verbose_name_plural': 'Фасовки',
                'verbose_name': 'Фасовка',
            },
        ),
        migrations.CreateModel(
            name='TypesDesign',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название', validators=[django.core.validators.RegexValidator(regex='^\\S+', message='Текст не должен начинаться пробелом'), django.core.validators.RegexValidator(regex='\\S+$', message='Текст не должен оканчиваться пробелом')])),
                ('accessability', models.BooleanField(default=False, verbose_name='Доступно')),
                ('comment', models.TextField(max_length=1000, blank=True, verbose_name='Примечание')),
                ('order', models.FloatField(default=0, verbose_name='Порядок')),
                ('created', models.DateTimeField(db_index=True, verbose_name='Создано', auto_now_add=True)),
                ('modifyed', models.DateTimeField(db_index=True, auto_now=True, verbose_name='Изменено')),
                ('code', models.SlugField(unique=True, verbose_name='Код')),
            ],
            options={
                'verbose_name_plural': 'Типы форм',
                'verbose_name': 'Тип формы',
            },
        ),
        migrations.CreateModel(
            name='TypesPacking',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название', validators=[django.core.validators.RegexValidator(regex='^\\S+', message='Текст не должен начинаться пробелом'), django.core.validators.RegexValidator(regex='\\S+$', message='Текст не должен оканчиваться пробелом')])),
                ('accessability', models.BooleanField(default=False, verbose_name='Доступно')),
                ('comment', models.TextField(max_length=1000, blank=True, verbose_name='Примечание')),
                ('order', models.FloatField(default=0, verbose_name='Порядок')),
                ('created', models.DateTimeField(db_index=True, verbose_name='Создано', auto_now_add=True)),
                ('modifyed', models.DateTimeField(db_index=True, auto_now=True, verbose_name='Изменено')),
                ('code', models.SlugField(unique=True, verbose_name='Код')),
            ],
            options={
                'verbose_name_plural': 'Типы фасовок',
                'verbose_name': 'Тип фасовки',
            },
        ),
        migrations.CreateModel(
            name='TypesUnit',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название', validators=[django.core.validators.RegexValidator(regex='^\\S+', message='Текст не должен начинаться пробелом'), django.core.validators.RegexValidator(regex='\\S+$', message='Текст не должен оканчиваться пробелом')])),
                ('accessability', models.BooleanField(default=False, verbose_name='Доступно')),
                ('comment', models.TextField(max_length=1000, blank=True, verbose_name='Примечание')),
                ('order', models.FloatField(default=0, verbose_name='Порядок')),
                ('created', models.DateTimeField(db_index=True, verbose_name='Создано', auto_now_add=True)),
                ('modifyed', models.DateTimeField(db_index=True, auto_now=True, verbose_name='Изменено')),
                ('code', models.SlugField(unique=True, verbose_name='Код')),
            ],
            options={
                'verbose_name_plural': 'Типы единиц',
                'verbose_name': 'Тип единицы',
            },
        ),
        migrations.CreateModel(
            name='Units',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название', validators=[django.core.validators.RegexValidator(regex='^\\S+', message='Текст не должен начинаться пробелом'), django.core.validators.RegexValidator(regex='\\S+$', message='Текст не должен оканчиваться пробелом')])),
                ('accessability', models.BooleanField(default=False, verbose_name='Доступно')),
                ('comment', models.TextField(max_length=1000, blank=True, verbose_name='Примечание')),
                ('order', models.FloatField(default=0, verbose_name='Порядок')),
                ('created', models.DateTimeField(db_index=True, verbose_name='Создано', auto_now_add=True)),
                ('modifyed', models.DateTimeField(db_index=True, auto_now=True, verbose_name='Изменено')),
                ('bases', models.ManyToManyField(blank=True, verbose_name='Обоснования', to='refer.Bases')),
                ('type', models.ForeignKey(verbose_name='Тип', to='refer.TypesUnit', on_delete=django.db.models.deletion.PROTECT, null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Единицы',
                'verbose_name': 'Единица',
            },
        ),
        migrations.AddField(
            model_name='packings',
            name='type',
            field=models.ForeignKey(verbose_name='Тип', to='refer.TypesPacking', on_delete=django.db.models.deletion.PROTECT, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='designs',
            name='type',
            field=models.ForeignKey(verbose_name='Тип', to='refer.TypesDesign', on_delete=django.db.models.deletion.PROTECT, null=True, blank=True),
        ),
    ]
