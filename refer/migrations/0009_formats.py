# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('refer', '0008_auto_20160331_1123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formats',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(validators=[django.core.validators.RegexValidator(message='Текст не должен начинаться пробелом', regex='^\\S+'), django.core.validators.RegexValidator(message='Текст не должен оканчиваться пробелом', regex='\\S+$')], verbose_name='Название', unique=True, max_length=100)),
                ('accessability', models.BooleanField(verbose_name='Доступно', default=False)),
                ('comment', models.TextField(verbose_name='Примечание', blank=True, max_length=1000)),
                ('order', models.FloatField(verbose_name='Порядок', default=0)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Создано')),
                ('modifyed', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Изменено')),
                ('precision', models.SmallIntegerField(validators=[django.core.validators.MaxValueValidator(6), django.core.validators.MinValueValidator(-6)], verbose_name='Точность', default=0)),
                ('design', models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.PROTECT, verbose_name='Форма', to='refer.Designs')),
                ('packing', models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.PROTECT, verbose_name='Фасовка', to='refer.Packings')),
                ('unit', models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.PROTECT, verbose_name='Единица', to='refer.Units')),
            ],
            options={
                'verbose_name': 'Формат',
                'verbose_name_plural': 'Форматы',
            },
        ),
    ]
