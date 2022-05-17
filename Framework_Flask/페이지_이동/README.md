### Structure
```
├── templates
│   ├── main.html 
│   └── test.html 
└── app.py          // 진입점
``` 
### 페이지 이동 방법 4가지
- [GET] a 태그 href 속성
- [GET] a 태그 href 속성 + url_for()
- [GET] JS onclick + window.location.href 방식
- [GET, POST] Form - submit 방식
- [GET] Redirect

### API Endpoint
- @app.route('/test/basic', methods=['GET'])
- @app.route('/test/name', methods=['GET'])
- @app.route('/test/animals', methods=['GET', 'POST'])
- @app.route('/test/redir', methods=['GET']) => '/test/name'
