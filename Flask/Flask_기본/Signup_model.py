from flask_sqlalchemy import SQLAlchemy

import warnings
warnings.filterwarnings('ignore')

# db에 대한 최상위 변수
db = SQLAlchemy()

class Fcuser(db.Model):
    __tablename__ = 'fcuser'
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(64))
    userid = db.Column(db.String(32))
    username = db.Column(db.String(8))

