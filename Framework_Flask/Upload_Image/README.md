## 이미지 업로드
- File Structure Version
- Modal Version

### Structure
```
├── static/css
│   └── image_upload.css
│
├── imgs
├── templates 
│   ├── index.html         // 메인 페이지
│   └── modal_upload.html  // 모달 Ver html
│
└── app.py // 진입점
``` 

### API Endpoint
- @app.route('/fileupload', methods=['POST'])

### 기능 스크린샷

#### File Ver
<img src="./readme_img/2.PNG" width="350px" height="250px"/>

#### Modal ver
<img src="./readme_img/3.PNG" width="350px" height="250px"/>

