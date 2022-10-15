from celery import Task


class HelloCeleryTask(Task):
    name = "HelloCeleryTask"

    def run(self):
        return "hello it's celery_web task"
