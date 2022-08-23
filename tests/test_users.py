from fastapi.testclient import TestClient
import json
from app.main import app

client = TestClient(app)


def test_post_user():
    payload = json.dumps({"name": "Lawry", "location": "Poole", "password": "Pa55w0rd", "user_id": 5, "ageRef": 6, "bio": "This is all about me."})
    response = client.post(
        "/users/",
        json=payload,
    )
    assert response.status_code == 200