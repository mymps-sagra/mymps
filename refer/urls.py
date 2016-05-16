"""refer URL Configuration

Справочники
"""
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import ReferMenu
from .views import TypeBasePage
from .views import BaseList, BaseAdd, BaseDetail, BaseEdit
from .views import TypeSupplierPage
from .views import SupplierList, SupplierAdd, SupplierDetail, SupplierEdit
from .views import TypeDesignPage
from .views import DesignList, DesignAdd, DesignDetail, DesignEdit
from .views import TypePackingPage
from .views import PackingList, PackingAdd, PackingDetail, PackingEdit
from .views import TypeUnitPage
from .views import UnitList, UnitAdd, UnitDetail, UnitEdit
from .views import FormatList, FormatAdd, FormatDetail, FormatEdit
from .views import TypeItemPage
from .views import ItemList, ItemAdd, ItemDetail, ItemEdit
from .views import TypeManufacturerPage
from .views import ManufacturerList, ManufacturerAdd, ManufacturerDetail, ManufacturerEdit
from .views import TypeStorePage
from .views import StoreList, StoreAdd, StoreDetail, StoreEdit
from .views import TypeTargetPage
from .views import TargetList, TargetAdd, TargetDetail, TargetEdit
from .views import TypeDeliveryPage
from .views import TypePartPage
from .views import PartList, PartAdd, PartDetail, PartEdit
from .views import TypeConsumerPage
from .views import ConsumerList, ConsumerAdd, ConsumerDetail, ConsumerEdit
from .views import TypeIssuePage


