from django.db import models

# Create your models here.
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from common.models import CommonModel, CommonPositionModel
from refer.models import ReferBased, TypeIssue, Consumer, Store, Target
from refer.models import Item, Design, Packing, Unit, Part


class Issue(CommonModel, ReferBased):

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
    type = models.ForeignKey(
        TypeIssue,
        blank = True, 
        null = True,
        limit_choices_to = {'accessability': True},
        on_delete = models.PROTECT,
        verbose_name = "Тип",
        )
    consumer = models.ForeignKey(
        Consumer,
        blank = True, 
        null = True,
        limit_choices_to = {'accessability': True},
        on_delete = models.PROTECT,
        verbose_name = Consumer._meta.verbose_name,
        )
    executed = models.BooleanField(
        default = False, 
        verbose_name = "Исполнено",
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

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-date", "name"]
        verbose_name = "Выдача"
        verbose_name_plural = "Выдачи"


class Position_issue(CommonPositionModel):

    issue = models.ForeignKey(
        Issue,
        blank = False, 
        null = True,
        on_delete = models.PROTECT,
        verbose_name = Issue._meta.verbose_name,
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
    part = models.ForeignKey(
        Part,
        blank = True, 
        null = True,
        limit_choices_to = {'accessability': True},
        on_delete = models.PROTECT,
        verbose_name = Part._meta.verbose_name,
        )

    def __str__(self):
        return self.issue.name + "/" + self.number + "/" + self.item.name

    class Meta:
        ordering = ["number"]
        verbose_name = "Позиция выдачи"
        verbose_name_plural = "Позиции выдач"
        unique_together = ("issue", "number")


#EOF