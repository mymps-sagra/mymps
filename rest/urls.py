"""rest URL Configuration

остаток
"""
from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from rest.views import RestMenu
from rest.views import PeriodList, PeriodAdd, PeriodDetail, PeriodAdd, PeriodEdit
from rest.views import TurnoverList, RestList, rest_get


urlpatterns = [
    url(r'^$',                           login_required(RestMenu.as_view()),     name="rest"),
    url(r'^period_list/$',               login_required(PeriodList.as_view()),   name="period_list"),
    url(r'^period_add/$',                login_required(PeriodAdd.as_view()),    name='period_add'),
    url(r'^period_detail/(?P<pk>\d+)/$', login_required(PeriodDetail.as_view()), name='period_detail'),
    url(r'^period_edit/(?P<pk>\d+)/$',   login_required(PeriodEdit.as_view()),   name='period_edit'),
    url(r'^turnover_list/(?P<pk>\d+)/$', login_required(TurnoverList.as_view()), name='turnover_list'),
    url(r'^rest_list/(?P<pk>\d+)/$',     login_required(RestList.as_view()),     name='rest_list'),
    url(r'^rest_get/(?P<pk>\d+)/$',      login_required(rest_get),               name='rest_get'),
]


#EOF