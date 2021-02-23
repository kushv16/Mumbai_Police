from django.contrib import admin

from complaints.admin import complaint_status_approve, complaint_status_reject
from .models import stolenVehiclesInfo
# Register your models here.

# def complaint_status_approve(modeladmin, request, queryset):
#     queryset.update(admin_status='approved')
#
# complaint_status_approve.short_description = "Mark selected complaints as approved"
#
#
# def complaint_status_reject(modeladmin, request, queryset):
#     queryset.update(admin_status='rejected')
#
# complaint_status_reject.short_description = "Mark selected complaints as rejected"

class stolenVehiclesInfoAdmin(admin.ModelAdmin):
    readonly_fields = ('fullName', 'contact' ,'model_name' ,'reg_no' ,'chassis_no', 'engine_no',
                       'datetime' ,'police_station', 'desc','user','ack_no')

    list_display = ['fullName','model_name','datetime', 'admin_status']
    ordering = ['fullName']
    actions = [complaint_status_approve,complaint_status_reject]

    search_fields = ('fullName',"model_name","datetime","police_station")
    list_filter = ['datetime','police_station','admin_status']


    def has_add_permission(self, request, obj=None):
            return False

admin.site.register(stolenVehiclesInfo,stolenVehiclesInfoAdmin)
