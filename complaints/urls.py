from django.urls import path
from . import views
urlpatterns = [
    path('', views.complaints, name='complaints-page'),
]