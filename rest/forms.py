from django import forms

from .models import Period, Turnover, Rest


class PeriodForm(forms.ModelForm):
    
    class Meta:
        model = Period
        fields = "__all__"
        widgets = {
            "comment": forms.Textarea(attrs={'rows': 3,}),
        }


class TurnoverForm(forms.ModelForm):
    
    class Meta:
        model = Turnover
        fields = "__all__"
        widgets = {
            "precision": forms.TextInput(attrs={'size': 6,}),
            "rest_init": forms.TextInput(attrs={'size': 16,}),
            "quantity_in": forms.TextInput(attrs={'size': 16,}),
            "quantity_out": forms.TextInput(attrs={'size': 16,}),
            "rest_total": forms.TextInput(attrs={'size': 16,}),
        }


class RestForm(forms.ModelForm):
    
    class Meta:
        model = Rest
        fields = "__all__"
        widgets = {
            "precision": forms.TextInput(attrs={'size': 6,}),
            "rest_total": forms.TextInput(attrs={'size': 16,}),
        }


#EOF