urlpatterns = [
    url(r'^$',                                 login_required(ReferMenu.as_view()),             name="refer"),
    #url(r'^type_base/$',                       login_required(TypeBasePage.as_view()),          name="type_base"),
    url(r'^base_list/$',                       login_required(BaseList.as_view()),              name="base_list"),
    url(r'^base_add/$',                        login_required(BaseAdd.as_view()),               name='base_add'),
    url(r'^base_detail/(?P<pk>\d+)/$',         login_required(BaseDetail.as_view()),            name='base_detail'),
    url(r'^base_edit/(?P<pk>\d+)/$',           login_required(BaseEdit.as_view()),              name='base_edit'),
    #url(r'^type_supplier/$',                   login_required(TypeSupplierPage.as_view()),      name="type_supplier"),
    url(r'^supplier_list/$',                   login_required(SupplierList.as_view()),          name="supplier_list"),
    url(r'^supplier_add/$',                    login_required(SupplierAdd.as_view()),           name='supplier_add'),
    url(r'^supplier_detail/(?P<pk>\d+)/$',     login_required(SupplierDetail.as_view()),        name='supplier_detail'),
    url(r'^supplier_edit/(?P<pk>\d+)/$',       login_required(SupplierEdit.as_view()),          name='supplier_edit'),
    #url(r'^type_design/$',                     login_required(TypeDesignPage.as_view()),        name="type_design"),
    url(r'^design_list/$',                     login_required(DesignList.as_view()),            name="design_list"),
    url(r'^design_add/$',                      login_required(DesignAdd.as_view()),             name='design_add'),
    url(r'^design_detail/(?P<pk>\d+)/$',       login_required(DesignDetail.as_view()),          name='design_detail'),
    url(r'^design_edit/(?P<pk>\d+)/$',         login_required(DesignEdit.as_view()),            name='design_edit'),
    #url(r'^type_packing/$',                    login_required(TypePackingPage.as_view()),       name="type_packing"),
    url(r'^packing_list/$',                    login_required(PackingList.as_view()),           name="packing_list"),
    url(r'^packing_add/$',                     login_required(PackingAdd.as_view()),            name='packing_add'),
    url(r'^packing_detail/(?P<pk>\d+)/$',      login_required(PackingDetail.as_view()),         name='packing_detail'),
    url(r'^packing_edit/(?P<pk>\d+)/$',        login_required(PackingEdit.as_view()),           name='packing_edit'),
    #url(r'^type_unit/$',                       login_required(TypeUnitPage.as_view()),          name="type_unit"),
    url(r'^unit_list/$',                       login_required(UnitList.as_view()),              name="unit_list"),
    url(r'^unit_add/$',                        login_required(UnitAdd.as_view()),               name='unit_add'),
    url(r'^unit_detail/(?P<pk>\d+)/$',         login_required(UnitDetail.as_view()),            name='unit_detail'),
    url(r'^unit_edit/(?P<pk>\d+)/$',           login_required(UnitEdit.as_view()),              name='unit_edit'),
    url(r'^format_list/$',                     login_required(FormatList.as_view()),            name="format_list"),
    url(r'^format_add/$',                      login_required(FormatAdd.as_view()),             name='format_add'),
    url(r'^format_detail/(?P<pk>\d+)/$',       login_required(FormatDetail.as_view()),          name='format_detail'),
    url(r'^format_edit/(?P<pk>\d+)/$',         login_required(FormatEdit.as_view()),            name='format_edit'),
    #url(r'^type_item/$',                       login_required(TypeItemPage.as_view()),          name="type_item"),
    url(r'^item_list/$',                       login_required(ItemList.as_view()),              name="item_list"),
    url(r'^item_add/$',                        login_required(ItemAdd.as_view()),               name='item_add'),
    url(r'^item_detail/(?P<pk>\d+)/$',         login_required(ItemDetail.as_view()),            name='item_detail'),
    url(r'^item_edit/(?P<pk>\d+)/$',           login_required(ItemEdit.as_view()),              name='item_edit'),
    #url(r'^type_manufacturer/$',               login_required(TypeManufacturerPage.as_view()),  name="type_manufacturer"),
    url(r'^manufacturer_list/$',               login_required(ManufacturerList.as_view()),      name="manufacturer_list"),
    url(r'^manufacturer_add/$',                login_required(ManufacturerAdd.as_view()),       name='manufacturer_add'),
    url(r'^manufacturer_detail/(?P<pk>\d+)/$', login_required(ManufacturerDetail.as_view()),    name='manufacturer_detail'),
    url(r'^manufacturer_edit/(?P<pk>\d+)/$',   login_required(ManufacturerEdit.as_view()),      name='manufacturer_edit'),
    #url(r'^type_store/$',                      login_required(TypeStorePage.as_view()),         name="type_store"),
    url(r'^store_list/$',                      login_required(StoreList.as_view()),             name="store_list"),
    url(r'^store_add/$',                       login_required(StoreAdd.as_view()),              name='store_add'),
    url(r'^store_detail/(?P<pk>\d+)/$',        login_required(StoreDetail.as_view()),           name='store_detail'),
    url(r'^store_edit/(?P<pk>\d+)/$',          login_required(StoreEdit.as_view()),             name='store_edit'),
    #url(r'^type_target/$',                     login_required(TypeTargetPage.as_view()),        name="type_target"),
    url(r'^target_list/$',                     login_required(TargetList.as_view()),            name="target_list"),
    url(r'^target_add/$',                      login_required(TargetAdd.as_view()),             name='target_add'),
    url(r'^target_detail/(?P<pk>\d+)/$',       login_required(TargetDetail.as_view()),          name='target_detail'),
    url(r'^target_edit/(?P<pk>\d+)/$',         login_required(TargetEdit.as_view()),            name='target_edit'),
    #url(r'^type_delivery/$',                   login_required(TypeDeliveryPage.as_view()),      name="type_delivery"),
    #url(r'^type_part/$',                       login_required(TypePartPage.as_view()),          name="type_part"),
    url(r'^part_list/$',                       login_required(PartList.as_view()),              name="part_list"),
    url(r'^part_add/$',                        login_required(PartAdd.as_view()),               name='part_add'),
    url(r'^part_detail/(?P<pk>\d+)/$',         login_required(PartDetail.as_view()),            name='part_detail'),
    url(r'^part_edit/(?P<pk>\d+)/$',           login_required(PartEdit.as_view()),              name='part_edit'),
    #url(r'^type_consumer/$',                   login_required(TypeConsumerPage.as_view()),      name="type_consumer"),
    url(r'^consumer_list/$',                   login_required(ConsumerList.as_view()),          name="consumer_list"),
    url(r'^consumer_add/$',                    login_required(ConsumerAdd.as_view()),           name='consumer_add'),
    url(r'^consumer_detail/(?P<pk>\d+)/$',     login_required(ConsumerDetail.as_view()),        name='consumer_detail'),
    url(r'^consumer_edit/(?P<pk>\d+)/$',       login_required(ConsumerEdit.as_view()),          name='consumer_edit'),
    #url(r'^type_issue/$',                      login_required(TypeIssuePage.as_view()),         name="type_issue"),
]


#EOF