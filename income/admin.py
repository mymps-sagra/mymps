from django.contrib import admin

# Register your models here.
from .models import Delivery, Position_delivery


class DeliveryAdmin(admin.ModelAdmin):
    list_display = ("date", "name", "accessability", "executed", "comment", 
        "created", "modifyed", "id")
    list_editable = ("accessability",)
    list_display_links = ("date", "name",)
    readonly_fields = ("executed", )
    ordering = ("-date", "name")


class Position_deliveryAdmin(admin.ModelAdmin):
    list_display = ("delivery", "number", "accessability", "item", "unit", 
        "quantity", "created", "modifyed", "id")
    list_display_links = ("delivery", "number",)
    ordering = ("delivery", "number", )


admin.site.register(Delivery, DeliveryAdmin)
admin.site.register(Position_delivery, Position_deliveryAdmin)


#EOF


