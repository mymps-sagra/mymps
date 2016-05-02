from django.contrib import admin

# Register your models here.
from refer.models import TypeBase, Base
from refer.models import TypeSupplier, Supplier
from refer.models import TypeDesign, Design
from refer.models import TypePacking, Packing
from refer.models import TypeUnit, Unit
from refer.models import Format
from refer.models import TypeItem, Item
from refer.models import TypeManufacturer, Manufacturer
from refer.models import TypeStore, Store
from refer.models import TypeTarget, Target
from refer.models import TypeDelivery
from refer.models import TypePart, Part
from refer.models import TypeConsumer, Consumer
from refer.models import TypeIssue


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