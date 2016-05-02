# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import django.db.models.deletion
import expense.models


class Migration(migrations.Migration):

    dependencies = [
        ('refer', '0018_typeissue'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('accessability', models.BooleanField(verbose_name='Доступно', default=False)),
                ('comment', models.TextField(verbose_name='Примечание', blank=True, max_length=1000)),
                ('created', models.DateTimeField(db_index=True, auto_now_add=True, verbose_name='Создано')),
                ('modifyed', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Изменено')),
                ('date', models.DateField(verbose_name='Дата')),
                ('name', models.CharField(verbose_name='Название', validators=[django.core.validators.RegexValidator(regex='^\\S+', message='Текст не должен начинаться пробелом'), django.core.validators.RegexValidator(regex='\\S+$', message='Текст не должен оканчиваться пробелом')], unique_for_date='date', max_length=100)),
                ('executed', models.BooleanField(verbose_name='Исполнено', default=False)),
                ('bases', models.ManyToManyField(verbose_name='Обоснование', blank=True, to='refer.Base')),
                ('consumer', models.ForeignKey(verbose_name='Получатель', blank=True, on_delete=django.db.models.deletion.PROTECT, to='refer.Consumer', null=True)),
                ('store', models.ForeignKey(verbose_name='Хранилище', blank=True, on_delete=django.db.models.deletion.PROTECT, to='refer.Store', null=True)),
                ('target', models.ForeignKey(verbose_name='Цель', blank=True, on_delete=django.db.models.deletion.PROTECT, to='refer.Target', null=True)),
                ('type', models.ForeignKey(verbose_name='Тип', blank=True, on_delete=django.db.models.deletion.PROTECT, to='refer.TypeIssue', null=True)),
            ],
            options={
                'verbose_name': 'Выдача',
                'verbose_name_plural': 'Выдачи',
                'ordering': ['-date', 'name'],
            },
        ),
        migrations.CreateModel(
            name='PositionExp',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('number', models.CharField(verbose_name='Номер', validators=[django.core.validators.RegexValidator(regex='^\\S+', message='Текст не должен начинаться пробелом'), django.core.validators.RegexValidator(regex='\\S+$', message='Текст не должен оканчиваться пробелом')], max_length=100)),
                ('accessability', models.BooleanField(verbose_name='Доступно', default=True)),
                ('created', models.DateTimeField(db_index=True, auto_now_add=True, verbose_name='Создано')),
                ('modifyed', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Изменено')),
                ('precision', models.SmallIntegerField(verbose_name='Точность', validators=[django.core.validators.MaxValueValidator(6), django.core.validators.MinValueValidator(-6)], default=0)),
                ('quantity', models.DecimalField(max_digits=20, verbose_name='Количество', decimal_places=6, default=0)),
                ('design', models.ForeignKey(verbose_name='Форма', blank=True, on_delete=django.db.models.deletion.PROTECT, to='refer.Design', null=True)),
                ('issue', models.ForeignKey(verbose_name='Выдача', on_delete=django.db.models.deletion.PROTECT, to='expense.Issue', null=True)),
                ('item', models.ForeignKey(verbose_name='Медсредство', on_delete=django.db.models.deletion.PROTECT, to='refer.Item', null=True)),
                ('packing', models.ForeignKey(verbose_name='Фасовка', on_delete=django.db.models.deletion.PROTECT, to='refer.Packing', null=True)),
                ('part', models.ForeignKey(verbose_name='Партия', blank=True, on_delete=django.db.models.deletion.PROTECT, to='refer.Part', null=True)),
                ('unit', models.ForeignKey(verbose_name='Единица', on_delete=django.db.models.deletion.PROTECT, to='refer.Unit', null=True)),
            ],
            options={
                'verbose_name': 'Позиция выдачи',
                'verbose_name_plural': 'Позиции выдач',
                'ordering': ['number'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='positionexp',
            unique_together=set([('issue', 'number')]),
        ),
    ]
