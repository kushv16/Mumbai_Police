from django.contrib import admin
from .models import stolenVehiclesInfo
# Register your models here.


class stolenVehiclesInfoAdmin(admin.ModelAdmin):
    readonly_fields = ('fullName', 'contact' ,'model_name' ,'reg_no' ,'chassis_no', 'engine_no',
                       'datetime' ,'police_station', 'desc',)

admin.site.register(stolenVehiclesInfo,stolenVehiclesInfoAdmin)
