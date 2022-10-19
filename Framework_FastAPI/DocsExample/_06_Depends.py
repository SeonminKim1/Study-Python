from typing import Optional
from fastapi import Depends, FastAPI
import requests
import json

app = FastAPI()

async def common_parameters(q: Optional[str] = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}

@app.get("/items/")
async def read_items(commons: dict = Depends(common_parameters)):
    return commons

@app.get("/users/")
async def read_users(commons: dict = Depends(common_parameters)):
    return commons

if __name__ == "__main__":
    response_object = requests.get("http://127.0.0.1:8000/items/foo2",)
    print(response_object.content)
    response_object2 = requests.get("http://127.0.0.1:8000/items/foo",)
    print(response_object2.content)