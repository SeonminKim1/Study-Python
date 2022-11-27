import time
from celery import Celery

mode = 'rabbitmq'
# mode = 'redis'
if mode == 'rabbitmq':
    celery_task = Celery(
        'celery_app',
        broker="pyamqp://guest@127.0.0.1:5672",
        backend="rpc://",
        # include=['celery_worker']
    )
     
else: # redis
    celery_task = Celery(
        'celery_app',
        broker="redis://localhost:6379",
        backend="redis://localhost:6379",
        # include=['celery_worker'] # celery_worker.py
    )

@celery_task.task
def add_func(x, y):
    time.sleep(2)
    return x + y