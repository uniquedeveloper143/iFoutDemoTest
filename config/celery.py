# my_project/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings  # Add this to access Django settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')  # development need to replace with production in production 

app = Celery('config')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# namespace='CELERY' means all celery-related configuration keys
# should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Check if settings are properly loaded
# print("BROKER URL:", settings.CELERY_BROKER_URL)  # This should print the correct Redis URL


# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


# run redis command
# celery -A project_name worker -l INFO
# celery -A config worker --loglevel=info # here config is project name
# celery -A config worker -l info  # For executing tasks
# celery -A config beat -l info  # For scheduling tasks


#Install redis in ubunto
# sudo apt-get install redis-server
# run redis
# sudo systemctl start redis-server
# sudo systemctl status redis-server
# sudo systemctl restart redis-server

# Run the Celery shell and inspect all the loaded settings. Start the Celery shell:
# celery -A config shell
# app.conf.broker_url  # This should return 'redis://localhost:6379/0'
# app.conf.result_backend  # This should return 'redis://localhost:6379/0'


# Kill existing Celery workers (to ensure no old processes are interfering):
# pkill -f 'celery worker'