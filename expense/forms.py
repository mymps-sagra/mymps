from django import forms

from .models import Issue, Position_issue


class IssueForm(forms.ModelForm):
    
    class Meta:
        model = Issue
        fields = "__all__"
        widgets = {
            "comment": forms.Textarea(attrs={'rows': 3,}),
        }


class PositionForm(forms.ModelForm):
    
    class Meta:
        model = Position_issue
        fields = "__all__"
        widgets = {
            "number": forms.TextInput(attrs={'size': 8,}),
            "precision": forms.TextInput(attrs={'size': 6,}),
            "quantity": forms.TextInput(attrs={'size': 16,}),
        }


#EOF