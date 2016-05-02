# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('refer', '0018_typeissue'),
        ('rest', '0003_auto_20160415_1854'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(verbose_name='Создано', auto_now_add=True, db_index=True)),
                ('modifyed', models.DateTimeField(verbose_name='Изменено', auto_now=True, db_index=True)),
                ('precision', models.SmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(6), django.core.validators.MinValueValidator(-6)], verbose_name='Точность')),
                ('rest_total', models.DecimalField(default=0, decimal_places=6, verbose_name='Итоговый остаток', max_digits=20)),
                ('design', models.ForeignKey(to='refer.Design', on_delete=django.db.models.deletion.PROTECT, null=True, verbose_name='Форма', blank=True)),
                ('item', models.ForeignKey(to='refer.Item', on_delete=django.db.models.deletion.PROTECT, verbose_name='Медсредство', null=True)),
                ('packing', models.ForeignKey(to='refer.Packing', on_delete=django.db.models.deletion.PROTECT, verbose_name='Фасовка', null=True)),
                ('part', models.ForeignKey(to='refer.Part', on_delete=django.db.models.deletion.PROTECT, null=True, verbose_name='Партия', blank=True)),
                ('period', models.ForeignKey(to='rest.Period', on_delete=django.db.models.deletion.PROTECT, verbose_name='Период', null=True)),
                ('store', models.ForeignKey(to='refer.Store', on_delete=django.db.models.deletion.PROTECT, null=True, verbose_name='Хранилище', blank=True)),
                ('target', models.ForeignKey(to='refer.Target', on_delete=django.db.models.deletion.PROTECT, null=True, verbose_name='Цель', blank=True)),
                ('unit', models.ForeignKey(to='refer.Unit', on_delete=django.db.models.deletion.PROTECT, verbose_name='Единица', null=True)),
            ],
            options={
                'ordering': ['item'],
                'verbose_name_plural': 'Остатки',
                'verbose_name': 'Остаток',
            },
        ),
    ]
