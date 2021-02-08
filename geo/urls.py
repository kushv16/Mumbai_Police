from django.urls import path

from .views import map_home, point_datasets, maha_datasets

urlpatterns = [
    path('', map_home, name = 'map'),
    path('maha_data/', maha_datasets, name = 'data'),
    path('incidence_data/', point_datasets, name = 'incidences')
]