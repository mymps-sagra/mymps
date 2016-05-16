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
from .models import Issue, Position_issue
from .forms import IssueForm, PositionForm

APP = 'expense'


class MyExpensesContextMixin(ContextMixin):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["app_code"] = APP
        context["app_name"] = apps.get_app_config(APP).verbose_name
        submenus = [
            {"url": "issue_list",          "model": Issue},
            {"url": "position_issue_list", "model": Position_issue},
        ]
        for submenu in submenus:
            submenu["model_name"] = submenu["model"]._meta.verbose_name_plural
        context["submenus"] = submenus
        return context


class ExpenseMenu(TemplateView, MyContextMixin, MyExpensesContextMixin):
    template_name = APP + "/expense_menu.html"


class IssueList(ListView, MyPageNumberContextMixin, MyModelContextMixin, 
    MyExpensesContextMixin):
    model = Issue
    queryset = model.objects.order_by("-date", "name")
    paginate_by = 5
    allow_empty = True


class IssueGet(CommonPositionSetGet, MyPageNumberContextMixin, MyModelContextMixin):
    model = Issue
    modelinline = Position_issue
    Form = IssueForm
    FormSet = inlineformset_factory(model, modelinline, form=PositionForm, 
        fk_name="issue", min_num=1, extra=5)
    form = Form()
    formset = FormSet()
    back_url = 'issue_list'


class IssueAdd(CommonPositionSetAdd, IssueGet):
    success_url = 'issue_list'
    template_name = APP + "/issue_form.html"


class IssueDetail(CommonPositionSetDetail, IssueGet):
    model = Issue
    modelinline = Position_issue
    FormSet = inlineformset_factory(model, modelinline, form=PositionForm, 
        fk_name="issue", extra=0, can_delete=False)
    template_name = APP + "/issue_detail.html"


class IssueEdit(CommonPositionSetEdit, IssueAdd):
    pass


class PositionList(ListView, MyPageNumberContextMixin, MyModelContextMixin, 
    MyModelSetContextMixin, MyExpensesContextMixin):
    model = Position_issue
    model_set = [Issue]
    queryset = model.objects.order_by("item", "-modifyed",)
    paginate_by = 5
    allow_empty = True


#EOF
