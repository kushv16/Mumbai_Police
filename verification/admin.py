from django.contrib import admin

from complaints.admin import complaint_status_approve, complaint_status_reject
from .models import VerificationInfo
# Register your models here.

class VerificationInfoAdmin(admin.ModelAdmin):
    readonly_fields = ('propOwnerFullName',
                       'propOwnerContact',
                       'propOwnerEmail',
                       'propOwnerFlatno',
                       'propOwnerAddress',
                       'propOwnerCity',
                       'propOwnerState',
                       'propOwnerCountry',
                       'tenantFullName',
                       'tenantContact',
                       'tenantEmail',
                       'tenantFlatno',
                       'tenantAddress',
                       'tenantCity',
                       'tenantState',
                       'tenantCountry',
                       'tenantDOB',
                       'tenantReason',
                       'tenantOrganisation',
                       'tenantDepartment',
                       'tenantID',
                       'tenantInstitute',
                       'tenantBranch',
                       'desc',
                       'user',
                       'ack_no',

    )


    list_display = ['user','tenantReason', 'admin_status']
    ordering = ['user']
    actions = [complaint_status_approve,complaint_status_reject]

    search_fields = ('propOwnerFullName',"tenantFullName","tenantReason")
    list_filter = ['tenantReason','admin_status']

    def has_add_permission(self, request, obj=None):
        return False



admin.site.register(VerificationInfo,VerificationInfoAdmin)
