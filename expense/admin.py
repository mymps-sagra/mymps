from django.contrib import admin

# Register your models here.
from .models import Issue, Position_issue


class IssueAdmin(admin.ModelAdmin):
    list_display = ("date", "name", "accessability", "executed", "comment", 
        "created", "modifyed", "id")
    list_editable = ("accessability",)
    list_display_links = ("date", "name",)
    readonly_fields = ("executed", )
    ordering = ("-date", "name")


class Position_issueAdmin(admin.ModelAdmin):
    list_display = ("issue", "number", "accessability", "item", "unit", 
        "quantity", "created", "modifyed", "id")
    list_display_links = ("issue", "number",)
    ordering = ("issue", "number", )


admin.site.register(Issue, IssueAdmin)
admin.site.register(Position_issue, Position_issueAdmin)


