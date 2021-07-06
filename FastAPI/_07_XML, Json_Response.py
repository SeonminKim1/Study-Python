'''
# Response 반환 방법 종류
- a dict
- a list
- Pydantic 모델
- 데이터베이스 모델
- FastAPI 는 JSON Compatible Encoder로 해당 값을 자동 JSON으로 변환함
'''

from datetime import datetime
from typing import Optional
import json
from fastapi import FastAPI, Response
# jsonable_encoder실제로 FastAPI에서 내부적으로 데이터를 변환 하는 데 사용
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import requests

class Item(BaseModel):
    title: str
    timestamp: datetime
    description: Optional[str] = None

app = FastAPI()

@app.get("/items/")
def update_item(item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    return JSONResponse(content=json_compatible_item_data)

@app.get("/legacy/")
def get_legacy_data():
    data = """<?xml version="1.0"?>
    <shampoo><Body>
        You'll have to use soap here.
    </Body></shampoo>
    """
    return Response(content=data, media_type="application/xml")

# jsonresponse , xml response 방법
if __name__ == "__main__":
    data = {
        "title":'string',
        'timestamp' : datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'description':'description임'
    }

    response_object = requests.get("http://127.0.0.1:8000/items/", data=json.dumps(data)) # json 안 씌우면 오류남.
    print(type(response_object.content), response_object.content) # bytes 형식

    response_object2 = requests.get("http://127.0.0.1:8000/legacy/",)
    print(type(response_object2.content), response_object2.content) # bytes 형식
