from fastapi.testclient import TestClient
from ex_5_fastapi_pytest_extended import app

client = TestClient(app)

# 1. get item -> ok 로직 체크
def test_read_item():
    response = client.get("/items/foo", headers={"X-Token": "asdfasdf"})
    assert response.status_code == 200 # 호출 결과가 200이 맞는지
    assert response.json() == { # 얻어온 데이터가 맞는지
        "id": "foo",
        "title": "Foo",
        "description": "There goes my hero",
    }

# 2. get item -> header token error 체크 => 400이 나오면 ok
def test_read_item_bad_token():
    response = client.get("/items/foo", headers={"X-Token": "hailhydra"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid X-Token header"}

# 3. get item -> item error 체크 => 404이 나오면 ok
def test_read_inexistent_item():
    response = client.get("/items/baz", headers={"X-Token": "asdfasdf"})
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}

# 4. post item write -> OK 로직 체크  => 400이 나오면 ok
def test_create_item(): 
    response = client.post(
        "/items/",
        headers={"X-Token": "asdfasdf"},
        json={"id": "yubi5050", "title": "smkim", "description": "The smkim is god"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": "yubi5050",
        "title": "smkim",
        "description": "The smkim is god"
    }

# 5. post item write -> token error
def test_create_item_bad_token():
    response = client.post(
        "/items/",
        headers={"X-Token": "hailhydra"},
        json={"id": "bazz", "title": "Bazz", "description": "Drop the bazz"},
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid X-Token header"}

# 6. post item write -> existing item
def test_create_existing_item():
    response = client.post(
        "/items/",
        headers={"X-Token": "asdfasdf"},
        json={
            "id": "foo",
            "title": "The Foo ID Stealers",
            "description": "There goes my stealer",
        },
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Item already exists"}