from fastapi import FastAPI, HTTPException
import requests
import json

app = FastAPI()
items = {"foo": "The Foo Wrestlers"}

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": items[item_id]}


if __name__ == "__main__":
    response_object = requests.get("http://127.0.0.1:8000/items/foo2",)
    print(response_object.content)
    response_object2 = requests.get("http://127.0.0.1:8000/items/foo",)
    print(response_object2.content)