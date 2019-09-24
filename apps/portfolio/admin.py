from django.contrib import admin
from .models import Service, WorkHistory


class ServiceAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'description'
    )


class WorkHistoryAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'description'
    )


admin.site.register(Service, ServiceAdmin)
admin.site.register(WorkHistory, WorkHistoryAdmin)
