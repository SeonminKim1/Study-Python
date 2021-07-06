from fastapi import FastAPI, Request
import requests

app = FastAPI()

@app.get("/items/{item_id}")
def read_root(item_id: str, request: Request):
    client_host = request.client.host
    return {"client_host": client_host, "item_id": item_id}

if __name__ == "__main__":
    response_object = requests.get("http://127.0.0.1:8000/items/foo",)
    print(response_object.content)