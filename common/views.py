from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormMixin
from django.forms.models import inlineformset_factory
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404


class CommonPositionSetGet(FormMixin):
    model = None
    modelinline = None
    Form = None
    FormSet = None
    form = None
    formset = None
    object = None

    def get_obj(self, **kwargs):
        if not "pk" in kwargs:
            raise Http404(self.model._meta.verbose_name + \
                " not 'pk' in request")
        pk = kwargs["pk"]
        try:
            self.object = self.model.objects.get(pk = pk)
        except ObjectDoesNotExist:
            raise Http404(self.model._meta.verbose_name + \
                " does not exist pk= " + pk )
            
    def get_forms(self, **kwargs):
        self.get_obj(**kwargs)
        self.form = self.Form(instance = self.object)
        self.formset = self.FormSet(instance = self.object)
        field_q = "quantity"
        field_p = "precision"
        for form in self.formset:
            if field_q in form.initial and field_p in form.initial:
                precision = form.initial[field_p]
                quantity = form.initial[field_q]
                if precision > 0:
                    quantity = round(quantity, precision)
                else:
                    quantity = round(quantity, 0)
                form.initial[field_q] = quantity
                
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_verbose_name"] = self.model._meta.verbose_name_plural
        context['object'] = self.object
        context['form'] = self.form
        context['formset'] = self.formset
        formseterrors = []
        if self.formset:
            for form in self.formset:
                for source, errs in form.errors.items():
                    if source == "__all__":
                        for err in errs:
                            formseterrors.append(err)
        context['formseterrors'] = formseterrors
        return context


class CommonPositionSetAdd(TemplateView, CommonPositionSetGet):
    success_url = None
    template_name = None

    def get_success_url(self, **kwargs):
        return reverse(self.success_url) + \
            "?page=" + self.request.GET.get("page", "1")

    def post(self, request, *args, **kwargs):
        self.success_url = self.request.GET.get('success_url', self.success_url)
        self.form = self.Form(request.POST, instance = self.object)
        self.formset = self.FormSet(request.POST, instance = self.object)
        if self.form.is_valid() and self.formset.is_valid():
            self.object = self.form.save()
            self.formset = self.FormSet(request.POST, instance = self.object)
            if self.formset.is_valid():
                self.formset.save()
                return redirect(self.get_success_url())
        return super().get(request, *args, **kwargs)


class CommonPositionSetDetail(TemplateView, CommonPositionSetGet):
    model = None
    modelinline = None
    FormSet = None
    template_name = None

    def get(self, request, *args, **kwargs):
        self.get_forms(**kwargs)
        for f in self.form.fields:
            self.form.fields[f].widget.attrs['disabled'] = 'disabled'
        for form in self.formset:
            for f in form.fields:
                form.fields[f].widget.attrs['disabled'] = 'disabled'
        return super().get(request, *args, **kwargs)


class CommonPositionSetEdit(CommonPositionSetAdd):

    def get(self, request, *args, **kwargs):
        self.get_forms(**kwargs)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.get_obj(**kwargs)
        return super().post(request, *args, **kwargs)


#EOF
