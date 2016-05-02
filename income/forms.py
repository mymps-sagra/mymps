from django import forms

from income.models import Delivery, Position_delivery


class DeliveryForm(forms.ModelForm):
    
    class Meta:
        model = Delivery
        fields = "__all__"
        widgets = {
            "comment": forms.Textarea(attrs={'rows': 3,}),
        }


class PositionForm(forms.ModelForm):
    
    class Meta:
        model = Position_delivery
        fields = "__all__"
        widgets = {
            "number": forms.TextInput(attrs={'size': 8,}),
            "precision": forms.TextInput(attrs={'size': 6,}),
            "quantity": forms.TextInput(attrs={'size': 16,}),
        }


#EOF