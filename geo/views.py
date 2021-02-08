from django.shortcuts import render
from .models import Maha, Incidences
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse

class HomePageView(TemplateView):
	template_name = 'index.html'

def maha_datasets(request):
	names = serialize('geojson', Maha.objects.all())
	return HttpResponse(names,content_type='json')

def point_datasets(request):
	points = serialize('geojson', Incidences.objects.all())
	return HttpResponse(points,content_type='json')
