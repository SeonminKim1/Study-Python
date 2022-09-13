from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.smkim
book_review_collections = db.bookreview

@app.route('/')
def home():
   return render_template('index.html')

# 요청 URL= /review , 요청 방식 = POST 
@app.route('/review', methods=['POST'])
def write_review():
   title_receive = request.form['title_give'] # 클라이언트가 준 title
   author_receive = request.form['author_give'] # 클라이언트가 준 author 
   review_receive = request.form['review_give'] # 클라이언트가 준 review

   # DB에 삽입할 review 만들기
   doc = {
      'title': title_receive,
      'author': author_receive,
      'review': review_receive
   }
   # reviews에 review 저장하기
   book_review_collections.insert_one(doc)
   return jsonify({'msg': '리뷰가 성공적으로 작성되었습니다.'})

# 요청 URL= /review , 요청 방식 = GET
@app.route('/review', methods=['GET'])
def read_reviews():
   receive1 = request.args.get('title_give')
   receive2 = request.args.get('author_give')
   receive3 = request.args.get('review_give')
   print(receive1, receive2, receive3)

   return jsonify({'msg': '이 요청은 GET!'})


if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)