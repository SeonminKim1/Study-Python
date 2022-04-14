from Book_sale.Book_sale_Model import Fcuser

# flask wtf 를 통해서 form에 대해서 좀 쉽게, 그리고 유효성검사도 쉽게 함
# form 관련 wtf 활용 (form 좀 잘꾸며주는)
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, RadioField, BooleanField, widgets, SelectMultipleField
from wtforms.validators import DataRequired, EqualTo

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class RegisterForm(FlaskForm):
    userid = StringField('userid', validators = [DataRequired()])
    username = StringField('username', validators = [DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    repassword = PasswordField('repassword', validators=[DataRequired()])
    userage = IntegerField('userage', validators=[DataRequired()])
    usergender = RadioField('gender', choices = [('man','남자'),('woman','여자')])

    list_of_files = ['IT도서', '인문학', '경영', '소설', '문학', '예술']

    # create a list of value/description tuples
    files = [(x, x) for x, x in zip(list_of_files, list_of_files)]
    userinterest1 = MultiCheckboxField('Label', choices=files[:2])
    userinterest2 = MultiCheckboxField('Label', choices=files[2:4])
    userinterest3 = MultiCheckboxField('Label', choices=files[4:])

# FlaskForm 은 wtf 꺼
class LoginForm(FlaskForm):
    # init와 ,__call__ 기본적으로 은 항상 들어가있음.
    class UserPassword(object):
        def __init__(self, message = None):
            self.message = message

        def __call__(selfs, form, field):
            # form 에서 입력한 값들 가져오기
            userid = form['userid'].data
            password = field.data

            # real database 에서 찾기- Database 에 ID가 있으면 OK
            fcuser = Fcuser.query.filter_by(userid=userid).first()

            if fcuser.password != password:
                raise ValueError('Wrong Password')

    userid = StringField('userid',validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(), UserPassword()])

