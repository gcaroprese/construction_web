from settings import *

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
	'KEY_PREFIX': 'construction_site_sample.com',
    }
}

