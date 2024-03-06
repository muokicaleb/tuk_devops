from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_subtract():
    response = client.post("/subtract", json={"a": 10, "b": 4})
    assert response.status_code == 200
    assert response.json() == {"result": 6}
