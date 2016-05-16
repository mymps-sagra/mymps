from django.shortcuts import render

# Create your views here.
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, FormMixin
from django.apps import apps
from django.views.generic.base import ContextMixin
from common.mycontext import MyContextMixin, MyPageNumberContextMixin, \
    MyModelContextMixin
from .models import TypeBase, Base
from .forms import BaseForm
from .models import TypeSupplier, Supplier
from .forms import SupplierForm
from .models import TypeDesign, Design
from .forms import DesignForm
from .models import TypePacking, Packing
from .forms import PackingForm
from .models import TypeUnit, Unit
from .forms import UnitForm
from .models import Format
from .forms import FormatForm
from .models import TypeItem, Item
from .forms import ItemForm
from .models import TypeManufacturer, Manufacturer
from .forms import ManufacturerForm
from .models import TypeStore, Store
from .forms import StoreForm
from .models import TypeTarget, Target
from .forms import TargetForm
from .models import TypeDelivery
from .models import TypePart, Part
from .forms import PartForm
from .models import TypeConsumer, Consumer
from .forms import ConsumerForm
from .models import TypeIssue

APP = 'refer'


class MyRefersContextMixin(ContextMixin):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["app_code"] = APP
        context["app_name"] = apps.get_app_config(APP).verbose_name
        refers = [
            {"url": "base_list",         "model": Base},
            {"url": "supplier_list",     "model": Supplier},
            {"url": "design_list",       "model": Design},
            {"url": "packing_list",      "model": Packing},
            {"url": "unit_list",         "model": Unit},
            {"url": "format_list",       "model": Format},
            {"url": "item_list",         "model": Item},
            {"url": "manufacturer_list", "model": Manufacturer},
            {"url": "store_list",        "model": Store},
            {"url": "target_list",       "model": Target},
            {"url": "part_list",         "model": Part},
            {"url": "consumer_list",     "model": Consumer},
            #{"url": "type_base",         "model": TypeBase},
            #{"url": "type_supplier",     "model": TypeSupplier},
            #{"url": "type_design",       "model": TypeDesign},
            #{"url": "type_packing",      "model": TypePacking},
            #{"url": "type_unit",         "model": TypeUnit},
            #{"url": "type_item",         "model": TypeItem},
            #{"url": "type_manufacturer", "model": TypeManufacturer},
            #{"url": "type_store",        "model": TypeStore},
            #{"url": "type_target",       "model": TypeTarget},
            #{"url": "type_delivery",     "model": TypeDelivery},
            #{"url": "type_part",         "model": TypePart},
            #{"url": "type_consumer",     "model": TypeConsumer},
            #{"url": "type_issue",        "model": TypeIssue},
        ]
        for refer in refers:
            refer["model_name"] = refer["model"]._meta.verbose_name_plural
        context["refers"] = refers
        return context


class ReferMenu(TemplateView, MyContextMixin, MyRefersContextMixin):
    template_name = APP + "/refer_menu.html"


class TypePage(ReferMenu, MyModelContextMixin):
    template_name = APP + "/type_page.html"
    model = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["objects"] = self.model.objects.all().order_by("order", "name")
        return context


class TypeBasePage(TypePage):
    model = TypeBase


class TypeSupplierPage(TypePage):
    model = TypeSupplier


class TypeDesignPage(TypePage):
    model = TypeDesign


class TypePackingPage(TypePage):
    model = TypePacking


class TypeUnitPage(TypePage):
    model = TypeUnit


class TypeItemPage(TypePage):
    model = TypeItem


class TypeManufacturerPage(TypePage):
    model = TypeManufacturer


class TypeStorePage(TypePage):
    model = TypeStore


class TypeTargetPage(TypePage):
    model = TypeTarget


class TypeDeliveryPage(TypePage):
    model = TypeDelivery


class TypePartPage(TypePage):
    model = TypePart


class TypeConsumerPage(TypePage):
    model = TypeConsumer


class TypeIssuePage(TypePage):
    model = TypeDelivery


class CommonList(ListView, MyPageNumberContextMixin, MyModelContextMixin, 
    MyRefersContextMixin):
    model = None
    if model:
        queryset = model.objects.order_by("order", "name")
    paginate_by = 5
    allow_empty = True


class CommonDetail(DetailView, MyPageNumberContextMixin, MyModelContextMixin):
    model = None
    form_class = None
    form = None

    def get(self, request, *args, **kwargs):
        obj = self.model.objects.get(pk = self.kwargs["pk"])
        self.form = self.form_class(instance = obj)
        for f in self.form.fields:
            self.form.fields[f].widget.attrs['disabled'] = 'disabled'
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_verbose_name"] = self.model._meta.verbose_name
        context['form'] = self.form
        return context


