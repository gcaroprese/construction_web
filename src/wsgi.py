import sys
import os
from django.core.wsgi import get_wsgi_application
from dj_static import Cling, MediaCling

sys.path.insert(0, os.path.dirname(__file__))
application = Cling(MediaCling(get_wsgi_application()))
