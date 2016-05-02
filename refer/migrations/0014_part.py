# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('refer', '0013_typepart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(validators=[django.core.validators.RegexValidator(regex='^\\S+', message='Текст не должен начинаться пробелом'), django.core.validators.RegexValidator(regex='\\S+$', message='Текст не должен оканчиваться пробелом')], unique=True, max_length=100, verbose_name='Название')),
                ('accessability', models.BooleanField(default=False, verbose_name='Доступно')),
                ('comment', models.TextField(max_length=1000, verbose_name='Примечание', blank=True)),
                ('order', models.FloatField(default=0, verbose_name='Порядок')),
                ('created', models.DateTimeField(db_index=True, auto_now_add=True, verbose_name='Создано')),
                ('modifyed', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Изменено')),
                ('date_from', models.DateField(blank=True, verbose_name='С даты', null=True)),
                ('date_to', models.DateField(blank=True, verbose_name='По дату', null=True)),
                ('bases', models.ManyToManyField(to='refer.Base', verbose_name='Обоснования', blank=True)),
                ('manufacturer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='refer.Manufacturer', verbose_name='Производитель', blank=True)),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='refer.TypePart', verbose_name='Тип', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Партии',
                'verbose_name': 'Партия',
            },
        ),
    ]
