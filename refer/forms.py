from django import forms

from .models import Base, Supplier, Design, Packing, Unit, Format, Item
from .models import Manufacturer, Store, Target, Part, Consumer

class BaseForm(forms.ModelForm):
    
    class Meta:
        model = Base
        fields = "__all__"


class SupplierForm(forms.ModelForm):
    
    class Meta:
        model = Supplier
        fields = "__all__"


class DesignForm(forms.ModelForm):
    
    class Meta:
        model = Design
        fields = "__all__"


class PackingForm(forms.ModelForm):
    
    class Meta:
        model = Packing
        fields = "__all__"


class UnitForm(forms.ModelForm):
    
    class Meta:
        model = Unit
        fields = "__all__"


class FormatForm(forms.ModelForm):
    
    class Meta:
        model = Format
        fields = "__all__"


class ItemForm(forms.ModelForm):
    
    class Meta:
        model = Item
        fields = "__all__"


class ManufacturerForm(forms.ModelForm):
    
    class Meta:
        model = Manufacturer
        fields = "__all__"


class StoreForm(forms.ModelForm):
    
    class Meta:
        model = Store
        fields = "__all__"


class TargetForm(forms.ModelForm):
    
    class Meta:
        model = Target
        fields = "__all__"


class PartForm(forms.ModelForm):
    
    class Meta:
        model = Part
        fields = "__all__"


class ConsumerForm(forms.ModelForm):
    
    class Meta:
        model = Consumer
        fields = "__all__"


#EOF