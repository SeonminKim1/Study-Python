
## FastAPI 
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    email: str
    password : Optional[str] = None

app = FastAPI()
@app.post("/register")
async def create_item(item : Item):
    item = item.dict()
    item.update({'is_ok':True})
    return item


# TEST Code 작성
from httpx import AsyncClient
import pytest

@pytest.fixture
async def async_app_client():
    async with AsyncClient(app=app, base_url='http://') as client:
        yield client

@pytest.mark.asyncio
async def test_create_user(async_app_client):
    response = await async_app_client.post(
        "/register",
        json={
            "name": "Test User",
            "email": "test@test.com",
            "password": "password",
        },
    )
    assert response.status_code == 200
    assert response.json() == {
            "name": "Test User",
            "email": "test@test.com",
            "password": "password",
            'is_ok': True
        }
