import json

from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_get_tasks():
    response = client.post("/get_tasks", json={"build": "forward_interest"})
    with open('test.txt') as f:
        test_result = json.load(f)
    assert response.status_code == 200
    assert response.json() == test_result
