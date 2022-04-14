from typing import Optional
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

fake_secret_token = "asdfasdf"
fake_db = {
    "foo": {"id": "foo", "title": "Foo", "description": "There goes my hero"},
    "bar": {"id": "bar", "title": "Bar", "description": "The bartenders"},
}

app = FastAPI()

class Item(BaseModel):
    id: str
    title: str
    description: Optional[str] = None
    age: int

def get_age(n):
    return n

# update db item
@app.post("/items/", response_model=Item)
async def create_item(item: Item, x_token: str = Header(...)):
    if x_token != fake_secret_token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    if item.id in fake_db:
        raise HTTPException(status_code=400, detail="Item already exists")
    print(type(item), item, item.age, type(item.age))
    m = get_age(n=1)
    item.age = m
    fake_db[item.id] = item
    return item