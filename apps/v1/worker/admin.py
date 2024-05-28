from django.contrib import admin

from apps.v1.worker.models import Worker, Unit, Visit


# Register your models here.
class WorkerAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'phone_number']


admin.site.register(Worker, WorkerAdmin)


class UnitAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'worker']


admin.site.register(Unit, UnitAdmin)


class VisitAdmin(admin.ModelAdmin):
    search_fields = ['unit__name', 'unit__worker__name']
    list_display = ['unit', 'datetime', 'latitude', 'longitude']

    # Disable adding
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    # Disable deleting
    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Visit, VisitAdmin)
