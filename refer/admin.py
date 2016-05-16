from django.contrib import admin

# Register your models here.
from .models import TypeBase, Base
from .models import TypeSupplier, Supplier
from .models import TypeDesign, Design
from .models import TypePacking, Packing
from .models import TypeUnit, Unit
from .models import Format
from .models import TypeItem, Item
from .models import TypeManufacturer, Manufacturer
from .models import TypeStore, Store
from .models import TypeTarget, Target
from .models import TypeDelivery
from .models import TypePart, Part
from .models import TypeConsumer, Consumer
from .models import TypeIssue


class ReferCommonAdmin(admin.ModelAdmin):
    list_display = ("name", "accessability", "order", "comment", 
        "created", "modifyed", "id")
    list_editable = ("accessability", "order",)
    list_display_links = ("name",)
    ordering = ("order", "name")


class ReferTypeAdmin(ReferCommonAdmin):
    list_display = ("name", "code", "accessability", "order", "comment", 
        "created", "modifyed",)


class ReferTypedCommonAdmin(ReferCommonAdmin):
    list_display = ("name", "type", "accessability", "order", "comment", 
        "created", "modifyed", "id")


admin.site.register(TypeDelivery, ReferTypeAdmin)
admin.site.register(TypeBase, ReferTypeAdmin)
admin.site.register(Base, ReferTypedCommonAdmin)
admin.site.register(TypeSupplier, ReferTypeAdmin)
admin.site.register(Supplier, ReferTypedCommonAdmin)
admin.site.register(TypeDesign, ReferTypeAdmin)
admin.site.register(Design, ReferTypedCommonAdmin)
admin.site.register(TypePacking, ReferTypeAdmin)
admin.site.register(Packing, ReferTypedCommonAdmin)
admin.site.register(TypeUnit, ReferTypeAdmin)
admin.site.register(Unit, ReferTypedCommonAdmin)
admin.site.register(Format, ReferCommonAdmin)
admin.site.register(TypeItem, ReferTypeAdmin)
admin.site.register(Item, ReferTypedCommonAdmin)
admin.site.register(TypeManufacturer, ReferTypeAdmin)
admin.site.register(Manufacturer, ReferTypedCommonAdmin)
admin.site.register(TypeStore, ReferTypeAdmin)
admin.site.register(Store, ReferTypedCommonAdmin)
admin.site.register(TypeTarget, ReferTypeAdmin)
admin.site.register(Target, ReferTypedCommonAdmin)
admin.site.register(TypePart, ReferTypeAdmin)
admin.site.register(Part, ReferTypedCommonAdmin)
admin.site.register(TypeConsumer, ReferTypeAdmin)
admin.site.register(Consumer, ReferTypedCommonAdmin)
admin.site.register(TypeIssue, ReferTypeAdmin)


#EOF