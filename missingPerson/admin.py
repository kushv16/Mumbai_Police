from django.contrib import admin
from .models import missingPersonInfo
# Register your models here.

def complaint_status_approve(modeladmin, request, queryset):
    queryset.update(admin_status='approved')

complaint_status_approve.short_description = "Mark selected complaints as approved"


def complaint_status_reject(modeladmin, request, queryset):
    queryset.update(admin_status='rejected')

complaint_status_reject.short_description = "Mark selected complaints as rejected"


class missingPersonInfoAdmin(admin.ModelAdmin):
    readonly_fields = ('firstName','lastname','age','gender','color','height','datetime','placemissing','police_st',
                       'desc','image','user','ack_no')

    list_display = ['firstName','lastname','datetime','admin_status']
    ordering = ['firstName','lastname']
    actions = [complaint_status_approve,complaint_status_reject]

    search_fields = ('firstName','lastname',"police_st","placemissing")
    list_filter = ['datetime','police_st','admin_status']


    def has_add_permission(self, request, obj=None):
            return False

admin.site.register(missingPersonInfo,missingPersonInfoAdmin)