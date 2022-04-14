from fastapi.testclient import TestClient
from ex7_monkeypatch import app
import ex7_monkeypatch as module_a
import pytest

client = TestClient(app)

# 4. post item write -> OK 로직 체크  => 400이 나오면 ok
def test_create_item(monkeypatch): 
    # obj, name, value
    
    def mock_getcwd(n):
        return n

    monkeypatch.setattr(module_a, 'get_age', mock_getcwd)
    response = client.post(
        "/items/",
        headers={"X-Token": "asdfasdf"},
        json={"id": "yubi5050", "title": "smkim", "description": "The smkim is god", "age":1},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": "yubi5050",
        "title": "smkim",
        "description": "The smkim is god",
        "age":1
    }