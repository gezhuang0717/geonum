from os.path import abspath, dirname, join, exists
from pkg_resources import get_distribution

__version__ = get_distribution('geonum').version

_LIBDIR = abspath(dirname(__file__))
LOCAL_TOPO_PATH = join(_LIBDIR, "local_topo_data")

from .base import GeoPoint, GeoVector3D
from .geosetup import GeoSetup
from .topodata import TopoData, TopoDataAccess
from .processing import LineOnGrid, ElevationProfile  
from .mapping import Map
import helpers

if not exists(join(LOCAL_TOPO_PATH, "LOCAL_TOPO_PATHS.txt")):
    f = open(join(LOCAL_TOPO_PATH, "LOCAL_TOPO_PATHS.txt"), "w")
    f.close()
    del f