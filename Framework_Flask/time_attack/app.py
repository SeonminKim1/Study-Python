from flask import Flask, request, jsonify, render_template, redirect, url_for
app = Flask(__name__)  
import hashlib
import jwt
import datetime

# DB Setting
from pymongo import MongoClient
my_client = MongoClient('localhost', 27017)
my_db = my_client.smkim # smkim db 만들기

SECRET_KEY = '$seonmin'

# [회원가입 API]
# id, pw, nickname을 받아서, mongoDB에 저장합니다.
# 저장하기 전에, pw를 sha256 방법(=단방향 암호화. 풀어볼 수 없음)으로 암호화해서 저장합니다.
@app.route('/api/join', methods=['POST'])
def api_register():
    id_receive = request.form['email_give']
    pw_receive = request.form['pwd_give']
    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()
    my_db.user.insert_one({'id': id_receive, 'pw': pw_hash})
    return jsonify({'result': 'success'}) 


    # [로그인 API]
# id, pw를 받아서 맞춰보고, 토큰을 만들어 발급합니다.
@app.route('/api/login', methods=['POST'])
def api_login():
    id_receive = request.form['email_give']
    pw_receive = request.form['pwd_give']

    # 회원가입 때와 같은 방법으로 pw를 암호화합니다.
    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    # id, 암호화된pw을 가지고 해당 유저를 찾습니다.
    result = my_db.user.find_one({'id': id_receive, 'pw': pw_hash})

    # 찾으면 JWT 토큰을 만들어 발급합니다.
    if result is not None:
        # JWT 토큰에는, payload와 시크릿키가 필요합니다.
        # 시크릿키가 있어야 토큰을 디코딩(=풀기) 해서 payload 값을 볼 수 있습니다.
        # 아래에선 id와 exp를 담았습니다. 즉, JWT 토큰을 풀면 유저ID 값을 알 수 있습니다.
        # exp에는 만료시간을 넣어줍니다. 만료시간이 지나면, 시크릿키로 토큰을 풀 때 만료되었다고 에러가 납니다.
        payload = {
            'id': id_receive,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=1800)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        # token을 줍니다.
        return jsonify({'result': 'success', 'token': token})
    # 찾지 못하면
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})

@app.route('/')
def home():
   return render_template('index.html')

# 게시판
@app.route('/index')
def index():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = my_db.user.find_one({"id": payload['id']})
        return render_template('board.html', id=user_info['id'])
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))

@app.route('/logout')
def logout():
    token_receive = request.cookies.get('mytoken')
    if token_receive is not None:
        return jsonify({'msg':'로그아웃 완료!'})


@app.errorhandler(401)
def page_not_found(error):
    return redirect("https://developer.mozilla.org/ko/docs/Web/HTTP/Status/401", code=401)

if __name__ == '__main__':
    app.debug = True
    app.run()