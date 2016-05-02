from django.db import models

# Create your models here.
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError


class CommonModel(models.Model):
    accessability = models.BooleanField(
        default = False, 
        verbose_name = "Доступно",
        )
    comment = models.TextField(
        max_length = 1000,
        blank = True, 
        verbose_name = "Примечание",
        )
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

    class Meta:
        abstract = True


class CommonPositionModel(models.Model):

    def clean_quantity(value):
        if value <= 0 :
            raise ValidationError('Количество должно быть БОЛЬШЕ нуля.')

    number = models.CharField(
        max_length = 100, 
        verbose_name = "Номер",
        validators = [
            RegexValidator(regex=r'^\S+', 
                message= "Текст не должен начинаться пробелом"),
            RegexValidator(regex=r'\S+$', 
                message= "Текст не должен оканчиваться пробелом"),
            ]
        )
    accessability = models.BooleanField(
        default = True, 
        verbose_name = "Доступно",
        )
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
    precision = models.SmallIntegerField(
        default = 0, 
        verbose_name = "Точность",
        validators = [
            MaxValueValidator(6),
            MinValueValidator(-6),
            ]
        )
    quantity = models.DecimalField(
        default = 0, 
        verbose_name = "Количество",
        max_digits = 20,
        decimal_places = 6,
        validators = [
            clean_quantity,
            ]
        )

    def clean(self):
        if self.quantity != round(self.quantity, self.precision) :
            raise ValidationError(
                'Номер:%s - Количество %s задано с избыточной точностью.' % \
                (self.number, self.quantity)
                )

    class Meta:
        abstract = True


#EOF


