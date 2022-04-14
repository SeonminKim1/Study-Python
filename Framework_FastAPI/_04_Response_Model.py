from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
import requests
import json

app = FastAPI()

class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Optional[str] = None

class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None

# 응답할 모델의 형태는 UserOut
# 자동으로 들어온 Pydantic에서 찾음
# response_model_include => response로 필수로 주어야 하는 것들
# case1. Base, all return
# @app.post("/user/", response_model=UserOut)
# case2. Base + include
# @app.post("/user/", response_model=UserOut, response_model_include = {"username",'email','full_name'})
# case3. Base - exclude
@app.post("/user/", response_model=UserOut, response_model_exclude = {"username"})
async def create_user(user: UserIn):
    print('username:', user.username)
    print('password:', user.email)
    print('full_name:', user.full_name)
    print('email:', user.email)
    return user


if __name__ == "__main__":
    data = {
        "username": "yubi5050",
        "password": "tjsals1",
        "email":"yubi5050@naver.com",
        "full_name": "KSM",
    }

    response_object = requests.post(
        "http://127.0.0.1:8000/user/",
        data=json.dumps(data)
    )
    print(response_object.content)
