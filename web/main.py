from fastapi import FastAPI

from tasks import HelloCeleryTask
from celery_main import app as celery_app

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/list_of_celery_tasks")
def list_of_celery_tasks():
    return {'result': str(celery_app.tasks)}


@app.get("/test_celery")
def test_celery():
    result = HelloCeleryTask().delay().get()
    return {"result": result}
