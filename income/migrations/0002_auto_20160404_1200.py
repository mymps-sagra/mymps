# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('refer', '0016_auto_20160404_1200'),
        ('income', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(verbose_name='Номер', validators=[django.core.validators.RegexValidator(regex='^\\S+', message='Текст не должен начинаться пробелом'), django.core.validators.RegexValidator(regex='\\S+$', message='Текст не должен оканчиваться пробелом')], max_length=100, unique=True)),
                ('accessability', models.BooleanField(verbose_name='Доступно', default=True)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Создано')),
                ('modifyed', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Изменено')),
                ('precision', models.SmallIntegerField(verbose_name='Точность', validators=[django.core.validators.MaxValueValidator(6), django.core.validators.MinValueValidator(-6)], default=0)),
                ('quantity', models.DecimalField(max_digits=20, verbose_name='Количество', validators=[django.core.validators.MinValueValidator(0)], decimal_places=6, default=0)),
            ],
            options={
                'verbose_name': 'Позиция',
                'verbose_name_plural': 'Позиции',
                'ordering': ['number'],
            },
        ),
        migrations.AlterModelOptions(
            name='delivery',
            options={'verbose_name': 'Поставка', 'verbose_name_plural': 'Поставки', 'ordering': ['-date', 'name']},
        ),
        migrations.AlterField(
            model_name='delivery',
            name='bases',
            field=models.ManyToManyField(verbose_name='Обоснование', blank=True, to='refer.Base'),
        ),
        migrations.AddField(
            model_name='position',
            name='delivery',
            field=models.ForeignKey(to='income.Delivery', null=True, verbose_name='Поставка', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='position',
            name='design',
            field=models.ForeignKey(to='refer.Design', null=True, verbose_name='Форма', blank=True, on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='position',
            name='format',
            field=models.ForeignKey(to='refer.Format', null=True, verbose_name='Формат', blank=True, on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='position',
            name='item',
            field=models.ForeignKey(to='refer.Item', null=True, verbose_name='Медсредство', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='position',
            name='packing',
            field=models.ForeignKey(to='refer.Packing', null=True, verbose_name='Фасовка', blank=True, on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='position',
            name='part',
            field=models.ForeignKey(to='refer.Part', null=True, verbose_name='Партия', blank=True, on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='position',
            name='unit',
            field=models.ForeignKey(to='refer.Unit', null=True, verbose_name='Единица', blank=True, on_delete=django.db.models.deletion.PROTECT),
        ),
    ]
