from django.shortcuts import render
from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

# DB Setting
from pymongo import MongoClient
my_client = MongoClient('localhost', 27017)
my_db = my_client.sign_in_up # smkim db 만들기

# Page

@app.route('/')
def home():
    return redirect('/login')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/join')
def join():
    return render_template('join.html')

@app.route('/main')
def main():
    return render_template('main.html')

# API
@app.route('/api/login', methods=['POST'])
def api_login():
    id = request.form['id']
    pwd = request.form['pwd']
    query = {
        'id':id, 
        'pwd':pwd
    }
    
    # Validation Check (by DB..)
    try:
        data = my_db.users.find_one(query)
        print(data, type(data))
        if data is not None:
            doc = {'success':1, 'msg' : '로그인 성공'}
        else:
            doc = {'success':0, 'msg': '로그인 실패'}

    except: # DB Error
        doc = {'success':0, 'msg': '로그인 실패'}
    return jsonify(doc)
    
@app.route('/api/join', methods=['POST'])
def api_join():
    id = request.form['id']
    name = request.form['name']
    nickname = request.form['nickname']
    pwd = request.form['pwd']

    query = {
        'id' : id,
        'name' : name,
        'nickname' : nickname,
        'pwd' : pwd,
    }

    # DB 저장
    try:
        my_db.users.insert_one(query)
        doc = {'success':1, "msg" : 'DB 저장 성공'}
    except: # DB Error
        doc = {'success':0, "msg" : 'DB 저장 실패'}
    return jsonify(doc)

### ================ Main ================
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)  # 기본포트값 5000으로 설정
