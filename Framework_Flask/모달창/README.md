### 모달 창 개발

### 주의 점
- 모달 창 Key
    - Overlay Div와 Modal Content Div
    - CSS Display : None 과 Block(flex) 반복
    - CSS Position : absolute, top:0, left:0
    - CSS Z-index : Overlay는 최상단으로

### Structure
```
├── static/css
│   └── modal.css
│
├── templates 
│   └── modal.html  // 모달 페이지
│
└── app.py         // 진입점
``` 