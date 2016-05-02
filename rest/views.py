from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.views.generic.base import ContextMixin
from django.apps import apps
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
#from django.views.generic.edit import FormMixin
#from django.forms.models import BaseInlineFormSet
#from django.forms.models import inlineformset_factory, modelform_factory
from django.core.urlresolvers import reverse_lazy, reverse
from django.template.loader import render_to_string
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.http import Http404
from common.mycontext import MyContextMixin, MyPageNumberContextMixin, \
    MyModelContextMixin, MyModelSetContextMixin
from rest.models import Period, Turnover, Rest
from refer.views import CommonEdit, CommonDetail
from rest.forms import PeriodForm, TurnoverForm, RestForm
import datetime
import tempfile
import os
import shutil
from zipfile import ZipFile, ZIP_DEFLATED


APP = 'rest'


class MyRestsContextMixin(ContextMixin):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["app_code"] = APP
        context["app_name"] = apps.get_app_config(APP).verbose_name
        submenus = [
            {"url": "period_list",      "model": Period,   "param": ""},
            {"url": "turnover_list",    "model": Turnover, "param": 0},
            {"url": "rest_list",        "model": Rest,     "param": 0},
        ]
        for submenu in submenus:
            submenu["model_name"] = submenu["model"]._meta.verbose_name_plural
        context["submenus"] = submenus
        return context


class RestMenu(TemplateView, MyContextMixin, MyRestsContextMixin):
    template_name = APP + "/rest_menu.html"


class PeriodList(ListView, MyPageNumberContextMixin, MyModelContextMixin, 
    MyRestsContextMixin):
    model = Period
    queryset = model.objects.order_by("-date", "name")
    paginate_by = 5
    allow_empty = True


class PeriodDetail(CommonDetail):
    model = Period
    form_class = PeriodForm


class PeriodEdit(CommonEdit, UpdateView):
    model = Period
    success_url = 'period_detail'

    def get_success_url(self, **kwargs):
        return reverse(self.success_url, kwargs={'pk': self.object.pk}) + \
            "?page=" + self.request.GET.get("page", "1")


class PeriodAdd(CommonEdit, CreateView):
    model = Period
    success_url = 'period_detail'

    def get_success_url(self, **kwargs):
        return reverse(self.success_url, kwargs={'pk': self.object.pk}) + \
            "?page=" + self.request.GET.get("page", "1")