class CommonEdit(FormMixin, MyPageNumberContextMixin, MyModelContextMixin):
    model = None
    fields = "__all__"
    success_url = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_verbose_name"] = self.model._meta.verbose_name
        # print(self.fields)
        return context

    def get_success_url(self, **kwargs):
        return self.success_url + "?page=" + self.request.GET.get("page", "1")


class BaseList(CommonList):
    model = Base


class BaseDetail(CommonDetail):
    model = Base
    form_class = BaseForm


class BaseEdit(CommonEdit, UpdateView):
    model = Base
    success_url = reverse_lazy('base_list')


class BaseAdd(CommonEdit, CreateView):
    model = Base
    success_url = reverse_lazy('base_list')


class SupplierList(CommonList):
    model = Supplier


class SupplierDetail(CommonDetail):
    model = Supplier
    form_class = SupplierForm


class SupplierEdit(CommonEdit, UpdateView):
    model = Supplier
    success_url = reverse_lazy('supplier_list')


class SupplierAdd(CommonEdit, CreateView):
    model = Supplier
    success_url = reverse_lazy('supplier_list')


class DesignList(CommonList):
    model = Design


class DesignDetail(CommonDetail):
    model = Design
    form_class = DesignForm


class DesignEdit(CommonEdit, UpdateView):
    model = Design
    success_url = reverse_lazy('design_list')


class DesignAdd(CommonEdit, CreateView):
    model = Design
    success_url = reverse_lazy('design_list')


class PackingList(CommonList):
    model = Packing


class PackingDetail(CommonDetail):
    model = Packing
    form_class = PackingForm


class PackingEdit(CommonEdit, UpdateView):
    model = Packing
    success_url = reverse_lazy('packing_list')


class PackingAdd(CommonEdit, CreateView):
    model = Packing
    success_url = reverse_lazy('packing_list')


class UnitList(CommonList):
    model = Unit


class UnitDetail(CommonDetail):
    model = Unit
    form_class = UnitForm


class UnitEdit(CommonEdit, UpdateView):
    model = Unit
    success_url = reverse_lazy('unit_list')


class UnitAdd(CommonEdit, CreateView):
    model = Unit
    success_url = reverse_lazy('unit_list')


class FormatList(CommonList):
    model = Format


class FormatDetail(CommonDetail):
    model = Format
    form_class = FormatForm


class FormatEdit(CommonEdit, UpdateView):
    model = Format
    success_url = reverse_lazy('format_list')


class FormatAdd(CommonEdit, CreateView):
    model = Format
    success_url = reverse_lazy('format_list')


class ItemList(CommonList):
    model = Item


class ItemDetail(CommonDetail):
    model = Item
    form_class = ItemForm


class ItemEdit(CommonEdit, UpdateView):
    model = Item
    success_url = reverse_lazy('item_list')


class ItemAdd(CommonEdit, CreateView):
    model = Item
    success_url = reverse_lazy('item_list')


class ManufacturerList(CommonList):
    model = Manufacturer


class ManufacturerDetail(CommonDetail):
    model = Manufacturer
    form_class = ManufacturerForm


class ManufacturerEdit(CommonEdit, UpdateView):
    model = Manufacturer
    success_url = reverse_lazy('manufacturer_list')


class ManufacturerAdd(CommonEdit, CreateView):
    model = Manufacturer
    success_url = reverse_lazy('manufacturer_list')


class StoreList(CommonList):
    model = Store


class StoreDetail(CommonDetail):
    model = Store
    form_class = StoreForm


class StoreEdit(CommonEdit, UpdateView):
    model = Store
    success_url = reverse_lazy('store_list')


class StoreAdd(CommonEdit, CreateView):
    model = Store
    success_url = reverse_lazy('store_list')


class TargetList(CommonList):
    model = Target


class TargetDetail(CommonDetail):
    model = Target
    form_class = TargetForm


class TargetEdit(CommonEdit, UpdateView):
    model = Target
    success_url = reverse_lazy('target_list')


class TargetAdd(CommonEdit, CreateView):
    model = Target
    success_url = reverse_lazy('target_list')


class PartList(CommonList):
    model = Part


class PartDetail(CommonDetail):
    model = Part
    form_class = PartForm


class PartEdit(CommonEdit, UpdateView):
    model = Part
    success_url = reverse_lazy('part_list')


class PartAdd(CommonEdit, CreateView):
    model = Part
    success_url = reverse_lazy('part_list')


class ConsumerList(CommonList):
    model = Consumer


class ConsumerDetail(CommonDetail):
    model = Consumer
    form_class = ConsumerForm


class ConsumerEdit(CommonEdit, UpdateView):
    model = Consumer
    success_url = reverse_lazy('consumer_list')


class ConsumerAdd(CommonEdit, CreateView):
    model = Consumer
    success_url = reverse_lazy('consumer_list')


#EOF