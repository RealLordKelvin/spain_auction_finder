from __future__ import absolute_import, unicode_literals
from django.conf import settings
import os

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'auction.settings')

app = Celery('getauctions')

app.config_from_object('django.conf:settings')

app.autodiscover_tasks(settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

