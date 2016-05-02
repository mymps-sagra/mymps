# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('refer', '0016_auto_20160404_1200'),
    ]

    operations = [
        migrations.CreateModel(
            name='TotalPeriod',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('accessability', models.BooleanField(verbose_name='Доступно', default=False)),
                ('comment', models.TextField(max_length=1000, verbose_name='Примечание', blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Создано')),
                ('modifyed', models.DateTimeField(db_index=True, verbose_name='Изменено', auto_now=True)),
                ('date', models.DateField(verbose_name='Дата')),
                ('name', models.CharField(max_length=100, verbose_name='Название', unique_for_date='date', validators=[django.core.validators.RegexValidator(message='Текст не должен начинаться пробелом', regex='^\\S+'), django.core.validators.RegexValidator(message='Текст не должен оканчиваться пробелом', regex='\\S+$')])),
                ('date_from', models.DateField(null=True, verbose_name='С даты', blank=True)),
                ('date_to', models.DateField(null=True, verbose_name='По дату', blank=True)),
                ('executed', models.BooleanField(verbose_name='Исполнено', default=False)),
                ('stores', models.ManyToManyField(verbose_name='Хранилища', to='refer.Store', blank=True)),
                ('targets', models.ManyToManyField(verbose_name='Цели', to='refer.Target', blank=True)),
            ],
            options={
                'verbose_name': 'Итог периода',
                'verbose_name_plural': 'Итоги периодов',
                'ordering': ['-date', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Turnover',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Создано')),
                ('modifyed', models.DateTimeField(db_index=True, verbose_name='Изменено', auto_now=True)),
                ('precision', models.SmallIntegerField(validators=[django.core.validators.MaxValueValidator(6), django.core.validators.MinValueValidator(-6)], verbose_name='Точность', default=0)),
                ('rest_init', models.DecimalField(decimal_places=6, verbose_name='Входящий остаток', default=0, max_digits=20)),
                ('quantity_in', models.DecimalField(decimal_places=6, verbose_name='Поставлено', default=0, max_digits=20)),
                ('quantity_out', models.DecimalField(decimal_places=6, verbose_name='Отпущено', default=0, max_digits=20)),
                ('rest_total', models.DecimalField(decimal_places=6, verbose_name='Итоговый остаток', default=0, max_digits=20)),
                ('design', models.ForeignKey(verbose_name='Форма', blank=True, on_delete=django.db.models.deletion.PROTECT, null=True, to='refer.Design')),
                ('item', models.ForeignKey(verbose_name='Медсредство', on_delete=django.db.models.deletion.PROTECT, null=True, to='refer.Item')),
                ('packing', models.ForeignKey(verbose_name='Фасовка', on_delete=django.db.models.deletion.PROTECT, null=True, to='refer.Packing')),
                ('part', models.ForeignKey(verbose_name='Партия', blank=True, on_delete=django.db.models.deletion.PROTECT, null=True, to='refer.Part')),
                ('store', models.ForeignKey(verbose_name='Хранилище', blank=True, on_delete=django.db.models.deletion.PROTECT, null=True, to='refer.Store')),
                ('target', models.ForeignKey(verbose_name='Цель', blank=True, on_delete=django.db.models.deletion.PROTECT, null=True, to='refer.Target')),
                ('total_period', models.ForeignKey(verbose_name='Итог периода', on_delete=django.db.models.deletion.PROTECT, null=True, to='rest.TotalPeriod')),
                ('unit', models.ForeignKey(verbose_name='Единица', on_delete=django.db.models.deletion.PROTECT, null=True, to='refer.Unit')),
            ],
            options={
                'verbose_name': 'Оборот',
                'verbose_name_plural': 'Обороты',
                'ordering': ['item'],
            },
        ),
    ]
