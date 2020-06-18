from __future__ import absolute_import, unicode_literals
from django.conf import settings

import subprocess


# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app

__all__ = ('celery_app',)

f = open('./redis_import.sh', 'r')
initial = f.read()
changed = initial.replace('/sample.csv','sample.csv')
changed = changed.replace('$host','')
changed = changed.replace('redis-cli -h $host keys "__"$previous"__*" | xargs redis-cli -h $host del ','')
f.close()
f = open('./redis_import.sh', 'w')
f.write(changed)
f.flush()
f.close()
subprocess.call('./redis_import.sh')
f = open('./redis_import.sh', 'w')
f.write(initial)
f.close()
