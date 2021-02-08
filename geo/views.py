from django.shortcuts import render
from .models import Maha, Incidences
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.contrib.gis.geoip2 import GeoIP2
from django.http import HttpResponse

def map_home(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = request.META.get('REMOTE_ADDR')
	g = GeoIP2()
	lat, lng = g.lat_lon(ip)
	#template_name = 'index.html'
	context = {
		'lat':lat,
		'lng':lng,
	}
	return render(request, 'geo/index.html', context)



def maha_datasets(request):
	names = serialize('geojson', Maha.objects.all())
	return HttpResponse(names,content_type='json')

def point_datasets(request):
	points = serialize('geojson', Incidences.objects.all())
	return HttpResponse(points,content_type='json')