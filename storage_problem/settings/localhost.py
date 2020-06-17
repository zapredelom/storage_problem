from storage_problem.settings.base import *
import configparser
config = configparser.ConfigParser()
config.read('application.properties')
USE_RELATIONAL_DB=config.getboolean('storage','service.db.relationional')
REDIS_HOST = config.get('storage','redis.host')
REDIS_PORT = config.getint('storage','redis.port')
DATABASES = {
    'default': {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST':'localhost',
        'NAME': "postgres",
        'PASSWORD': 'postgres',
        'USER': 'postgres'
    }
}
}
DB_CONNECTION_URL='postgres+psycopg2://postgres:postgres@localhost:5432/postgres'
POOL_RECYCLE=50
CELERY_BROKER_URL = 'redis://{}'.format(REDIS_HOST)
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://{}:{}/'.format(REDIS_HOST,REDIS_PORT),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}