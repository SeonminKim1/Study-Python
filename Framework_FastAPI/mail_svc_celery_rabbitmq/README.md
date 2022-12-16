## Celery Basic Example

### 1. package install
```
$ pip install fastapi-mail python-dotenv
$ pip install Celery
$ pip install Redis # if use redis
$ pip install gevent # if use window 
```
### 2. Redis or RabbitMQ Broker
```
# use redis broker docker
$ docker run --name my-redis -d redis

# use rabbitmq broker docker
$ docker run --name rabbitmq-container -p 5671:5671 -p 5672:5672 -p 15672:15672 rabbitmq:management
```

### 3. Make gmail app password
gmail 2차 인증으로 password 

### 4. .env 파일 작성
```
MAIL_USERNAME=<username - ex.yubi5050>
MAIL_PASSWORD=<app password>
MAIL_FROM=<보내는 이 email>
MAIL_PORT=587
MAIL_SERVER=smtp.gmail.com
```

### 5. fastapi 서버, celery 서버 실행
```
$ uvicorn app:app --reload
$ celery -A celery_app worker

# if window
$ celery -A celery_app worker -l info -P gevent
```

### 6. API Test
```
POST - http://127.0.0.1:8000/mail/api
body = {
    "subject" : "메일 제목",
    "message" : "메일 본문",
    "recipient": ["email@email.com"]
}
```