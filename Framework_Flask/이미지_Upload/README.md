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
<table>
<th><td></td><td>File Ver</td><td>Modal ver</td></th>
<tr><td>![1.PNG](readme_img/1.PNG)</td><td>![2.PNG](readme_img/2.PNG)</td><td>![3.PNG](readme_img/3.PNG)</td></tr>
</table>


