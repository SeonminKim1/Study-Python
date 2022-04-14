from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import requests
import json

# FastAPI에서 POST Method 작성시 Schema Dependency가 존재. (pydantic)
# FastAPI는 BaseModel 상속 없이는 POST Method를 작성할 수 없음

class Item(BaseModel):
    name: str
    price: Optional[float] = None

app = FastAPI()

@app.post("/items")
async def create_item(item : Item):
    print(item)
    item = item.dict()
    item.update({'ok':True})
    return item

if __name__ == "__main__":
    data = {
        "name": "smkim",
        "price": 10.2
    }

    response_object = requests.post(
        "http://127.0.0.1:8000/items/",
        data=json.dumps(data)
    )

    print(response_object.content)