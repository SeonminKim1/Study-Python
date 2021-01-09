from flask_sqlalchemy import SQLAlchemy

# db에 대한 최상위 변수
db = SQLAlchemy()

class Fcuser(db.Model):
    __tablename__ = 'fcuser'

    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String(32))
    password = db.Column(db.String(128))
    username = db.Column(db.String(8))
    userage = db.Column(db.Integer)
    usergender = db.Column(db.String(4))
    userinterest = db.Column(db.String(100))