def turnover_get_queryset_sql(period):
    period_id = 0
    date_from = None
    date_to = None
    stores_id = []
    targets_id = []
    stores_only_blank = None
    targets_only_blank = None
    if period:
        period_id = period.id
        date_from = period.date_from
        date_to = period.date_to
        stores_id = [object.id for object in period.stores.all()]
        targets_id = [object.id for object in period.targets.all()]
        stores_only_blank = period.stores_only_blank
        targets_only_blank = period.targets_only_blank
    #print('stores_id=', stores_id)
    #print('targets_id=', targets_id)
    #print(date_from)
    #if not date_from :
    #    date_from = datetime.datetime.now()
    #print(date_from)
    #group_by_null = \
    #    'IFNULL(item_id, 0) as item_id, ' + \
    #    'IFNULL(design_id, 0) as design_id, ' +\
    #    'IFNULL(packing_id, 0) as packing_id, ' +\
    #    'IFNULL(unit_id, 0) as unit_id, ' +\
    #    'IFNULL(store_id, 0) as store_id, ' +\
    #    'IFNULL(target_id, 0) as target_id, ' +\
    #    'IFNULL(part_id, 0) as part_id '
    group_by = \
        'item_id, design_id, packing_id, unit_id, store_id, target_id, part_id '
    from_table_income = 'FROM income_position_delivery p ' + \
        'LEFT JOIN income_delivery d ON p.delivery_id = d.id '
    from_table_expense = 'FROM expense_position_issue p ' + \
        'LEFT JOIN expense_issue d ON p.issue_id = d.id '
    where =  "WHERE d.executed > 0 "
    if stores_only_blank:
        where +=  "AND d.store_id IS NULL " 
    elif len(stores_id) > 0:
        if len(stores_id) == 1:
            where +=  "AND d.store_id = %s " % stores_id[0]
        else:
            where +=  "AND d.store_id IN %s " % str(tuple(stores_id))
    if targets_only_blank:
        where +=  "AND d.target_id IS NULL " 
    elif len(targets_id) > 0:
        if len(targets_id) == 1:
            where +=  "AND d.target_id = %s " % targets_id[0]
        else:
            where +=  "AND d.target_id IN %s " % str(tuple(targets_id))
    if date_from:
        where_init = "AND d.date < date('%s') " % \
            datetime.datetime.strftime(date_from, "%Y-%m-%d")
        query_init_income = 'SELECT ' + \
            'p.id as id, %s as period_id, ' + group_by + ', ' +\
            'quantity as rest_init, 0 as quantity_in, 0 as quantity_out ' + \
            from_table_income + \
            where + where_init
        params_init = (
            period_id,
        )
        query_init_income_subs = query_init_income % params_init
        query_init_expense = 'SELECT ' + \
            'p.id as id, %s as period_id, ' + group_by + ', ' +\
            '-quantity as rest_init, 0 as quantity_in, 0 as quantity_out ' + \
            from_table_expense + \
            where + where_init
        query_init_expense_subs = query_init_expense % params_init
        query_init_subs = query_init_income_subs + ' UNION ALL ' + \
            query_init_expense_subs
    else:
        query_init_subs = None
    #print(query_init)
    #print(params_init)
    #print(query_init % params_init)
    where_period =  ""
    if date_from:
        where_period += "AND d.date >= date('%s') " % \
            datetime.datetime.strftime(date_from, "%Y-%m-%d")
    if date_to:
        where_period += "AND d.date <= date('%s') " % \
            datetime.datetime.strftime(date_to, "%Y-%m-%d")
    query_period_income = 'SELECT ' + \
        'p.id as id, %s as period_id, ' + group_by + ', ' +\
        '0 as rest_init, quantity as quantity_in, 0 as quantity_out ' + \
        from_table_income + \
        where + where_period
    params_period = (
        period_id,
    )
    query_period_income_subs = query_period_income % params_period
    query_period_expense = 'SELECT ' + \
        'p.id as id, %s as period_id, ' + group_by + ', ' +\
        '0 as rest_init, 0 as quantity_in, quantity as quantity_out ' + \
        from_table_expense + \
        where + where_period
    query_period_expense_subs = query_period_expense % params_period
    query_period_subs = query_period_income_subs + ' UNION ALL ' + \
        query_period_expense_subs
    #print(query_init_subs)
    #print(query_period_subs)
    #
    # SQLite НЕ РАБОТАЕТ СО СЛОВАРЕМ !
    #
    # query = 'SELECT id, %(period)s as period_id, item_id, design_id, packing_id, unit_id, SUM(quantity) as quantity_in FROM income_position GROUP BY item_id, design_id, packing_id, unit_id'
    #params = {}
    #params['period'] = self.period.id
    #print(query % params)
    #self.queryset = self.model.objects.raw(query, params)
    # SQLite НЕ ПОЛУЧИЛОСЬ ПЕРЕДАТЬ СПИСОК ПАРАМЕТРОВ !
    #self.queryset = self.model.objects.raw(query_init, params=params_init)
    query = query_period_subs
    if query_init_subs:
        query += ' UNION ALL ' + query_init_subs
    #print(query)
    query_group = 'SELECT id, ' + group_by + ', ' +\
        'SUM(rest_init) as rest_init, SUM(quantity_in) as quantity_in, ' + \
        'SUM(quantity_out) as quantity_out ' + \
        'FROM ( ' + query + ' )' + \
        'GROUP BY ' + group_by + \
        'HAVING rest_init <> 0 OR quantity_in <> 0 OR quantity_out <> 0 ' 
    #print(query_group)
    query_sum = 'SELECT *, rest_init + quantity_in - quantity_out as rest_total ' + \
        'FROM ( ' + query_group + ' )'
    queryset = Turnover.objects.raw(query_sum)
    #self.queryset = self.model.objects.raw(query_group)
    #print(self.queryset)
    return list(queryset)


def model_object_get(model, **kwargs):
    object = None
    if not "pk" in kwargs:
        raise Http404(model._meta.verbose_name + " not 'pk' in request")
    pk = kwargs["pk"]
    if not pk == "0":
        try:
            object = model.objects.get(pk = pk)
        except ObjectDoesNotExist:
            raise Http404(model._meta.verbose_name + " does not exist pk= " + pk )
    return object


class TurnoverList(ListView, MyPageNumberContextMixin, MyModelContextMixin, 
    MyModelSetContextMixin, MyRestsContextMixin):
    model = Turnover
    model_set = [Period]
    #queryset = model.objects.raw('SELECT id, (1) as period_id, item_id, design_id, packing_id, unit_id, quantity as quantity_in FROM income_position' )
    #print(queryset)
    #print((list(queryset)))
    queryset = None
    paginate_by = 5
    allow_empty = True
    period = None
    template_name = APP + "/turnover_list.html"

    def get(self, request, *args, **kwargs):
        self.period = model_object_get(Period, **kwargs)
        self.queryset = turnover_get_queryset_sql(self.period)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #print(context)
        context["model_verbose_name"] = self.model._meta.verbose_name_plural
        context['period'] = self.period
        return context


