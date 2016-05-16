"""api URL Configuration

REST api
"""
from django.conf.urls import url
from .views import PeriodList, PeriodDetail, RestList


urlpatterns = [
    url(r'^periods/$',             PeriodList.as_view(),   name="api_period_list"),
    url(r'^periods/(?P<pk>\d+)/$', PeriodDetail.as_view(), name='api_period_detail'),
    url(r'^rests/(?P<pk>\d+)/$',   RestList.as_view(),     name='api_rest_list'),
]


#EOF