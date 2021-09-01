import os

from celery import Celery
from celery.schedules import crontab


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crypcentra.settings")

app = Celery("crypcentra")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.beat_schedule = {
    "add-every-30-seconds": {"task": "tasks.add", "schedule": 30.0, "args": (16, 16)},
}
app.conf.timezone = "UTC"

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
