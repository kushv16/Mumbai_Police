from django.contrib import admin
from .models import Maha, Incidences
from leaflet.admin import LeafletGeoAdmin


class IncidencesAdmin(LeafletGeoAdmin):
    list_display = ['name', 'location']

class MahaAdmin(LeafletGeoAdmin):
    pass

admin.site.register(Incidences, IncidencesAdmin)
admin.site.register(Maha, MahaAdmin)