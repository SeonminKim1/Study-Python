### URL Practice
- Separate from only Project/urls.py into Project/urls.py and APP/urls.py  

### Key code
- path('test1/', views.http_response_view) // HTTP Response
- path('test4/', include('p_app1.urls')), // p_app1의 url들과 연결

### Structure
```
├── p_app1  // app
│   ├── urls.py
│   ├── views.py
│   └── ...
├── url_practice   // project
│   ├── urls.py
│   ├── views.py
│   ├── settings.py
│   └── ...
└── ... 
``` 