from django.contrib import admin
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
)

admin.site.register(VerificationInfo,VerificationInfoAdmin)
