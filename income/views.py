from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.views.generic.base import ContextMixin
from django.apps import apps
from django.views.generic.list import ListView
from django.forms.models import inlineformset_factory
from common.mycontext import MyContextMixin, MyPageNumberContextMixin, \
    MyModelContextMixin, MyModelSetContextMixin
from common.views import CommonPositionSetGet, CommonPositionSetAdd, \
    CommonPositionSetDetail, CommonPositionSetEdit
from .models import Delivery, Position_delivery
from .forms import DeliveryForm, PositionForm

APP = 'income'


class MyIncomesContextMixin(ContextMixin):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["app_code"] = APP
        context["app_name"] = apps.get_app_config(APP).verbose_name
        submenus = [
            {"url": "delivery_list",          "model": Delivery},
            {"url": "position_delivery_list", "model": Position_delivery},
        ]
        for submenu in submenus:
            submenu["model_name"] = submenu["model"]._meta.verbose_name_plural
        context["submenus"] = submenus
        return context


class IncomeMenu(TemplateView, MyContextMixin, MyIncomesContextMixin):
    template_name = APP + "/income_menu.html"


class DeliveryList(ListView, MyPageNumberContextMixin, MyModelContextMixin, 
    MyIncomesContextMixin):
    model = Delivery
    queryset = model.objects.order_by("-date", "name")
    paginate_by = 5
    allow_empty = True


class DeliveryGet(CommonPositionSetGet, MyPageNumberContextMixin, MyModelContextMixin):
    model = Delivery
    modelinline = Position_delivery
    Form = DeliveryForm
    FormSet = inlineformset_factory(model, modelinline, form=PositionForm, 
        fk_name="delivery", min_num=1, extra=5)
    form = Form()
    formset = FormSet()
    back_url = 'delivery_list'


class DeliveryAdd(CommonPositionSetAdd, DeliveryGet):
    success_url = 'delivery_list'
    template_name = APP + "/delivery_form.html"


class DeliveryDetail(CommonPositionSetDetail, DeliveryGet):
    model = Delivery
    modelinline = Position_delivery
    FormSet = inlineformset_factory(model, modelinline, form=PositionForm, 
        fk_name="delivery", extra=0, can_delete=False)
    template_name = APP + "/delivery_detail.html"


class DeliveryEdit(CommonPositionSetEdit, DeliveryAdd):
    pass


class PositionList(ListView, MyPageNumberContextMixin, MyModelContextMixin, 
    MyModelSetContextMixin, MyIncomesContextMixin):
    model = Position_delivery
    model_set = [Delivery]
    queryset = model.objects.order_by("item", "-modifyed",)
    paginate_by = 5
    allow_empty = True


#EOF
