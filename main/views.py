from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
from common.mycontext import MyContextMixin

class MainPage(TemplateView, MyContextMixin):
  template_name = "mainpage.html"
