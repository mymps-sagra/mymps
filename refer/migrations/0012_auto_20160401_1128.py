# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('refer', '0011_auto_20160331_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Название', validators=[django.core.validators.RegexValidator(regex='^\\S+', message='Текст не должен начинаться пробелом'), django.core.validators.RegexValidator(regex='\\S+$', message='Текст не должен оканчиваться пробелом')], max_length=100, unique=True)),
                ('accessability', models.BooleanField(verbose_name='Доступно', default=False)),
                ('comment', models.TextField(verbose_name='Примечание', blank=True, max_length=1000)),
                ('order', models.FloatField(verbose_name='Порядок', default=0)),
                ('created', models.DateTimeField(verbose_name='Создано', db_index=True, auto_now_add=True)),
                ('modifyed', models.DateTimeField(verbose_name='Изменено', db_index=True, auto_now=True)),
                ('date_from', models.DateField(verbose_name='С даты', blank=True, null=True)),
                ('date_to', models.DateField(verbose_name='По дату', blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Обоснование',
                'verbose_name_plural': 'Обоснования',
            },
        ),
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Название', validators=[django.core.validators.RegexValidator(regex='^\\S+', message='Текст не должен начинаться пробелом'), django.core.validators.RegexValidator(regex='\\S+$', message='Текст не должен оканчиваться пробелом')], max_length=100, unique=True)),
                ('accessability', models.BooleanField(verbose_name='Доступно', default=False)),
                ('comment', models.TextField(verbose_name='Примечание', blank=True, max_length=1000)),
                ('order', models.FloatField(verbose_name='Порядок', default=0)),
                ('created', models.DateTimeField(verbose_name='Создано', db_index=True, auto_now_add=True)),
                ('modifyed', models.DateTimeField(verbose_name='Изменено', db_index=True, auto_now=True)),
                ('bases', models.ManyToManyField(verbose_name='Обоснования', blank=True, to='refer.Base')),
            ],
            options={
                'verbose_name': 'Форма',
                'verbose_name_plural': 'Формы',
            },
        ),
        migrations.CreateModel(
            name='Format',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Название', validators=[django.core.validators.RegexValidator(regex='^\\S+', message='Текст не должен начинаться пробелом'), django.core.validators.RegexValidator(regex='\\S+$', message='Текст не должен оканчиваться пробелом')], max_length=100, unique=True)),
                ('accessability', models.BooleanField(verbose_name='Доступно', default=False)),
                ('comment', models.TextField(verbose_name='Примечание', blank=True, max_length=1000)),
                ('order', models.FloatField(verbose_name='Порядок', default=0)),
                ('created', models.DateTimeField(verbose_name='Создано', db_index=True, auto_now_add=True)),
                ('modifyed', models.DateTimeField(verbose_name='Изменено', db_index=True, auto_now=True)),
                ('precision', models.SmallIntegerField(verbose_name='Точность', validators=[django.core.validators.MaxValueValidator(6), django.core.validators.MinValueValidator(-6)], default=0)),
                ('design', models.ForeignKey(verbose_name='Форма', null=True, on_delete=django.db.models.deletion.PROTECT, blank=True, to='refer.Design')),
            ],
            options={
                'verbose_name': 'Формат',
                'verbose_name_plural': 'Форматы',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Название', validators=[django.core.validators.RegexValidator(regex='^\\S+', message='Текст не должен начинаться пробелом'), django.core.validators.RegexValidator(regex='\\S+$', message='Текст не должен оканчиваться пробелом')], max_length=100, unique=True)),
                ('accessability', models.BooleanField(verbose_name='Доступно', default=False)),
                ('comment', models.TextField(verbose_name='Примечание', blank=True, max_length=1000)),
                ('order', models.FloatField(verbose_name='Порядок', default=0)),
                ('created', models.DateTimeField(verbose_name='Создано', db_index=True, auto_now_add=True)),
                ('modifyed', models.DateTimeField(verbose_name='Изменено', db_index=True, auto_now=True)),
                ('bases', models.ManyToManyField(verbose_name='Обоснования', blank=True, to='refer.Base')),
                ('formats', models.ManyToManyField(verbose_name='Форматы', blank=True, to='refer.Format')),
            ],
            options={
                'verbose_name': 'Медсредство',
                'verbose_name_plural': 'Медсредства',
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Название', validators=[django.core.validators.RegexValidator(regex='^\\S+', message='Текст не должен начинаться пробелом'), django.core.validators.RegexValidator(regex='\\S+$', message='Текст не должен оканчиваться пробелом')], max_length=100, unique=True)),
                ('accessability', models.BooleanField(verbose_name='Доступно', default=False)),
                ('comment', models.TextField(verbose_name='Примечание', blank=True, max_length=1000)),
                ('order', models.FloatField(verbose_name='Порядок', default=0)),
                ('created', models.DateTimeField(verbose_name='Создано', db_index=True, auto_now_add=True)),
                ('modifyed', models.DateTimeField(verbose_name='Изменено', db_index=True, auto_now=True)),
                ('bases', models.ManyToManyField(verbose_name='Обоснования', blank=True, to='refer.Base')),
            ],
            options={
                'verbose_name': 'Производитель',
                'verbose_name_plural': 'Производители',
            },
        ),
        migrations.CreateModel(
            name='Packing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Название', validators=[django.core.validators.RegexValidator(regex='^\\S+', message='Текст не должен начинаться пробелом'), django.core.validators.RegexValidator(regex='\\S+$', message='Текст не должен оканчиваться пробелом')], max_length=100, unique=True)),
                ('accessability', models.BooleanField(verbose_name='Доступно', default=False)),
                ('comment', models.TextField(verbose_name='Примечание', blank=True, max_length=1000)),
                ('order', models.FloatField(verbose_name='Порядок', default=0)),
                ('created', models.DateTimeField(verbose_name='Создано', db_index=True, auto_now_add=True)),
                ('modifyed', models.DateTimeField(verbose_name='Изменено', db_index=True, auto_now=True)),
                ('bases', models.ManyToManyField(verbose_name='Обоснования', blank=True, to='refer.Base')),
            ],
            options={
                'verbose_name': 'Фасовка',
                'verbose_name_plural': 'Фасовки',
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Название', validators=[django.core.validators.RegexValidator(regex='^\\S+', message='Текст не должен начинаться пробелом'), django.core.validators.RegexValidator(regex='\\S+$', message='Текст не должен оканчиваться пробелом')], max_length=100, unique=True)),
                ('accessability', models.BooleanField(verbose_name='Доступно', default=False)),
                ('comment', models.TextField(verbose_name='Примечание', blank=True, max_length=1000)),
                ('order', models.FloatField(verbose_name='Порядок', default=0)),
                ('created', models.DateTimeField(verbose_name='Создано', db_index=True, auto_now_add=True)),
                ('modifyed', models.DateTimeField(verbose_name='Изменено', db_index=True, auto_now=True)),
                ('bases', models.ManyToManyField(verbose_name='Обоснования', blank=True, to='refer.Base')),
            ],
            options={
                'verbose_name': 'Хранилище',
                'verbose_name_plural': 'Хранилища',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Название', validators=[django.core.validators.RegexValidator(regex='^\\S+', message='Текст не должен начинаться пробелом'), django.core.validators.RegexValidator(regex='\\S+$', message='Текст не должен оканчиваться пробелом')], max_length=100, unique=True)),
                ('accessability', models.BooleanField(verbose_name='Доступно', default=False)),
                ('comment', models.TextField(verbose_name='Примечание', blank=True, max_length=1000)),
                ('order', models.FloatField(verbose_name='Порядок', default=0)),
                ('created', models.DateTimeField(verbose_name='Создано', db_index=True, auto_now_add=True)),
                ('modifyed', models.DateTimeField(verbose_name='Изменено', db_index=True, auto_now=True)),
                ('bases', models.ManyToManyField(verbose_name='Обоснования', blank=True, to='refer.Base')),
            ],
            options={
                'verbose_name': 'Поставщик',
                'verbose_name_plural': 'Поставщики',
            },
        ),
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Название', validators=[django.core.validators.RegexValidator(regex='^\\S+', message='Текст не должен начинаться пробелом'), django.core.validators.RegexValidator(regex='\\S+$', message='Текст не должен оканчиваться пробелом')], max_length=100, unique=True)),
                ('accessability', models.BooleanField(verbose_name='Доступно', default=False)),
                ('comment', models.TextField(verbose_name='Примечание', blank=True, max_length=1000)),
                ('order', models.FloatField(verbose_name='Порядок', default=0)),
                ('created', models.DateTimeField(verbose_name='Создано', db_index=True, auto_now_add=True)),
                ('modifyed', models.DateTimeField(verbose_name='Изменено', db_index=True, auto_now=True)),
                ('bases', models.ManyToManyField(verbose_name='Обоснования', blank=True, to='refer.Base')),
            ],
            options={
                'verbose_name': 'Цель',
                'verbose_name_plural': 'Цели',
            },
        ),
        migrations.CreateModel(
            name='TypeBase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Название', validators=[django.core.validators.RegexValidator(regex='^\\S+', message='Текст не должен начинаться пробелом'), django.core.validators.RegexValidator(regex='\\S+$', message='Текст не должен оканчиваться пробелом')], max_length=100, unique=True)),
                ('accessability', models.BooleanField(verbose_name='Доступно', default=False)),
                ('comment', models.TextField(verbose_name='Примечание', blank=True, max_length=1000)),
                ('order', models.FloatField(verbose_name='Порядок', default=0)),
                ('created', models.DateTimeField(verbose_name='Создано', db_index=True, auto_now_add=True)),
                ('modifyed', models.DateTimeField(verbose_name='Изменено', db_index=True, auto_now=True)),
                ('code', models.SlugField(verbose_name='Код', unique=True)),
            ],
            options={
                'verbose_name': 'Тип обоснования',
                'verbose_name_plural': 'Типы обоснований',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Название', validators=[django.core.validators.RegexValidator(regex='^\\S+', message='Текст не должен начинаться пробелом'), django.core.validators.RegexValidator(regex='\\S+$', message='Текст не должен оканчиваться пробелом')], max_length=100, unique=True)),
                ('accessability', models.BooleanField(verbose_name='Доступно', default=False)),
                ('comment', models.TextField(verbose_name='Примечание', blank=True, max_length=1000)),
                ('order', models.FloatField(verbose_name='Порядок', default=0)),
                ('created', models.DateTimeField(verbose_name='Создано', db_index=True, auto_now_add=True)),
                ('modifyed', models.DateTimeField(verbose_name='Изменено', db_index=True, auto_now=True)),
                ('bases', models.ManyToManyField(verbose_name='Обоснования', blank=True, to='refer.Base')),
            ],
            options={
                'verbose_name': 'Единица',
                'verbose_name_plural': 'Единицы',
            },
        ),
        migrations.RenameModel(
            old_name='TypesDesign',
            new_name='TypeDesign',
        ),
        migrations.RenameModel(
            old_name='TypesIncome',
            new_name='TypeIncome',
        ),
        migrations.RenameModel(
            old_name='TypesItem',
            new_name='TypeItem',
        ),
        migrations.RenameModel(
            old_name='TypesManufacturer',
            new_name='TypeManufacturer',
        ),
        migrations.RenameModel(
            old_name='TypesPacking',
            new_name='TypePacking',
        ),
        migrations.RenameModel(
            old_name='TypesStore',
            new_name='TypeStore',
        ),
        migrations.RenameModel(
            old_name='TypesSupplier',
            new_name='TypeSupplier',
        ),
        migrations.RenameModel(
            old_name='TypesTarget',
            new_name='TypeTarget',
        ),
        migrations.RenameModel(
            old_name='TypesUnit',
            new_name='TypeUnit',
        ),
        migrations.RemoveField(
            model_name='bases',
            name='type',
        ),
        migrations.RemoveField(
            model_name='designs',
            name='bases',
        ),
        migrations.RemoveField(
            model_name='designs',
            name='type',
        ),
        migrations.RemoveField(
            model_name='formats',
            name='design',
        ),
        migrations.RemoveField(
            model_name='formats',
            name='packing',
        ),
        migrations.RemoveField(
            model_name='formats',
            name='unit',
        ),
        migrations.RemoveField(
            model_name='items',
            name='bases',
        ),
        migrations.RemoveField(
            model_name='items',
            name='formats',
        ),
        migrations.RemoveField(
            model_name='items',
            name='type',
        ),
        migrations.RemoveField(
            model_name='manufacturers',
            name='bases',
        ),
        migrations.RemoveField(
            model_name='manufacturers',
            name='type',
        ),
        migrations.RemoveField(
            model_name='packings',
            name='bases',
        ),
        migrations.RemoveField(
            model_name='packings',
            name='type',
        ),
        migrations.RemoveField(
            model_name='stores',
            name='bases',
        ),
        migrations.RemoveField(
            model_name='stores',
            name='type',
        ),
        migrations.RemoveField(
            model_name='suppliers',
            name='bases',
        ),
        migrations.RemoveField(
            model_name='suppliers',
            name='type',
        ),
        migrations.RemoveField(
            model_name='targets',
            name='bases',
        ),
        migrations.RemoveField(
            model_name='targets',
            name='type',
        ),
        migrations.RemoveField(
            model_name='units',
            name='bases',
        ),
        migrations.RemoveField(
            model_name='units',
            name='type',
        ),
        migrations.DeleteModel(
            name='Bases',
        ),
        migrations.DeleteModel(
            name='Designs',
        ),
        migrations.DeleteModel(
            name='Formats',
        ),
        migrations.DeleteModel(
            name='Items',
        ),
        migrations.DeleteModel(
            name='Manufacturers',
        ),
        migrations.DeleteModel(
            name='Packings',
        ),
        migrations.DeleteModel(
            name='Stores',
        ),
        migrations.DeleteModel(
            name='Suppliers',
        ),
        migrations.DeleteModel(
            name='Targets',
        ),
        migrations.DeleteModel(
            name='TypesBase',
        ),
        migrations.DeleteModel(
            name='Units',
        ),
        migrations.AddField(
            model_name='unit',
            name='type',
            field=models.ForeignKey(verbose_name='Тип', null=True, on_delete=django.db.models.deletion.PROTECT, blank=True, to='refer.TypeUnit'),
        ),
        migrations.AddField(
            model_name='target',
            name='type',
            field=models.ForeignKey(verbose_name='Тип', null=True, on_delete=django.db.models.deletion.PROTECT, blank=True, to='refer.TypeTarget'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='type',
            field=models.ForeignKey(verbose_name='Тип', null=True, on_delete=django.db.models.deletion.PROTECT, blank=True, to='refer.TypeSupplier'),
        ),
        migrations.AddField(
            model_name='store',
            name='type',
            field=models.ForeignKey(verbose_name='Тип', null=True, on_delete=django.db.models.deletion.PROTECT, blank=True, to='refer.TypeStore'),
        ),
        migrations.AddField(
            model_name='packing',
            name='type',
            field=models.ForeignKey(verbose_name='Тип', null=True, on_delete=django.db.models.deletion.PROTECT, blank=True, to='refer.TypePacking'),
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='type',
            field=models.ForeignKey(verbose_name='Тип', null=True, on_delete=django.db.models.deletion.PROTECT, blank=True, to='refer.TypeManufacturer'),
        ),
        migrations.AddField(
            model_name='item',
            name='type',
            field=models.ForeignKey(verbose_name='Тип', null=True, on_delete=django.db.models.deletion.PROTECT, blank=True, to='refer.TypeItem'),
        ),
        migrations.AddField(
            model_name='format',
            name='packing',
            field=models.ForeignKey(verbose_name='Фасовка', null=True, on_delete=django.db.models.deletion.PROTECT, blank=True, to='refer.Packing'),
        ),
        migrations.AddField(
            model_name='format',
            name='unit',
            field=models.ForeignKey(verbose_name='Единица', null=True, on_delete=django.db.models.deletion.PROTECT, blank=True, to='refer.Unit'),
        ),
        migrations.AddField(
            model_name='design',
            name='type',
            field=models.ForeignKey(verbose_name='Тип', null=True, on_delete=django.db.models.deletion.PROTECT, blank=True, to='refer.TypeDesign'),
        ),
        migrations.AddField(
            model_name='base',
            name='type',
            field=models.ForeignKey(verbose_name='Тип', null=True, on_delete=django.db.models.deletion.PROTECT, blank=True, to='refer.TypeBase'),
        ),
    ]
