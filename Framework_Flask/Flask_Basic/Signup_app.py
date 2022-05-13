from flask import request, redirect
'''
# get 요청 페이지 띄우는 것
# post 요청 : 등록을 눌렀을 때 데이터를 가지고 오는것에 대한 요청
# get인지 post인지를 알기 위해 request라는 flask안에 메서드를 사용
'''
from flask import Flask, render_template
from flask_ex.Signup_model import db # model.py의 db변수 가져오기
## 부트스트랩 홈페이지
# https://getbootstrap.com/docs/4.5/getting-started/introduction/

# Flask 의 클래스 객체 가져오기
'''
클래스를 받아오고, 객체 실행 - Fcuser
'''
from flask_ex.Signup_model import Fcuser

import os
import warnings
warnings.filterwarnings('ignore')

# Flask 객체를 app에 할당
app = Flask(__name__)

# 컨테이너 - 회원가입 생성
# 기본적으로 get만 허용하기 때문에 post를 활성화해줘야함
@app.route('/register', methods=['GET','POST'])
def register():
    # 만약 GET 이면 그냥 화면 띄워주고
    if request.method == 'GET':
        return render_template('register.html')
    else:
        # 회원 정보 생성
        userid = request.form.get('userid')
        username = request.form.get('username')
        password = request.form.get('password')
        re_password = request.form.get('re-password')

        ## 회원가입 기능에서의 몇가짗 ㅔ크
        if not (userid and username and password and re_password):
            return render_template('register.html')
        
        # 패스워드 같은지 안같은지 체크
        if password != re_password:
            return render_template('register.html')
        
        # 객체 만들기.
        fcuser = Fcuser()
        fcuser.userid = userid
        fcuser.username = username
        fcuser.password = password
        
        # db에 넣겠다. - 데이터베이스에 추가
        db.session.add(fcuser)
        db.session.commit() 

        # 해당 페이지로 전환
        return redirect('/')

# app 객체를 이용해 라우팅 경로를 설정
@app.route('/')
def hello():
    return render_template('hello.html')

if __name__ == "__main__":
    host_addr = "127.0.0.1"
    port_num = "8085"

    basedir = os.path.abspath(os.path.dirname('__file__'))
    dbfile = os.path.join(basedir, 'db.sqlite')

    ### SQLlite 설정
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False  # 변경에 대한 알림 안받기

    # 설정값들 초기화 하는 함수 - init_app
    db.init_app(app)
    db.app = app
    db.create_all() # 데이터베이스 생성

    app.run(host=host_addr, port=port_num)

