# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('refer', '0015_auto_20160401_1816'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\S+', message='Текст не должен начинаться пробелом'), django.core.validators.RegexValidator(regex='\\S+$', message='Текст не должен оканчиваться пробелом')], verbose_name='Название')),
                ('accessability', models.BooleanField(default=False, verbose_name='Доступно')),
                ('comment', models.TextField(max_length=1000, verbose_name='Примечание', blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Создано')),
                ('modifyed', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Изменено')),
                ('date', models.DateField(verbose_name='Дата')),
                ('executed', models.BooleanField(default=False, verbose_name='Исполнено')),
                ('bases', models.ManyToManyField(to='refer.Base', verbose_name='Обоснования', blank=True)),
                ('store', models.ForeignKey(to='refer.Store', blank=True, on_delete=django.db.models.deletion.PROTECT, null=True, verbose_name='Хранилище')),
                ('supplier', models.ForeignKey(to='refer.Supplier', blank=True, on_delete=django.db.models.deletion.PROTECT, null=True, verbose_name='Поставщик')),
                ('target', models.ForeignKey(to='refer.Target', blank=True, on_delete=django.db.models.deletion.PROTECT, null=True, verbose_name='Цель')),
                ('type', models.ForeignKey(to='refer.TypeDelivery', blank=True, on_delete=django.db.models.deletion.PROTECT, null=True, verbose_name='Тип')),
            ],
            options={
                'ordering': ['-date', 'name'],
            },
        ),
    ]
