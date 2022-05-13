## 로그인 with JWT Token

### Structure
```
├── static/css
│   └── login.css
│
├── templates 
│   ├── login.html // 로그인 페이지
│   └── main.html  // 메인 페이지
│
└── app.py         // 진입점
``` 

### API Endpoint
- @app.route('/') => redirect('/login') 
- @app.route('/login') => login.html
- @app.route('/main') => main.html
- @app.route('/api/login', methods=['POST'])

### 기능 설명
- Login / Logout / JWT Token 부여

### Error Handling
- @app.errorhandler(401)