def rest_get_queryset_sql(period):
    period_id = 0
    date_to = None
    stores_id = []
    targets_id = []
    stores_only_blank = None
    targets_only_blank = None
    if period:
        period_id = period_id
        date_to = period.date_to
        stores_id = [object.id for object in period.stores.all()]
        targets_id = [object.id for object in period.targets.all()]
        stores_only_blank = period.stores_only_blank
        targets_only_blank = period.targets_only_blank
    group_by = \
        'item_id, design_id, packing_id, unit_id, store_id, target_id, part_id '
    from_table_income = 'FROM income_position_delivery p ' + \
        'LEFT JOIN income_delivery d ON p.delivery_id = d.id '
    from_table_expense = 'FROM expense_position_issue p ' + \
        'LEFT JOIN expense_issue d ON p.issue_id = d.id '
    where =  "WHERE d.executed > 0 "
    if stores_only_blank:
        where +=  "AND d.store_id IS NULL " 
    elif len(stores_id) > 0:
        if len(stores_id) == 1:
            where +=  "AND d.store_id = %s " % stores_id[0]
        else:
            where +=  "AND d.store_id IN %s " % str(tuple(stores_id))
    if targets_only_blank:
        where +=  "AND d.target_id IS NULL " 
    elif len(targets_id) > 0:
        if len(targets_id) == 1:
            where +=  "AND d.target_id = %s " % targets_id[0]
        else:
            where +=  "AND d.target_id IN %s " % str(tuple(targets_id))
    where_period =  ""
    if date_to:
        where_period += "AND d.date <= date('%s') " % \
            datetime.datetime.strftime(date_to, "%Y-%m-%d")
    query_period_income = 'SELECT ' + \
        'p.id as id, %s as period_id, ' + group_by + ', ' +\
        'quantity as rest_total ' + \
        from_table_income + \
        where + where_period
    params_period = (
        period_id,
    )
    query_period_income_subs = query_period_income % params_period
    query_period_expense = 'SELECT ' + \
        'p.id as id, %s as period_id, ' + group_by + ', ' +\
        '-quantity as rest_total ' + \
        from_table_expense + \
        where + where_period
    query_period_expense_subs = query_period_expense % params_period
    query_period_subs = query_period_income_subs + ' UNION ALL ' + \
        query_period_expense_subs
    query = query_period_subs
    query_group = 'SELECT id, ' + group_by + ', ' +\
        'SUM(rest_total) as rest_total ' + \
        'FROM ( ' + query + ' )' + \
        'GROUP BY ' + group_by + \
        'HAVING rest_total <> 0 ' 
    queryset = Rest.objects.raw(query_group)
    return list(queryset)


class RestList(ListView, MyPageNumberContextMixin, MyModelContextMixin, 
    MyModelSetContextMixin, MyRestsContextMixin):
    model = Rest
    model_set = [Period]
    queryset = None
    paginate_by = 5
    allow_empty = True
    period = None
    template_name = APP + "/rest_list.html"
    #template_all = APP + "/rest_list_all.txt"
    #temp_file_name = None

    def get(self, request, *args, **kwargs):
        self.period = model_object_get(Period, **kwargs)
        self.queryset = rest_get_queryset_sql(self.period)
        #self.queryset = self.get_queryset_sql(period_id)
        #context = {'object_list': self.queryset}
        #content = render_to_string(self.template_all, context)
        #temp_file = tempfile.NamedTemporaryFile(mode="w", 
        #    dir='media/temp',
        #    prefix='rest_list_all_', suffix='.txt',  delete=False)
        #temp_file.write(content)
        #temp_file.close()
        #(dirName, fileName) = os.path.split(temp_file.name)
        #self.temp_file_name = '/' + 'media/temp' + '/' + fileName
        #self.temp_file_name = temp_file.name
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_verbose_name"] = self.model._meta.verbose_name_plural
        context['period'] = self.period
        #context['temp_file_name'] = self.temp_file_name
        return context


def rest_get(request, *args, **kwargs):
    template = APP + "/rest_get_content.xml"
    zip_name =  "rest_get.zip"
    zip_file = APP + "/templates/" + APP + "/" + zip_name
    if request.method == 'GET':
        period = model_object_get(Period, **kwargs)
        queryset = rest_get_queryset_sql(period)
        context = {'object_list': queryset}
        context['period'] = period
        content = render_to_string(template, context)
        #temp_dir = "temp"
        #if True:
        with tempfile.TemporaryDirectory(dir='temp') as temp_dir:
            #print(temp_dir)
            shutil.copy2(zip_file, temp_dir)
            with ZipFile(temp_dir + "/" + zip_name, "a") as temp_file:
                temp_file.writestr('content.xml', content, ZIP_DEFLATED)
            with open(temp_dir + "/"+ zip_name, "rb")  as temp_file:
                response = HttpResponse(temp_file.read())
            #file_type = 'application/octet-stream'
            file_type = 'application/vnd.oasis.opendocument.spreadsheet'
            response['Content-Type'] = file_type
            #response['charset'] = 'utf-8'
            #response['Content-Length'] = str(os.stat(excel_file_name).st_size)
            # КИРИЛИЦУ в качестве имени файла послать не получилось
            #response['Content-Disposition'] = 'attachment; filename=rest_get.ods'
            response['Content-Disposition'] = 'attachment; filename=Ostatki.ods'
        return response;

#EOF