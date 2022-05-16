from flask import Blueprint

router2 = Blueprint("greet", __name__, url_prefix='/greet')

@router2.route("/hi")
def hi():
    return "HI ! "

@router2.route("/hello")
def hello():
    return "Hello"