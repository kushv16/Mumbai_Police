from django.contrib import admin
from .models import missingPersonInfo
# Register your models here.


class missingPersonInfoAdmin(admin.ModelAdmin):
    readonly_fields = ('firstName','lastname','age','gender','color','height','datetime','placemissing','police_st',
                       'desc','image',)

admin.site.register(missingPersonInfo,missingPersonInfoAdmin)