from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_add_numbers():
    response = client.post("/add", json={"a": 5, "b": 7})
    assert response.status_code == 200
    assert response.json() == {"result": 12}
