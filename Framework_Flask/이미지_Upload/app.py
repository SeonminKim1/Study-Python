from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime
from pymongo import MongoClient
from werkzeug.utils import secure_filename

app = Flask(__name__)

# DB Setting
from pymongo import MongoClient
my_client = MongoClient('localhost', 27017)
my_db = my_client.smkim # sign_in_up db 만들기
my_collection = my_db.image_upload

# Page
@app.route('/')
def home():
    return render_template('index.html')

# 파일 업로드 방식 
# 1. File 창 열어서 진행 Ver
# 2. 모달 창 Ver
@app.route('/fileupload', methods=['POST'])
def file_upload():
    f_name = request.form['f_name']
    file = request.files['file'] # werkzeug.datastructures.FileStorage
    extension = secure_filename(file.filename).split('.')[-1]
    f_name = f_name.replace('.' + extension, '')

    # 파일 이름 , Local 이미지 저장 
    today = datetime.now()
    filename = f_name + '-' + today.strftime('%Y-%m-%d-%H-%M-%S')
    save_path = 'static/' + filename + '.' + extension
    file.save(save_path)

    # DB에 Image Path 저장
    doc = {'f_name':f_name, 'img_path': filename + '.' + extension}
    my_collection.insert_one(doc)
    return jsonify({'result':'success'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)