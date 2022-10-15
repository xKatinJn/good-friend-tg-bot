import os

from celery import Celery
from web.profile.tasks import HelloCeleryTask


app = Celery(
    "celery_main",
    broker=os.environ.get("CELERY_BROKER_URL"),
    backend="rpc://",
)
app.autodiscover_tasks()
app.register_task(HelloCeleryTask)
