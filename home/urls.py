"""home URL Configuration

Стартовая страница
"""
from django.conf.urls import include, url
from home.views import HomePage


urlpatterns = [
    url(r'^$', HomePage.as_view(), name="home"),
]
