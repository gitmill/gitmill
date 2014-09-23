from gitmill.settings import *

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'postgres_1',
        'PORT': '5432',
        'ATOMIC_REQUESTS': True,
    }
}

SESSION_ENGINE = 'redis_sessions.session'
SESSION_REDIS_HOST = 'redis_1'
SESSION_REDIS_PORT = 6379
SESSION_REDIS_DB = 0
SESSION_REDIS_PREFIX = 'session'
