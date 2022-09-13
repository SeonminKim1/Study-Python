from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.smkim
articles_collections = db.articles


@app.route('/')
def home():
   return render_template('index.html')


## 전체 기능 2가지
# 1) 포스팅API - 카드 생성 (Create) : 클라이언트에서 받은 url, comment를 이용해 페이지 정보를 찾고 저장 
# 2) 리스팅API - 저장된 카드 보여주기 (Read)
# 동작 원리 : DB에 있는 링크(url) 통해 Meta 정보만 추출

## POST
# 1) 포스팅API - 카드 생성 (Create) : 클라이언트에서 받은 url, comment를 이용해 페이지 정보를 찾고 저장 
@app.route('/memo', methods=['POST'])
def saving():
    # 1. form에서 제출한 정보 저장 (url, comment)
    url_receive = request.form['url_give']
    comment_receive = request.form['comment_give']

    # 2. Crawling - <head>의 <meta> property 속성 - title, image, description 받아옴.
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers) # 저장 된 URL 에서 크롤링
    soup = BeautifulSoup(data.content.decode('utf-8', 'replace'), 'html.parser')
    title = soup.select_one('meta[property="og:title"]')['content']
    image = soup.select_one('meta[property="og:image"]')['content']
    desc = soup.select_one('meta[property="og:description"]')['content']

    doc = {
        'title':title,
        'image':image,
        'desc':desc,
        'url':url_receive,
        'comment':comment_receive
    }

    articles_collections.insert_one(doc)
    return jsonify({'msg':'저장이 완료되었습니다!'})

## GET
# 2) 리스팅API - 저장된 카드 보여주기 (Read)
@app.route('/memo', methods=['GET'])
def listing():
    articles = list(articles_collections.find({}, {'_id': False}))
    return jsonify({'all_articles':articles})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)