# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import django.core.validators
import common.models


class Migration(migrations.Migration):

    dependencies = [
        ('refer', '0018_typeissue'),
        ('income', '0006_auto_20160418_1224'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position_delivery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('number', models.CharField(validators=[django.core.validators.RegexValidator(regex='^\\S+', message='Текст не должен начинаться пробелом'), django.core.validators.RegexValidator(regex='\\S+$', message='Текст не должен оканчиваться пробелом')], verbose_name='Номер', max_length=100)),
                ('accessability', models.BooleanField(default=True, verbose_name='Доступно')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Создано')),
                ('modifyed', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Изменено')),
                ('precision', models.SmallIntegerField(default=0, verbose_name='Точность', validators=[django.core.validators.MaxValueValidator(6), django.core.validators.MinValueValidator(-6)])),
                ('quantity', models.DecimalField(max_digits=20, default=0, verbose_name='Количество', decimal_places=6, validators=[common.models.CommonPositionModel.clean_quantity])),
                ('delivery', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='income.Delivery', null=True, verbose_name='Поставка')),
                ('design', models.ForeignKey(to='refer.Design', on_delete=django.db.models.deletion.PROTECT, blank=True, null=True, verbose_name='Форма')),
                ('format', models.ForeignKey(to='refer.Format', on_delete=django.db.models.deletion.PROTECT, blank=True, null=True, verbose_name='Формат')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='refer.Item', null=True, verbose_name='Медсредство')),
                ('packing', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='refer.Packing', null=True, verbose_name='Фасовка')),
                ('part', models.ForeignKey(to='refer.Part', on_delete=django.db.models.deletion.PROTECT, blank=True, null=True, verbose_name='Партия')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='refer.Unit', null=True, verbose_name='Единица')),
            ],
            options={
                'verbose_name_plural': 'Позиции поставок',
                'ordering': ['number'],
                'verbose_name': 'Позиция поставки',
            },
        ),
        migrations.AlterUniqueTogether(
            name='position',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='position',
            name='delivery',
        ),
        migrations.RemoveField(
            model_name='position',
            name='design',
        ),
        migrations.RemoveField(
            model_name='position',
            name='format',
        ),
        migrations.RemoveField(
            model_name='position',
            name='item',
        ),
        migrations.RemoveField(
            model_name='position',
            name='packing',
        ),
        migrations.RemoveField(
            model_name='position',
            name='part',
        ),
        migrations.RemoveField(
            model_name='position',
            name='unit',
        ),
        migrations.DeleteModel(
            name='Position',
        ),
        migrations.AlterUniqueTogether(
            name='position_delivery',
            unique_together=set([('delivery', 'number')]),
        ),
    ]
