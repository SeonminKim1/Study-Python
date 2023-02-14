### CRUD Example
- Django Create, Read, Update, Delete Example

### Structure
```
├── article  // app
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   └── ...
├── crud     // project
│   ├── urls.py       
│   ├── settings.py    
│   └── ...
└── ... 
``` 

### API Endpoint
- / : 조회
- crud_create/ : 생성
- crud_update/ : 수정
- crud_delete/<int:number> :  삭제
- admin/ 
