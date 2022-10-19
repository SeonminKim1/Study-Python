from fastapi import FastAPI, status
from pydantic import BaseModel, HttpUrl
from typing import Optional
import uvicorn

app = FastAPI()

'''
FastAPI에서 POST Method 작성시 Schema Dependency가 존재. (pydantic)
FastAPI는 BaseModel 상속 없이는 POST Method를 작성할 수 없음
중첩하여 Schema를 작성하는 것도 가능함 (POST 안에 값의 POST)

POST => { "name":"spike", "url":"http://www.naver.com" }

pydantic 타입
- pydantic은 자주 쓰이는 타입들을 미리 제공하여
- 이메일(EmailStr), 파일 경로, 우편 번호, URL(HttpUrl) 등 다양한 형태의 값을 쉽게 검증 가능
'''

class User(BaseModel):
    name:str
    url:Optional[HttpUrl] = None

@app.post("/users")
def create_user(user:User):
    return {
        'name': 'name:' + user.name,
        'url': 'url:' + user.url,
        'message':'success'
    }

# response_model => (pydantic으로 정의한) 반환 응답 객체 형식 
# response_model_include => response로 필수로 주어야 하는 것들
@app.post("/user/response", response_model = User, response_model_include={"name"})
def create_user2(user:User):
    return user

# STATUS CODE
@app.post("/user/status", response_model = User, status_code=status.HTTP_201_CREATED)
def create_user3(user:User):
    return user

if __name__ == "__main__":
    uvicorn.run("_03_POST:app", reload=True)
