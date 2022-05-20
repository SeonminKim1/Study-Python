from flask import Flask, render_template, request, jsonify, redirect, url_for
from werkzeug.utils import secure_filename
from datetime import datetime
from classifier import get_classification_result
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/img/upload', methods=['POST'])
def file_upload():
    # 업로드 파일 받아오기.
    file = request.files['file'] # werkzeug.datastructures.FileStorage, name
    extension = secure_filename(file.filename).split('.')[-1] # file.filename /
    f_name = file.filename.replace('.' + extension, '') # test1, 확장자 제거

    # 파일 이름 , Local에 Upload 한 이미지 저장
    today = datetime.now()
    today = today.strftime('%Y-%m-%d-%H-%M-%S')
    filename = f_name + '-' + today # test1-2022-05-19-14-43-23.jpg
    upload_path = 'static/' + filename + '.' + extension
    file.save(upload_path)


    answer = get_classification_result(upload_path)
    print(answer)
    return jsonify({'msg':'추론이 완료 되었습니다~', 'answer':answer})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
