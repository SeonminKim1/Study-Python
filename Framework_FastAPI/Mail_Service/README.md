## FastAPI Mail Service 

### Settings

```
$ pip install fastapi-mail python-dotenv

```

### Make gmail app password
- gmail 2차 인증으로 password 받아야 함


### .env 파일 작성

``` 작성 예시
MAIL_USERNAME=<username - ex.yubi5050>
MAIL_PASSWORD=<app password>
MAIL_FROM=<보내는 이 email>
MAIL_PORT=587
MAIL_SERVER=smtp.gmail.com
```

### API TEST
```
$ POST - http://127.0.0.1:8000/mail/api
$ POST - http://127.0.0.1:8000/mail/api/backgroundtasks

```
{
    "subject" : "메일 제목",
    "message" : "메일 본문",
    "recipient": ["<YOUR EMAIL1>", "<YOUR EMAIL2>"]
}
```
