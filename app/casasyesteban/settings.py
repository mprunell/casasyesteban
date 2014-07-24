from django.conf import global_settings
"""
Django settings for casasyesteban project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
try:
    from secrets import *
except ImportError:
    pass


DEBUG = True
TEMPLATE_DEBUG = DEBUG

BASE_DIR = os.path.join(os.path.dirname(__file__), '../..')
APP_DIR = os.path.join(os.path.dirname(__file__), '..')


def rel_base(*x):
    """ Get path to file in the base directory.
    """
    return os.path.join(BASE_DIR, *x)


def rel_app(*x):
    """ Get path to file in the app directory.
    """
    return os.path.join(APP_DIR, *x)


ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = None

ALLOWED_HOSTS = []

TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en'

SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = True


MEDIA_ROOT = rel_app('media')
MEDIA_URL = '/media/'

STATIC_ROOT = rel_app('assets')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    rel_app('static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)


TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.core.context_processors.media',
)

TEMPLATE_DIRS = (
    rel_app('templates/'),
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i6oplc+0hma^fhj+4q%w5yq6-k7#1unob8ve^&5&k_svl1upiu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

# Application definition

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'south',
    'pages',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'casasyesteban.urls'

WSGI_APPLICATION = 'casasyesteban.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
