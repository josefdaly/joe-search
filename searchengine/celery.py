from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'searchengine.settings')

app = Celery('searchengine')
app.conf.enable_utc = False

app.config_from_object(settings, namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")

@app.task(bind=False)
def call_command_task(command_name):
    call_command(command_name)
