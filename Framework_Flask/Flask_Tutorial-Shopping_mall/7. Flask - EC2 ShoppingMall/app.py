from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

# client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://test:test@localhost', 27017)

db = client.smkim
orders_collection = db.shoppingmall

@app.route('/')
def homework():
    return render_template('index.html')


## 쇼핑몰 주요 기능 2가지
# 1) 주문하기(POST): 정보 입력 후 '주문하기' 버튼클릭 시 주문목록 추가
# 2) 주문내역보기(GET): 페이지 로딩 후 하단 주문 목록보이기

## POST
# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']

    doc = {
        'name': name_receive,
        'count': count_receive,
        'address': address_receive,
        'phone': phone_receive
    }
    orders_collection.insert_one(doc)

    return jsonify({'result': 'success', 'msg': '주문 완료!'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    orders = list(orders_collection.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)