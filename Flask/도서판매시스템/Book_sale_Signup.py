##############################################
# 이론
##############################################
## 부트스트랩 홈페이지
# https://getbootstrap.com/docs/4.5/getting-started/introduction/

# get 요청 : 페이지 띄우는 것
# post 요청 : 등록을 눌렀을 때 데이터를 가지고 오는것에 대한 요청
# get인지 post인지를 알기 위해 request라는 flask안에 메서드를 사용

##############################################
# 라이브러리
##############################################

# python 기본

import os
import pandas as pd
import numpy as np
import warnings; warnings.filterwarnings('ignore')

# Flask 라이브러리
from flask import request, redirect # get, post 등
from flask import Flask, render_template, session # html 띄워주기

# 유저 Model
from Book_sale.Book_sale_Model import Fcuser, db

# form 형태들 (Register form, Login form)
from Book_sale.Book_sale_Form import RegisterForm, LoginForm # form 불러오기, wtf로 작성된 것들임.

###########################################################################
# Code
###########################################################################

# Flask 객체를 app에 할당
app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    userid = session.get('userid',None)
    if userid:
        fcuser = Fcuser.query.filter_by(userid=userid).first()
    return render_template('Book_sale_home.html', userid=userid)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print('login success')
        session['userid'] = form.data.get('userid')
        return redirect('/')

    # 잘못되면 다시 login form으로
    print('wrong login')
    return render_template('Book_sale_login.html', form=form)

@app.route('/logout', methods=['GET'])
def logout():
    session.pop('userid', None)
    return redirect('/')

#### 회원 가입 Page
@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()

    # form.validate_on_submit
    # form 이 제대로 잘 전달됬고 유효성 검사까지 됬는지.
    # 이 기능은 POST 인지 검사를 안해도 됨. 값도 잘 들어왔는지 검사 안해도 ㄱㅊ
    if form.validate_on_submit():
        # user 객체 생성 및 form의 내용을 받아온다.
        fcuser = Fcuser()
        fcuser.userid = form.data.get('userid') # form 의 내용을 받아와서 Fcuser 객체 만듬.
        fcuser.password = form.data.get('password')
        fcuser.username = form.data.get('username')
        fcuser.userage = form.data.get('userage')
        fcuser.usergender = form.data.get('usergender')

        user_interset_list = []
        user_interset_list.extend(form.data.get('userinterest1'))
        user_interset_list.extend(form.data.get('userinterest2'))
        user_interset_list.extend(form.data.get('userinterest3'))

        print(user_interset_list)
        fcuser.userinterest = ','.join(user_interset_list)

        # db 작동되면 fcuser 넣고, commit()
        db.session.add(fcuser)
        db.session.commit()

        # 잘 완료되면 login 화면으로
        return redirect('/login')

    # 잘 안되면 Book_sale_register.html 로 다시
    return render_template('Book_sale_register.html', form=form)

#### IT 도서
@app.route('/it_book', methods=['GET','POST'])
def itbook():
    return render_template('Book_sale_List.html')
###########################################################################
# main
###########################################################################
# APP 에 대한 설정 무조건 되게 밖으로 뺌. (배포때)
basedir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(basedir, 'db.sqlite')

### SQLlite 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 변경에 대한 알림 안받기

### 암호화된 키 만들기
app.config['SECRET_KEY'] = 'jqiowejrojzxcovnklqnweiorjqwoijroi'

# 설정값들 초기화 하는 함수 - init_app
db.init_app(app)
db.app = app
db.create_all()  # 데이터베이스 생성

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
    #book_data = pd.read_csv('Book_data_it.csv', engine='python')
    #print(book_data.columns)