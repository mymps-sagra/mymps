"""main URL Configuration

Главная страница
"""
from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from .views import MainPage


urlpatterns = [
    url(r'^$', login_required(MainPage.as_view()), name="main"),
]
