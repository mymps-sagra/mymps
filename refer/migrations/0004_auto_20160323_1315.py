# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('refer', '0003_auto_20160321_0754'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bases',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Название', unique=True, max_length=100)),
                ('accessability', models.BooleanField(verbose_name='Доступно', default=False)),
                ('comment', models.TextField(verbose_name='Примечание', blank=True, max_length=1000)),
                ('order', models.FloatField(verbose_name='Порядок', default=0)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Создано')),
                ('modifyed', models.DateTimeField(db_index=True, auto_now=True, verbose_name='Изменено')),
                ('DateFrom', models.DateField(verbose_name='С даты', blank=True, null=True)),
                ('DateTo', models.DateField(verbose_name='По дату', blank=True, null=True)),
            ],
            options={
                'ordering': ['order', 'name'],
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='typesbase',
            name='accessability',
            field=models.BooleanField(verbose_name='Доступно', default=False),
        ),
        migrations.AlterField(
            model_name='typesbase',
            name='order',
            field=models.FloatField(verbose_name='Порядок', default=0),
        ),
        migrations.AlterField(
            model_name='typesinput',
            name='accessability',
            field=models.BooleanField(verbose_name='Доступно', default=False),
        ),
        migrations.AlterField(
            model_name='typesinput',
            name='order',
            field=models.FloatField(verbose_name='Порядок', default=0),
        ),
        migrations.AddField(
            model_name='bases',
            name='Type',
            field=models.ForeignKey(verbose_name='Тип', blank=True, on_delete=django.db.models.deletion.PROTECT, to='refer.TypesBase', null=True),
        ),
    ]
