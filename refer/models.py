from django.db import models

# Create your models here.
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from common.models import CommonModel


class ReferCommon(CommonModel):
    name = models.CharField(
        max_length = 100, 
        unique = True, 
        verbose_name = "Название",
        validators = [
            RegexValidator(regex=r'^\S+', 
                message= "Текст не должен начинаться пробелом"),
            RegexValidator(regex=r'\S+$', 
                message= "Текст не должен оканчиваться пробелом"),
            ]
        )
    order = models.FloatField(
        default = 0, 
        verbose_name = "Порядок",
        )

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = ["order", "name"]


class ReferType(ReferCommon):
    code = models.SlugField(
        max_length = 50, 
        unique = True, 
        verbose_name = "Код",
        )

    class Meta:
        abstract = True


class TypeBase(ReferType):

    class Meta:
        verbose_name = "Тип обоснования"
        verbose_name_plural = "Типы обоснований"


class TypeSupplier(ReferType):

    class Meta:
        verbose_name = "Тип поставшика"
        verbose_name_plural = "Типы поставщиков"


class TypeDesign(ReferType):

    class Meta:
        verbose_name = "Тип формы"
        verbose_name_plural = "Типы форм"


class TypePacking(ReferType):

    class Meta:
        verbose_name = "Тип фасовки"
        verbose_name_plural = "Типы фасовок"


class TypeUnit(ReferType):

    class Meta:
        verbose_name = "Тип единицы"
        verbose_name_plural = "Типы единиц"


class TypeItem(ReferType):

    class Meta:
        verbose_name = "Тип медсредства"
        verbose_name_plural = "Типы медсредств"


class TypeManufacturer(ReferType):

    class Meta:
        verbose_name = "Тип изготовителя"
        verbose_name_plural = "Типы изготовителей"


class TypeStore(ReferType):

    class Meta:
        verbose_name = "Тип хранилища"
        verbose_name_plural = "Типы хранилищ"


class TypeTarget(ReferType):

    class Meta:
        verbose_name = "Тип цели"
        verbose_name_plural = "Типы целей"


class TypeDelivery(ReferType):

    class Meta:
        verbose_name = "Тип поставки"
        verbose_name_plural = "Типы поставок"


class TypePart(ReferType):

    class Meta:
        verbose_name = "Тип партии"
        verbose_name_plural = "Типы партий"


class TypeConsumer(ReferType):

    class Meta:
        verbose_name = "Тип получателя"
        verbose_name_plural = "Типы получателей"


class TypeIssue(ReferType):

    class Meta:
        verbose_name = "Тип выдачи"
        verbose_name_plural = "Типы выдач"


class Base(ReferCommon):
    type = models.ForeignKey(
        TypeBase,
        blank = True, 
        null = True,
        limit_choices_to = {'accessability': True},
        on_delete = models.PROTECT,
        verbose_name = "Тип",
        )
    date_from = models.DateField(
        blank = True, 
        null = True,
        verbose_name = "С даты",
        )
    date_to = models.DateField(
        blank = True, 
        null = True,
        verbose_name = "По дату",
        )

    class Meta:
        verbose_name = "Обоснование"
        verbose_name_plural = "Обоснования"

    def clean(self):
        if self.date_from and self.date_to :
            if self.date_from > self.date_to :
                raise ValidationError('"С даты" больше чем "По дату".')


class ReferBased(models.Model):
    bases = models.ManyToManyField(
        Base,
        blank = True, 
        limit_choices_to = {'accessability': True},
        verbose_name = Base._meta.verbose_name,
        )

    class Meta:
        abstract = True


class Supplier(ReferCommon, ReferBased):
    type = models.ForeignKey(
        TypeSupplier,
        blank = True, 
        null = True,
        limit_choices_to = {'accessability': True},
        on_delete = models.PROTECT,
        verbose_name = "Тип",
        )

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"


class Design(ReferCommon, ReferBased):
    type = models.ForeignKey(
        TypeDesign,
        blank = True, 
        null = True,
        limit_choices_to = {'accessability': True},
        on_delete = models.PROTECT,
        verbose_name = "Тип",
        )

    class Meta:
        verbose_name = "Форма"
        verbose_name_plural = "Формы"


class Packing(ReferCommon, ReferBased):
    type = models.ForeignKey(
        TypePacking,
        blank = True, 
        null = True,
        limit_choices_to = {'accessability': True},
        on_delete = models.PROTECT,
        verbose_name = "Тип",
        )

    class Meta:
        verbose_name = "Фасовка"
        verbose_name_plural = "Фасовки"


