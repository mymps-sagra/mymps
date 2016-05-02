from django.db import models

# Create your models here.
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from common.models import CommonModel
from refer.models import Store, Target, Item, Design, Packing, Unit, Part


class Period(CommonModel):
    date = models.DateField(
        verbose_name = "Дата",
        )
    name = models.CharField(
        max_length = 100, 
        unique_for_date = "date", 
        verbose_name = "Название",
        validators = [
            RegexValidator(regex=r'^\S+', 
                message= "Текст не должен начинаться пробелом"),
            RegexValidator(regex=r'\S+$', 
                message= "Текст не должен оканчиваться пробелом"),
            ]
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
    executed = models.BooleanField(
        default = False, 
        verbose_name = "Исполнено",
        )
    stores = models.ManyToManyField(
        Store,
        blank = True, 
        limit_choices_to = {'accessability': True},
        verbose_name = Store._meta.verbose_name_plural,
        )
    stores_only_blank = models.BooleanField(
        default = False, 
        verbose_name = "Только неопределенные хранилища",
        )
    targets = models.ManyToManyField(
        Target,
        blank = True, 
        limit_choices_to = {'accessability': True},
        verbose_name = Target._meta.verbose_name_plural,
        )
    targets_only_blank = models.BooleanField(
        default = False, 
        verbose_name = "Только неопределенные цели",
        )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-date", "name"]
        verbose_name = "Период"
        verbose_name_plural = "Периоды"

    def clean(self):
        if self.date_from and self.date_to :
            if self.date_from > self.date_to :
                raise ValidationError('"С даты" больше чем "По дату".')


class Rest(models.Model):
    created = models.DateTimeField(
        auto_now_add = True, 
        db_index = True, 
        verbose_name = "Создано"
        )
    modifyed = models.DateTimeField(
        auto_now = True, 
        db_index = True, 
        verbose_name = "Изменено"
        )
    period = models.ForeignKey(
        Period,
        blank = False, 
        null = True,
        on_delete = models.PROTECT,
        verbose_name = Period._meta.verbose_name,
        )
    store = models.ForeignKey(
        Store,
        blank = True, 
        null = True,
        limit_choices_to = {'accessability': True},
        on_delete = models.PROTECT,
        verbose_name = Store._meta.verbose_name,
        )
    target = models.ForeignKey(
        Target,
        blank = True, 
        null = True,
        limit_choices_to = {'accessability': True},
        on_delete = models.PROTECT,
        verbose_name = Target._meta.verbose_name,
        )
    item = models.ForeignKey(
        Item,
        blank = False, 
        null = True,
        limit_choices_to = {'accessability': True},
        on_delete = models.PROTECT,
        verbose_name = Item._meta.verbose_name,
        )
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
        blank = False, 
        null = True,
        limit_choices_to = {'accessability': True},
        on_delete = models.PROTECT,
        verbose_name = Packing._meta.verbose_name,
        )
    unit = models.ForeignKey(
        Unit,
        blank = False, 
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
    part = models.ForeignKey(
        Part,
        blank = True, 
        null = True,
        limit_choices_to = {'accessability': True},
        on_delete = models.PROTECT,
        verbose_name = Part._meta.verbose_name,
        )
    rest_total = models.DecimalField(
        default = 0, 
        verbose_name = "Итоговый остаток",
        max_digits = 20,
        decimal_places = 6,
        )

    def __str__(self):
        return self.period.name + "/" + self.item.name

    class Meta:
        ordering = ["item"]
        verbose_name = "Остаток"
        verbose_name_plural = "Остатки"


class Turnover(models.Model):
    created = models.DateTimeField(
        auto_now_add = True, 
        db_index = True, 
        verbose_name = "Создано"
        )
    modifyed = models.DateTimeField(
        auto_now = True, 
        db_index = True, 
        verbose_name = "Изменено"
        )
    period = models.ForeignKey(
        Period,
        blank = False, 
        null = True,
        on_delete = models.PROTECT,
        verbose_name = Period._meta.verbose_name,
        )
    store = models.ForeignKey(
        Store,
        blank = True, 
        null = True,
        limit_choices_to = {'accessability': True},
        on_delete = models.PROTECT,
        verbose_name = Store._meta.verbose_name,
        )
    target = models.ForeignKey(
        Target,
        blank = True, 
        null = True,
        limit_choices_to = {'accessability': True},
        on_delete = models.PROTECT,
        verbose_name = Target._meta.verbose_name,
        )
    item = models.ForeignKey(
        Item,
        blank = False, 
        null = True,
        limit_choices_to = {'accessability': True},
        on_delete = models.PROTECT,
        verbose_name = Item._meta.verbose_name,
        )
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
        blank = False, 
        null = True,
        limit_choices_to = {'accessability': True},
        on_delete = models.PROTECT,
        verbose_name = Packing._meta.verbose_name,
        )
    unit = models.ForeignKey(
        Unit,
        blank = False, 
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
    part = models.ForeignKey(
        Part,
        blank = True, 
        null = True,
        limit_choices_to = {'accessability': True},
        on_delete = models.PROTECT,
        verbose_name = Part._meta.verbose_name,
        )
    rest_total = models.DecimalField(
        default = 0, 
        verbose_name = "Итоговый остаток",
        max_digits = 20,
        decimal_places = 6,
        )
    rest_init = models.DecimalField(
        default = 0, 
        verbose_name = "Входящий остаток",
        max_digits = 20,
        decimal_places = 6,
        )
    quantity_in = models.DecimalField(
        default = 0, 
        verbose_name = "Поставлено",
        max_digits = 20,
        decimal_places = 6,
        )
    quantity_out = models.DecimalField(
        default = 0, 
        verbose_name = "Отпущено",
        max_digits = 20,
        decimal_places = 6,
        )

    def __str__(self):
        return self.period.name + "/" + self.item.name

    class Meta:
        ordering = ["item"]
        verbose_name = "Оборот"
        verbose_name_plural = "Обороты"


#EOF