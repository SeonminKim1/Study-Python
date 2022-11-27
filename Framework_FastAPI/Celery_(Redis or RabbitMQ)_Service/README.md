## Celery Basic Example

### 1. package install
```
$ pip install Celery
$ pip install Redis # if use redis
$ pip install gevent # if use window 
```
### 2. Redis or RabbitMQ on
```
# use redis docker
$ docker run --name my-redis -d redis

# use rabbitmq docker
$ docker run --name rabbitmq-container -p 5671:5671 -p 5672:5672 -p 15672:15672 rabbitmq:management
```

### 3. fastapi 서버, celery 서버 실행
```
$ uvicorn app:app --reload
$ celery -A celery_app worker -l info -P gevent
```

### 4. API Test
```
GET - http://127.0.0.1:8000/worker/add?task_id=smkim&num_1=4&num_2=2
```