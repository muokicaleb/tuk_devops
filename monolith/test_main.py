from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_add():
    response = client.post("/add", json={"a": 5, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 8}

def test_subtract():
    response = client.post("/subtract", json={"a": 10, "b": 4})
    assert response.status_code == 200
    assert response.json() == {"result": 6}

def test_multiply():
    response = client.post("/multiply", json={"a": 7, "b": 6})
    assert response.status_code == 200
    assert response.json() == {"result": 42}

def test_divide():
    response = client.post("/divide", json={"a": 20, "b": 5})
    assert response.status_code == 200
    assert response.json() == {"result": 4}

def test_divide_by_zero():
    response = client.post("/divide", json={"a": 20, "b": 0})
    assert response.status_code == 200
    assert response.json() == {"error": "Division by zero is not allowed"}