class Unit(ReferCommon, ReferBased):
    type = models.ForeignKey(
        TypeUnit,
        blank = True, 
        null = True,
        limit_choices_to = {'accessability': True},
        on_delete = models.PROTECT,
        verbose_name = "Тип",
        )

    class Meta:
        verbose_name = "Единица"
        verbose_name_plural = "Единицы"


class Format(ReferCommon):
    design = models.ForeignKey(
        Design,
        blank = True, 
        null = True,
        limit_choices_to = {'accessability': True},
        on_delete = models.PROTECT,
        verbose_name = Design._meta.verbose_name,
        )
    packing = models.ForeignKey(
        Packing,
        blank = True, 
        null = True,
        limit_choices_to = {'accessability': True},
        on_delete = models.PROTECT,
        verbose_name = Packing._meta.verbose_name,
        )
    unit = models.ForeignKey(
        Unit,
        blank = True, 
        null = True,
        limit_choices_to = {'accessability': True},
        on_delete = models.PROTECT,
        verbose_name = Unit._meta.verbose_name,
        )
    precision = models.SmallIntegerField(
        default = 0, 
        verbose_name = "Точность",
        validators = [
            MaxValueValidator(6),
            MinValueValidator(-6),
            ]
        )

    class Meta:
        verbose_name = "Формат"
        verbose_name_plural = "Форматы"


class Item(ReferCommon, ReferBased):
    type = models.ForeignKey(
        TypeItem,
        blank = True, 
        null = True,
        limit_choices_to = {'accessability': True},
        on_delete = models.PROTECT,
        verbose_name = "Тип",
        )
    formats = models.ManyToManyField(
        Format,
        blank = True, 
        limit_choices_to = {'accessability': True},
        verbose_name = Format._meta.verbose_name,
        )

    class Meta:
        verbose_name = "Медсредство"
        verbose_name_plural = "Медсредства"


class Manufacturer(ReferCommon, ReferBased):
    type = models.ForeignKey(
        TypeManufacturer,
        blank = True, 
        null = True,
        limit_choices_to = {'accessability': True},
        on_delete = models.PROTECT,
        verbose_name = "Тип",
        )

    class Meta:
        verbose_name = "Изготовитель"
        verbose_name_plural = "Изготовители"


class Store(ReferCommon, ReferBased):
    type = models.ForeignKey(
        TypeStore,
        blank = True, 
        null = True,
        limit_choices_to = {'accessability': True},
        on_delete = models.PROTECT,
        verbose_name = "Тип",
        )

    class Meta:
        verbose_name = "Хранилище"
        verbose_name_plural = "Хранилища"


class Target(ReferCommon, ReferBased):
    type = models.ForeignKey(
        TypeTarget,
        blank = True, 
        null = True,
        limit_choices_to = {'accessability': True},
        on_delete = models.PROTECT,
        verbose_name = "Тип",
        )

    class Meta:
        verbose_name = "Цель"
        verbose_name_plural = "Цели"


class Part(ReferCommon, ReferBased):
    type = models.ForeignKey(
        TypePart,
        blank = True, 
        null = True,
        limit_choices_to = {'accessability': True},
        on_delete = models.PROTECT,
        verbose_name = "Тип",
        )
    manufacturer = models.ForeignKey(
        Manufacturer,
        blank = True, 
        null = True,
        limit_choices_to = {'accessability': True},
        on_delete = models.PROTECT,
        verbose_name = Manufacturer._meta.verbose_name,
        )
    date_from = models.DateField(
        blank = True, 
        null = True,
        verbose_name = "С даты",
        )
    date_to = models.DateField(
        blank = True, 
        null = True,
        verbose_name = "По дату",
        )

    class Meta:
        verbose_name = "Партия"
        verbose_name_plural = "Партии"

    def clean(self):
        if self.date_from and self.date_to :
            if self.date_from > self.date_to :
                raise ValidationError('"С даты" больше чем "По дату".')


class Consumer(ReferCommon, ReferBased):
    type = models.ForeignKey(
        TypeConsumer,
        blank = True, 
        null = True,
        limit_choices_to = {'accessability': True},
        on_delete = models.PROTECT,
        verbose_name = "Тип",
        )

    class Meta:
        verbose_name = "Получатель"
        verbose_name_plural = "Получатели"


#EOF


