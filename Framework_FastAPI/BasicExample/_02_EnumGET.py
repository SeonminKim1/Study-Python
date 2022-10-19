from enum import Enum

from fastapi import FastAPI

app = FastAPI()

class UserLevel(str, Enum):
    a = "a"
    b = "b"
    c = "c"

# 1. Enum 기반
# http://127.0.0.1:8000/users?grade=c (o)/
@app.get("/users")
def get_users(grade: UserLevel = UserLevel.a):  # 추가: UserLevel 기본값
    return {"grade": grade}