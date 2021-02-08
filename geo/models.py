from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager


class Incidences(models.Model):
    name = models.CharField(max_length=50)
    location = models.PointField(srid=4326, max_length=500)
    objects = GeoManager()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Incidences'


class Maha(models.Model):
    name = models.CharField(max_length=101)
    type = models.CharField(max_length=6)
    geom = models.MultiPolygonField(srid=4326)

    def __unicode__(self):
        return self.name
