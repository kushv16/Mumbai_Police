from django.contrib import admin
from .models import complaintsInfo
# Register your models here.


def complaint_status_approve(modeladmin, request, queryset):
    queryset.update(admin_status='approved')

complaint_status_approve.short_description = "Mark selected complaints as approved"



def complaint_status_reject(modeladmin, request, queryset):
    queryset.update(admin_status='rejected')

complaint_status_reject.short_description = "Mark selected complaints as rejected"

class complaintsInfoAdmin(admin.ModelAdmin):

    list_display = ['fullName','crime','datetime', 'admin_status']
    ordering = ['fullName']
    actions = [complaint_status_approve,complaint_status_reject]
    readonly_fields = ('fullName','contact','email','flatno', 'address' ,'city' ,'state' ,'country', 'datetime',
                        'desc','user','ack_no','crime')

    search_fields = ('fullName',"city","datetime","crime")
    list_filter = ['datetime','crime','admin_status']

    def has_add_permission(self, request, obj=None):
        return False


admin.site.register(complaintsInfo,complaintsInfoAdmin)



