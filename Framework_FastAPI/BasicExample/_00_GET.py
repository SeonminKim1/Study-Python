from fastapi import FastAPI
from typing import Optional
import uvicorn

app = FastAPI()

# 0. base
@app.get("/")
def hello():
    return "hello world"

# 1. 같은 url 충돌 시 Parameters URL을 위로
@app.get("/users/{user_id}")
def get_user(user_id:int):
    return {"user_id":user_id}

@app.get("/users/hi")
def get_hi():
    return {"hi"}

if __name__ == "__main__":
    uvicorn.run("_00_GET:app", reload=True)