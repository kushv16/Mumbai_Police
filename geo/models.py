from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager


class Incidences(models.Model):
    name = models.CharField(max_length=50)
    location = models.PointField(srid=4326, max_length=500)
    objects = GeoManager()

    class Meta:
        verbose_name_plural = 'Incidences'


class Maha1(models.Model):
    id_0 = models.BigIntegerField()
    iso = models.CharField(max_length=3)
    name_0 = models.CharField(max_length=75)
    id_1 = models.BigIntegerField()
    name_1 = models.CharField(max_length=75)
    type_1 = models.CharField(max_length=50)
    engtype_1 = models.CharField(max_length=50)
    nl_name_1 = models.CharField(max_length=50)
    varname_1 = models.CharField(max_length=150)
    geom = models.MultiPolygonField(srid=4326)


