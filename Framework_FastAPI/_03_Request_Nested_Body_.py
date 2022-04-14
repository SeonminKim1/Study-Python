from typing import Optional, Set

from fastapi import FastAPI
from pydantic import BaseModel
import requests
import json
app = FastAPI()

class Image(BaseModel):
    url: str
    name: str

class Item(BaseModel):
    name: str
    tax: Optional[float] = None
    tags: Set[str] = []
    image: Optional[Image] = None

# post도 body, parameter 같이 줄 수 있음.
@app.post("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

if __name__ == "__main__":
    data = {
        "name": "Foo",
        "tax": 3.2,
        "tags": ["rock", "metal", "bar"],
        "image": {
            "url": "http://example.com/baz.jpg",
            "name": "The Foo live"
        }
    }
    response_object = requests.post(
        "http://127.0.0.1:8000/items/3",
        data=json.dumps(data)
    )
    print(response_object.content)
