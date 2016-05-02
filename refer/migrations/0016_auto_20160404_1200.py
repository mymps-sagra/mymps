# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('refer', '0015_auto_20160401_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='design',
            name='bases',
            field=models.ManyToManyField(verbose_name='Обоснование', blank=True, to='refer.Base'),
        ),
        migrations.AlterField(
            model_name='item',
            name='bases',
            field=models.ManyToManyField(verbose_name='Обоснование', blank=True, to='refer.Base'),
        ),
        migrations.AlterField(
            model_name='item',
            name='formats',
            field=models.ManyToManyField(verbose_name='Формат', blank=True, to='refer.Format'),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='bases',
            field=models.ManyToManyField(verbose_name='Обоснование', blank=True, to='refer.Base'),
        ),
        migrations.AlterField(
            model_name='packing',
            name='bases',
            field=models.ManyToManyField(verbose_name='Обоснование', blank=True, to='refer.Base'),
        ),
        migrations.AlterField(
            model_name='part',
            name='bases',
            field=models.ManyToManyField(verbose_name='Обоснование', blank=True, to='refer.Base'),
        ),
        migrations.AlterField(
            model_name='store',
            name='bases',
            field=models.ManyToManyField(verbose_name='Обоснование', blank=True, to='refer.Base'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='bases',
            field=models.ManyToManyField(verbose_name='Обоснование', blank=True, to='refer.Base'),
        ),
        migrations.AlterField(
            model_name='target',
            name='bases',
            field=models.ManyToManyField(verbose_name='Обоснование', blank=True, to='refer.Base'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='bases',
            field=models.ManyToManyField(verbose_name='Обоснование', blank=True, to='refer.Base'),
        ),
    ]
