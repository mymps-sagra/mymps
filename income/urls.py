"""inсome URL Configuration

Приход
"""
from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from .views import IncomeMenu
from .views import DeliveryList, DeliveryAdd, DeliveryEdit, DeliveryDetail
from .views import PositionList


urlpatterns = [
    url(r'^$',                             login_required(IncomeMenu.as_view()),     name="income"),
    url(r'^delivery_list/$',               login_required(DeliveryList.as_view()),   name="delivery_list"),
    url(r'^delivery_add/$',                login_required(DeliveryAdd.as_view()),    name='delivery_add'),
    url(r'^delivery_detail/(?P<pk>\d+)/$', login_required(DeliveryDetail.as_view()), name='delivery_detail'),
    url(r'^delivery_edit/(?P<pk>\d+)/$',   login_required(DeliveryEdit.as_view()),   name='delivery_edit'),
    url(r'^position_delivery_list/$',      login_required(PositionList.as_view()),   name="position_delivery_list"),
]


#EOF