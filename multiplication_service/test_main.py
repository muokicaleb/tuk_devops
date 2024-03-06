from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_multiply():
    response = client.post("/multiply", json={"a": 7, "b": 6})
    assert response.status_code == 200
    assert response.json() == {"result": 42}

