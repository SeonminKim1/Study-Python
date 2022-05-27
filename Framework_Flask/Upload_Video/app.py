from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Page
@app.route('/')
def home():
    return render_template('index.html')

# 파일 업로드 방식 
@app.route('/fileupload', methods=['POST'])
def file_upload():
    file = request.files['file'] # 전체적인 파일의 개요 확인
    extension = secure_filename(file.filename).split('.')[-1] 
    f_name = file.filename.replace('.' + extension, '') 

    # 파일 이름 , Local에 Upload 한 이미지 저장
    today = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    filename = f_name + '-' + today  # test1-2022-05-19-14-43-23.jpg
    upload_path = filename + '.' + extension
    file.save(upload_path)  

    return jsonify({'result':'success'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)