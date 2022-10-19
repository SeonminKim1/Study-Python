from fastapi import FastAPI, Query, Path, status
from pydantic import BaseModel, Field
from typing import List
import uvicorn

# Pydantic의 데이터 검증을 통해 방어 코드 작성을 대신해줌
# url로 오는 것들 경로 매개변수, 쿼리 매개변수들 다 인자에서 손대기

## Path, Query 역할
# 매개변수를 명시적 정의 및 다양한 옵션을 추가 가능
# gt, ge, lt, le: 숫자
# min_length, max_length: str
# min_items, max_items: 컬렉션(e.g. List, Set)
# regex 도 사용 가능
# ... 기호 <-> None : 반대
app = FastAPI()

inventory = [
    {
        "id": 1,
        'user_id':2,
        "name": "무기",
        "price": 250.0,
    },
    {
        "id": 2,
        'user_id':3,
        "name": "방어구",
        "price": 500.0,
    },]

# v1 - 함수에서 작성 : user의 inventory 조회
# http://127.0.0.1:8000/users/2/inventory?name=무기
class Item(BaseModel):
    id: int 
    user_id: int
    name: str
    price: float

@app.get("/users/{user_id}/inventory", response_model=Item, response_model_exclude={'id', 'user_id'})
def get_item(
    user_id: int = Path(..., gt=0, title="사용자 id"), # ...은 필수라는 뜻
    name: str = Query(None, min_length=1, max_length=10, title="아이템 이름"),
    ):
    result = ''
    for item in inventory:
        if (user_id == item['user_id']) and (name == item['name']):
            result = item
            break
    result = [item for item in inventory if (user_id == item['user_id']) and (name == item['name'])]
    return result[0]

# v2
class Item2(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, title="이름")
    price: float = Field(None, ge=0)
    amount: int = Field(default=1, gt=0, le=300, title="수량",)

# http://127.0.0.1:8000/users/2/item body={ "name":"무기", "price":100.5, "amount":200}
@app.post("/users/{user_id}/item")
def create_item(item: Item2):
    inventory.append(item)
    return inventory
    
if __name__ == "__main__":
    uvicorn.run("_04_Validation:app", reload=True)
