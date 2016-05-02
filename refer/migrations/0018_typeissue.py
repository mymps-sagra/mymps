# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('refer', '0017_auto_20160415_2130'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeIssue',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('accessability', models.BooleanField(verbose_name='Доступно', default=False)),
                ('comment', models.TextField(verbose_name='Примечание', blank=True, max_length=1000)),
                ('created', models.DateTimeField(db_index=True, auto_now_add=True, verbose_name='Создано')),
                ('modifyed', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Изменено')),
                ('name', models.CharField(verbose_name='Название', validators=[django.core.validators.RegexValidator(regex='^\\S+', message='Текст не должен начинаться пробелом'), django.core.validators.RegexValidator(regex='\\S+$', message='Текст не должен оканчиваться пробелом')], unique=True, max_length=100)),
                ('order', models.FloatField(verbose_name='Порядок', default=0)),
                ('code', models.SlugField(verbose_name='Код', unique=True)),
            ],
            options={
                'verbose_name': 'Тип выдачи',
                'verbose_name_plural': 'Типы выдач',
            },
        ),
    ]
