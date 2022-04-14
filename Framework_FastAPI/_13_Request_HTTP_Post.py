from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import JSONResponse
import requests
import json

app = FastAPI()

# uvicorn FastAPI_Request:app --reload
# FastAPI에서 POST Method 작성시 Schema Dependency가 존재. (pydantic)
# FastAPI는 BaseModel 상속 없이는 POST Method를 작성할 수 없음
class Item(BaseModel):
    user_id:str
    password:str

@app.post("/inference_post")
async def register_item(item : Item):
    dicted_item = dict(item)
    dicted_item['success'] = True
    return JSONResponse(dicted_item)

if __name__ == "__main__":

    data = {
        "user_id": "yubi5050",
        "password": "123123",
    }

    # request.post -> response_object
    # response_object attribues
    # https://www.w3schools.com/python/ref_requests_response.asp
    response_object = requests.post("http://127.0.0.1:8000/inference_post/",
                  data=json.dumps(data))

    print(response_object.content)
