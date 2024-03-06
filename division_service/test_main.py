from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_divide():
    response = client.post("/divide", json={"a": 20, "b": 5})
    assert response.status_code == 200
    assert response.json() == {"result": 4}

def test_divide_by_zero():
    response = client.post("/divide", json={"a": 20, "b": 0})
    assert response.status_code == 200
    assert response.json() == {"error": "Division by zero is not allowed"}
