import os
from django.contrib.gis.utils import LayerMapping
from .models import Maha

maha_mapping = {
    'name': 'NAME',
    'type': 'TYPE',
    'geom': 'MULTIPOLYGON',
}

maha_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/maha.shp'))

def run(verbose=True):
    lm = LayerMapping(Maha, maha_shp, maha_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)
