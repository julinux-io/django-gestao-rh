from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

# Define o settings do Django para nao precisar passar para o celery toda hora
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestao_rh.settings')

app = Celery('gestao_rh')  # Instance of celery

# Read variables settings defined into settings.py,
# The namespace will check only tasks that starts with CELERY
app.config_from_object('django.conf:settings', namespace='CELERY')


# Discovery tasks.py inside of apps
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
