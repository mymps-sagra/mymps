"""inсome URL Configuration

Расход
"""
from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from .views import ExpenseMenu
from .views import IssueList, IssueAdd, IssueDetail, IssueEdit
from .views import PositionList


urlpatterns = [
    url(r'^$',                          login_required(ExpenseMenu.as_view()),  name="expense"),
    url(r'^issue_list/$',               login_required(IssueList.as_view()),    name="issue_list"),
    url(r'^issue_add/$',                login_required(IssueAdd.as_view()),     name='issue_add'),
    url(r'^issue_detail/(?P<pk>\d+)/$', login_required(IssueDetail.as_view()),  name='issue_detail'),
    url(r'^issue_edit/(?P<pk>\d+)/$',   login_required(IssueEdit.as_view()),    name='issue_edit'),
    url(r'^position_issue_list/$',      login_required(PositionList.as_view()), name="position_issue_list"),
]


#EOF