import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'storage_problem.settings.localhost')

app = Celery('storage_problem')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()