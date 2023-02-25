## Django Ninja Boilerplate

```
├── project/			// project 폴터
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py			// 최초 url 진입점
│   └── wsgi.py
├── app1/
│   ├── __init__.py
│   ├── apps.py
│   ├── router/			// router
│   │   ├── user_api.py
│   │   └── profile_api.py
│   ├── service/		// service (business logic)
│   │   ├── user_service.py
│   │   └── profile_service.py
│   ├── schema/			// schema
│   │   ├── user_Schema.py
│   │   └── profile_Schema.py
│   ├── test/			// test code
│   │   ├── test_user.py
│   │   └── test_profile.py
│   └── models.py		// models ORM
├── _utils/ 			// util 함수 폴더
│   ├── aws_service.py
│   └── decorator.py
├── manage.py
├── Dockerfile
└── requirements.txt
```