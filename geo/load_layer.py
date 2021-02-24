import os
from django.contrib.gis.utils import LayerMapping
from .models import Maha1

maha1_mapping = {
    'id_0': 'ID_0',
    'iso': 'ISO',
    'name_0': 'NAME_0',
    'id_1': 'ID_1',
    'name_1': 'NAME_1',
    'type_1': 'TYPE_1',
    'engtype_1': 'ENGTYPE_1',
    'nl_name_1': 'NL_NAME_1',
    'varname_1': 'VARNAME_1',
    'geom': 'MULTIPOLYGON',
}


maha_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/IND_adm1.shp'))

def run(verbose=True):
    lm = LayerMapping(Maha1, maha_shp, maha1_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)
