## 로그인, 회원가입

### Structure
```
├── static 
│   ├── join.css
│   └── login.css
│
├── templates 
│   ├── join.html  // 회원 가입 페이지
│   ├── login.html // 로그인 페이지
│   └── main.html  // 메인 페이지
│
└── app.py         // 진입점
``` 

### API Endpoint
- @app.route('/') => redirect('/login') 
- @app.route('/login') => login.html
- @app.route('/join') => join.html
- @app.route('/main') => main.html
- @app.route('/api/login', methods=['POST'])
- @app.route('/api/join', methods=['POST'])