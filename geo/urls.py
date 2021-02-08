from django.urls import path

from .views import HomePageView, point_datasets, maha_datasets

urlpatterns = [
    path('', HomePageView.as_view(), name = 'map'),
    path('maha_data/', maha_datasets, name = 'data'),
    path('incidence_data/', point_datasets, name = 'incidences')
]