from flask import Flask, render_template, request, jsonify, redirect, url_for, abort
import hashlib
import datetime
import jwt

SECRET_KEY = 'example-jwt'
app = Flask(__name__)

# DB Setting
from pymongo import MongoClient
my_client = MongoClient('localhost', 27017)
my_db = my_client.sign_in_up # sign_in_up db 만들기

# Page ====
@app.route('/')
def home():
    # 편의를 위해 DB에 암호화된 ID, PWD 저장
    temp_id = 'abcde12345@naver.com'
    temp_pwd = 'abcde12345'
    temp_pwd = hashlib.sha256(temp_pwd.encode('utf-8')).hexdigest()
    my_db.users.insert_one({
        'id': temp_id,
        'pwd':temp_pwd
    })
    return redirect('/login')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/main')
def main():
    # PC에 저장 된 'mytoken' 쿠키 확인
    token = request.cookies.get('mytoken')
    try:
        if token is None:
            abort(401) # '페이지를 로드 할 수 없음'을 의미하는 HTTP 상태코드
        # 암호화 되어있는 token의 값 디코딩(암호화 풀기)
        pwd = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        user = my_db.users.find_one({"id": pwd['id']})  # 해당 Token을 가지고 있는 유저 검색
    except jwt.ExpiredSignatureError:  # token의 로그인 시간 만료시 login 페이지로 redirect
        return redirect(url_for("login"))
    except jwt.exceptions.DecodeError:  # 해당 token이 다르다면 login 페이지로 redirect
        return redirect("/login")
    return render_template('main.html', user=user)

# Error Handler
@app.errorhandler(401)
def page_not_found(error):
    return redirect("https://developer.mozilla.org/ko/docs/Web/HTTP/Status/401", code=401)

# API ====
@app.route('/api/login', methods=['POST'])
def api_login():
    id = request.form['id'] # abcd12345@naver.com
    pwd = request.form['pwd'] # abcd12345

    # 입력받은 패스워드 값 해싱하여 암호화
    hashed_pw = hashlib.sha256(pwd.encode('utf-8')).hexdigest()

    # Validation Check (by DB..)
    query = {
        'id':id, 
        'pwd':hashed_pw
    }
    try:
        user = my_db.users.find_one(query)
        if user is not None:
            # JWT(Json Wep Token)생성 (토큰 ID 값과, 유효기간(exp)를 담음)
            query = {
                'id': id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=1800)
            }
            # 토큰 생성 payload의 값 인코딩, 암호키 필수 유출금지!, 암호화형태 지정
            token = jwt.encode(query, SECRET_KEY, algorithm='HS256')
            doc = {'success':1, 'token': token, 'msg' : '로그인 성공'}
        else:
            doc = {'success':0, 'msg': '로그인 실패'}
    except: # DB Error
        doc = {'success':0, 'msg': '로그인 실패'}
    return jsonify(doc)

### ================ Main ================
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)  # 기본포트값 5000으로 설정
