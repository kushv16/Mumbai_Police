from django.contrib import admin
from .models import complaintsInfo
# Register your models here.


class complaintsInfoAdmin(admin.ModelAdmin):
    readonly_fields = ('fullName','contact','email','flatno', 'address' ,'city' ,'state' ,'country', 'datetime',
                       'crime' ,'desc',)

    def has_add_permission(self, request, obj=None):
        return False

admin.site.register(complaintsInfo,complaintsInfoAdmin)