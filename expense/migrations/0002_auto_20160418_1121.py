# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import common.models
import django.core.validators
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('refer', '0018_typeissue'),
        ('expense', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position_issue',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('number', models.CharField(validators=[django.core.validators.RegexValidator(message='Текст не должен начинаться пробелом', regex='^\\S+'), django.core.validators.RegexValidator(message='Текст не должен оканчиваться пробелом', regex='\\S+$')], verbose_name='Номер', max_length=100)),
                ('accessability', models.BooleanField(verbose_name='Доступно', default=True)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Создано')),
                ('modifyed', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Изменено')),
                ('precision', models.SmallIntegerField(validators=[django.core.validators.MaxValueValidator(6), django.core.validators.MinValueValidator(-6)], verbose_name='Точность', default=0)),
                ('quantity', models.DecimalField(validators=[common.models.CommonPositionModel.clean_quantity], decimal_places=6, max_digits=20, verbose_name='Количество', default=0)),
                ('design', models.ForeignKey(null=True, blank=True, to='refer.Design', verbose_name='Форма', on_delete=django.db.models.deletion.PROTECT)),
                ('issue', models.ForeignKey(null=True, to='expense.Issue', verbose_name='Выдача', on_delete=django.db.models.deletion.PROTECT)),
                ('item', models.ForeignKey(null=True, to='refer.Item', verbose_name='Медсредство', on_delete=django.db.models.deletion.PROTECT)),
                ('packing', models.ForeignKey(null=True, to='refer.Packing', verbose_name='Фасовка', on_delete=django.db.models.deletion.PROTECT)),
                ('part', models.ForeignKey(null=True, blank=True, to='refer.Part', verbose_name='Партия', on_delete=django.db.models.deletion.PROTECT)),
                ('unit', models.ForeignKey(null=True, to='refer.Unit', verbose_name='Единица', on_delete=django.db.models.deletion.PROTECT)),
            ],
            options={
                'verbose_name_plural': 'Позиции выдач',
                'ordering': ['number'],
                'verbose_name': 'Позиция выдачи',
            },
        ),
        migrations.AlterUniqueTogether(
            name='position_issue',
            unique_together=set([('issue', 'number')]),
        ),
    ]
