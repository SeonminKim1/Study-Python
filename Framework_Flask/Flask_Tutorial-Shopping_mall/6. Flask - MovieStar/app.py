from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.smkim
movie_collections = db.movies_star

### 기능 3가지
## GET - 영화인 정보를 카드로 보여주기(Read)
# 1. 조회(Read) 기능: 영화인 정보 전체를 조회

## POST
# 2. 좋아요(Update) 기능: 클라이언트에서 받은 이름(name_give)으로 찾아서 좋아요(like)를 증가
# 3. 삭제(Delete) 기능: 클라이언트에서 받은 이름(name_give)으로 영화인을 찾고, 해당 영화인을 삭제

@app.route('/')
def home():
    return render_template('index.html')

## GET - 1. 조회(Read) 기능
# - 요청 URL= /api/list, 방식 = GET
# - 기능 : 데이터베이스에  영화인 정보를 조회(Read) / 영화인 정보 리턴
# - Return 값  : (JSON) 'stars_list'= 영화인 정보 리스트
@app.route('/api/list', methods=['GET'])
def show_stars():
    data = movie_collections.find({}, {'_id': False})
    movie_star = list(data.sort('like', -1)) # cursor class의 sort('key or list' , directions:-1은 내림차순)
    return jsonify({'movie_stars': movie_star})

## POST - 2. 좋아요(Update) 기능
# - 요청 URL= /api/like , 방식 = POST
# - 요청 데이터 : 영화인 이름(name_give)
# - 기능
#   - 영화인 이름(요청 데이터)과 일치하는 영화인 정보의 좋아요 수를 한 개 증가시켜 데이터베이스에 업데이트(Update)
#   - 성공 응답 메세지 Return
# - Return 값  : (JSON) 'msg'='좋아요 완료!'

@app.route('/api/like', methods=['POST'])
def like_star():
    name_receive = request.form['name_give']
    target_star = movie_collections.find_one({'name': name_receive})
    current_like = target_star['like']
    new_like = current_like + 1 # 좋아요 +1
    movie_collections.update_one({'name': name_receive}, {'$set': {'like': new_like}})
    return jsonify({'msg': '좋아요 완료!'})


## POST - 3. 삭제(Delete) 기능
# - 요청 URL= /api/delete , 방식 = POST
# - 요청 데이터 : 영화인 이름(name_give)
# - 기능
#   - 영화인 이름(요청 데이터)와 일치하는 영화인 정보를 데이터베이스에서 삭제(Delete)
#   - 성공 응답 메세지 Return
# - Return 값 : (JSON) 'msg'='삭제 완료!'
# API 역할을 하는 부분
@app.route('/api/delete', methods=['POST'])
def delete_star():
    name_receive = request.form['name_give']
    movie_collections.delete_one({'name': name_receive})
    return jsonify({'msg': '삭제 완료!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)