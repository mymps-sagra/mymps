# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('refer', '0014_part'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeDelivery',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(unique=True, validators=[django.core.validators.RegexValidator(regex='^\\S+', message='Текст не должен начинаться пробелом'), django.core.validators.RegexValidator(regex='\\S+$', message='Текст не должен оканчиваться пробелом')], max_length=100, verbose_name='Название')),
                ('accessability', models.BooleanField(default=False, verbose_name='Доступно')),
                ('comment', models.TextField(max_length=1000, blank=True, verbose_name='Примечание')),
                ('created', models.DateTimeField(db_index=True, auto_now_add=True, verbose_name='Создано')),
                ('modifyed', models.DateTimeField(db_index=True, verbose_name='Изменено', auto_now=True)),
                ('order', models.FloatField(default=0, verbose_name='Порядок')),
                ('code', models.SlugField(unique=True, verbose_name='Код')),
            ],
            options={
                'verbose_name': 'Тип поставки',
                'verbose_name_plural': 'Типы поставок',
            },
        ),
        migrations.DeleteModel(
            name='TypeIncome',
        ),
        migrations.AlterModelOptions(
            name='manufacturer',
            options={'verbose_name_plural': 'Изготовители', 'verbose_name': 'Изготовитель'},
        ),
        migrations.AlterField(
            model_name='part',
            name='manufacturer',
            field=models.ForeignKey(null=True, blank=True, verbose_name='Изготовитель', to='refer.Manufacturer', on_delete=django.db.models.deletion.PROTECT),
        ),
    ]
