################## FastAPI & Pymongo
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str

import pymongo
def mongo(): # connection_params
    db = pymongo.MongoClient().db # Makes the connection using another function
    return db

app = FastAPI()
@app.post("/register")
async def create_item(item : Item): 
    db = mongo()
    result = db.collection.find_one({"name":item.name}, {'_id': 0}) # ObjectId: 없애기
    return result

#################### TEST Code 작성
from httpx import AsyncClient
import pytest
import mongomock
documents = {'name':'smkim', 'password':3}

@pytest.fixture
async def async_app_client():
    async with AsyncClient(app=app, base_url='http://') as client:
        yield client

@pytest.mark.asyncio
async def test_patch_mongo(monkeypatch, async_app_client):
    # mongomock db 생성
    db = mongomock.MongoClient().db
    db.collection.insert_one(documents)
    def fake_mongo():
        return db

    # monkeypatch - db
    monkeypatch.setattr('ex_10_mongomock.mongo', fake_mongo)
    # post to FastAPI
    response = await async_app_client.post(
        "/register", json={"name": "smkim"},
    )
    assert response.status_code == 200
    assert response.json() == {
            "name": "smkim",
            "password": 3
    }
