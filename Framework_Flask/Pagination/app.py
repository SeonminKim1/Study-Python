# Flask
from flask import Flask, request, render_template

# DB 연결 코드
from pymongo import MongoClient

client = MongoClient(
    'mongodb+srv://luckyseven:luckyseven@cluster0.2hyld.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client.od_project

app = Flask(__name__)

# page 당 출력 글 수
PAGE_UNIT = 4

@app.route('/', methods=['GET'])
def ranking():
    if request.method == 'GET':
        # DB 조회
        result_info = list(db.RESULT.find({"company" : "(주)럭키세븐"}, {'_id': False}))
        ranking_list = [{'name':result['name'], 'score': result['score'], 'date': result['date']} for result in result_info]
        ranking_list = sorted(ranking_list, key=lambda x: x['date']) # Date 별 정렬
        
        # page 관련
        page_num = request.args.get('page_num',default=1, type=int)
        # print('== 현재 페이지 번호는' , page_num)
        return render_template('/ranking.html', ranking_list=ranking_list, page_unit=PAGE_UNIT, page_num=page_num)

    else: # POST
        return render_template('/ranking.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)