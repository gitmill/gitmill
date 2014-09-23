# -*- coding: utf-8 -*-

import os
ROOT = os.path.dirname(os.path.dirname(__file__))

# file path
DATA_ROOT = os.path.join(os.path.dirname(ROOT), 'data')
REPOSITORY_ROOT = os.path.join(DATA_ROOT, 'repository')
USER_ROOT = os.path.join(DATA_ROOT, 'user')
GIT_ROOT = os.path.join(DATA_ROOT, 'git')

# url
PREFIX = ''
SESSION_COOKIE_PATH = '/' + PREFIX
CSRF_COOKIE_PATH = '/' + PREFIX

# protect site from anonymous user
PROTECTED = True

# version derived from hostname
# because docker uses container id as docker name
# this version string is likely to change
import hashlib
VERSION = hashlib.sha1(os.environ.get('HOSTNAME', '')).hexdigest()

# basic configuration
SECRET_KEY = 'ir+$pvr2b!t@8fyesiwhk@s$o##(1+9k_#7+*ymw-f+9271!)i'

DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # app
    'internal',
    'web',
    'user',
    'repository',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "web.context_processors.all",
)

TEMPLATE_DIRS = (
    os.path.join(ROOT, 'template'),
)

ROOT_URLCONF = 'gitmill.urls'
WSGI_APPLICATION = 'gitmill.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DATA_ROOT, 'db.sqlite3'),
        'ATOMIC_REQUESTS': True,
    }
}

# timezone and locale
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
LOCALE_PATHS = (
    os.path.join(ROOT, 'locale'),
)
LANGUAGE_CODE = 'en-us'
LANGUAGE_COOKIE_NAME = 'locale'
LANGUAGE_COOKIE_PATH = '/' + PREFIX
LANGUAGES = (
    ('en-us', u'English (US)'),
    ('zh-cn', u'简体中文'),
)

# static files
STATIC_URL = '/' + PREFIX + 'static/' + VERSION + '/'
STATIC_ROOT = os.path.join(DATA_ROOT, 'static')
STATICFILES_DIRS = (
    os.path.join(ROOT, 'static'),
)

