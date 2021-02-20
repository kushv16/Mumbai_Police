from django.contrib import admin
from .models import criminalsInfo
# Register your models here.


class criminalsInfoAdmin(admin.ModelAdmin):

    list_display = ['firstname','lastname','crime','current_status','date',]
    ordering = ['firstname','lastname']

    search_fields = ('firstname','lastname',"crime","current_status","date")
    list_filter = ['date','crime','current_status']



admin.site.register(criminalsInfo,criminalsInfoAdmin)