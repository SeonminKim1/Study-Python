from flask import Blueprint

router1 = Blueprint("money", __name__, url_prefix='/money')

@router1.route("/earn")
def earn():
    return "earn money"

@router1.route("/lose")
def lose():
    return "lose money"