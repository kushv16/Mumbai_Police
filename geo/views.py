from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from django.shortcuts import render
from .models import Maha1, Incidences
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.contrib.gis.geoip2 import GeoIP2
from django.http import HttpResponse
from .load_layer import run


def map_home(request):
	# x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	# if x_forwarded_for:
	# 	ip = x_forwarded_for.split(',')[0]
	# else:
	# 	ip = request.META.get('REMOTE_ADDR')
	# g = GeoIP2()
	# (lat, lng) = g.lat_lon(ip)
	lat = 19.0748
	lng = 72.8856
	pnt = Point(lng, lat, srid=4326)
	inc_near = Incidences.objects.annotate(
		distance=Distance('location', pnt)
	).order_by('distance').first()
	# print(inc_near)
	# name = Incidences.objects.filter('name' == inc_near)
	string = str(inc_near.location)
	near_lat = ""
	near_lng = ""
	take1 = True
	go = False
	for i in string:
		if i == '(':
			go = True
			continue
		if i == ')':
			break
		if go:
			if i == " ":
				take1 = False
			elif take1:
				near_lng += i
			else:
				near_lat += i

	all_incidences = Incidences.objects.all()
	context = {
		'lng': lng,
		'lat': lat,
		'near_lat': near_lat,
		'near_lng': near_lng,
		'all_incidences': all_incidences,
	}
	return render(request, 'geo/index.html', context)


def maha_datasets(request):
	names = serialize('geojson', Maha1.objects.all())
	return HttpResponse(names,content_type='json')

def point_datasets(request):
	points = serialize('geojson', Incidences.objects.all())
	return HttpResponse(points,content_type='json')