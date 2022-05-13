## Jinja Include Tag

### Tag 사용 법
- {% Include 'a.html' %}
- <nav> <div> 등의 코드를 작성하고 nav.html, div1.html 등으로 저장한다.
- main.html 에서 {% include 'nav/nav.html' %} 등으로 사용
- 복잡한 div 구조를 가지거나 공통되는 영역 (nav 등)이 있을 때 빼서 쓰기 좋다.

### Structure
```
├── static/css
│   └── include_ex.css
│
├── templates 
│   ├── nav.html   // nav
│   ├── div1.html  // div1
│   ├── div2.html  // div2
│   └── main.html  // main
│
└── app.py         // 진입점
``` 
