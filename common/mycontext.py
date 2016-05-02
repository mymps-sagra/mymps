from django.views.generic.base import ContextMixin

class MyContextMixin(ContextMixin):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_url"] = self.request.path
        context["current_path"] = self.request.get_full_path()
        context["back_url"] = self.request.GET.get("back_url", "")
        context["success_url"] = self.request.GET.get("success_url", "")
        return context


class MyPageNumberContextMixin(MyContextMixin):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pn"] = self.request.GET.get("page", "1")
        return context


class MyModelContextMixin(ContextMixin):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_verbose_name_plural"] = self.model._meta.verbose_name_plural
        fields_name = {}
        for f in self.model._meta.get_fields():
            if hasattr(f, "verbose_name"):
                fields_name[f.name] = f.verbose_name
        context["fields_verbose_name"] = fields_name
        if self.request.user.is_authenticated():
            model_name = self.model.__name__
            model_app = self.model._meta.app_label
            can = {}
            if self.request.user.has_perm(model_app + '.change_' + model_name):
                can["edit"] = True
            if self.request.user.has_perm(model_app + '.add_' + model_name):
                can["add"] = True
            context["can"] = can
        return context


class MyModelSetContextMixin(ContextMixin):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for model in self.model_set:
            model_name = model.__name__
            model_app = model._meta.app_label
            model_tag = model_app + "_" + model_name
            context[model_tag + "_" + "model_verbose_name_plural"] = \
                model._meta.verbose_name_plural
            context[model_tag + "_" + "model_verbose_name"] = \
                model._meta.verbose_name
            fields_name = {}
            for f in model._meta.get_fields():
                if hasattr(f, "verbose_name"):
                    fields_name[f.name] = f.verbose_name
            context[model_tag + "_" + "fields_verbose_name"] = fields_name
        return context


#EOF