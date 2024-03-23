from os import environ, path

def root(subpath):
    return path.abspath(path.join(path.dirname(path.dirname(__file__)), subpath))

#---------------------------------------------------------------------------------------------------
# General settings
#---------------------------------------------------------------------------------------------------

SITE_NAME = 'Aulet Abiega'

ADMINS = MANAGERS = (
    ('Joni Bekenstein', 'jonibekenstein@gmail.com'),
    ('Ian Klement', 'ianklement@gmail.com'),
)

DEBUG = bool(environ.get('DJANGO_DEBUG'))
TEMPLATE_DEBUG = DEBUG
THUMBNAIL_DEBUG = DEBUG
HTML_MINIFY = not DEBUG

INSTALLED_APPS = (
    'apps.website',
    'apps.projects',
    'apps.contact',

    'grappelli',
    'djrill',
    'htmlmin',
    'markitup',
    'easy_thumbnails',
    'widget_tweaks',
    'django_extensions',

    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

ROOT_URLCONF = 'urls'
WSGI_APPLICATION = 'wsgi.application'

FIXTURE_DIRS = (
    root('src/fixtures'),
)

#---------------------------------------------------------------------------------------------------
# Site
#---------------------------------------------------------------------------------------------------

SITE_ID = 1

#---------------------------------------------------------------------------------------------------
# Security
#---------------------------------------------------------------------------------------------------

SECRET_KEY = environ.get('DJANGO_SECRET_KEY', 'no-secret')
ALLOWED_HOSTS = environ.get('DJANGO_ALLOWED_HOSTS', '*').split(',')
INTERNAL_IPS = environ.get('DJANGO_INTERNAL_IPS', '127.0.0.1').split(',')
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

#---------------------------------------------------------------------------------------------------
# Locale
#---------------------------------------------------------------------------------------------------

LANGUAGE_CODE = 'es-ar'
TIME_ZONE = 'America/Argentina/Buenos_Aires'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LOCALE_PATHS = (
    root('src/locale'),
)

#---------------------------------------------------------------------------------------------------
# Templates
#---------------------------------------------------------------------------------------------------

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'apps.website.context_processors.google_analytics',
)

TEMPLATE_DIRS = (
    root('src/templates'),
)

#---------------------------------------------------------------------------------------------------
# Middleware
#---------------------------------------------------------------------------------------------------

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'htmlmin.middleware.MarkRequestMiddleware',
    'utils.mobile_detection_middleware.MobileDetectionMiddleware',
)

#---------------------------------------------------------------------------------------------------
# Database
#---------------------------------------------------------------------------------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': environ.get('DATABASE_NAME'),
        'USER': environ.get('DATABASE_USER'),
        'PASSWORD': environ.get('DATABASE_PASSWORD'),
        'HOST': environ.get('DATABASE_HOST'),
        'PORT': environ.get('DATABASE_PORT'),
    }
}

#---------------------------------------------------------------------------------------------------
# Cache
#---------------------------------------------------------------------------------------------------

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'LOCATION': '%s:%s:1' % (environ.get('REDIS_HOST'), environ.get('REDIS_PORT')),
        'KEY_PREFIX': SITE_NAME.replace(' ', ''),
        'OPTIONS': {
            'PARSER_CLASS': 'redis.connection.HiredisParser',
        }
    }
}

#---------------------------------------------------------------------------------------------------
# Email
#---------------------------------------------------------------------------------------------------

SERVER_EMAIL = environ.get('SERVER_EMAIL')
DEFAULT_FROM_EMAIL = environ.get('DEFAULT_FROM_EMAIL', '%s <%s>' % (SITE_NAME, SERVER_EMAIL))
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME
EMAIL_HOST_USER = environ.get('EMAIL_HOST_USER', SERVER_EMAIL)
EMAIL_HOST_PASSWORD = environ.get('EMAIL_HOST_PASSWORD')
EMAIL_HOST = environ.get('EMAIL_HOST')
EMAIL_PORT = environ.get('EMAIL_PORT', '587')
EMAIL_USE_TLS = bool(environ.get('EMAIL_USE_TLS', True))

#---------------------------------------------------------------------------------------------------
# Static Files
#---------------------------------------------------------------------------------------------------

STATIC_URL = '/static/'
STATIC_ROOT = root('static')
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
STATICFILES_DIRS = (
    root('static-compiled'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = root('media')

#---------------------------------------------------------------------------------------------------
# Other settings
#---------------------------------------------------------------------------------------------------

MARKITUP_FILTER = ('markdown.markdown', {'safe_mode': True})
MARKITUP_SET = 'markitup/sets/markdown'

THUMBNAIL_BASEDIR = 'cache'
THUMBNAIL_NAMER = 'easy_thumbnails.namers.hashed'
THUMBNAIL_HIGH_RESOLUTION = True

GOOGLE_ANALYTICS = environ.get('GOOGLE_ANALYTICS', '')
GRAPPELLI_ADMIN_TITLE = SITE_NAME

#---------------------------------------------------------------------------------------------------
# Project specific settings
#---------------------------------------------------------------------------------------------------

# TBD...
