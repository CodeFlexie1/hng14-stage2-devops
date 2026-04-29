import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch

# Import the app from your main.py file
from main import app

# TestClient allows us to make fake HTTP requests to our API without starting a server
client = TestClient(app)

# TEST 1: Check the root health endpoint
def test_home_status():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

# TEST 2: Check the submit endpoint and MOCK the Redis database
# The @patch decorator intercepts 'redis_client.lpush' before it fires
@patch("main.redis_client.lpush")
def test_submit_job(mock_lpush):
    response = client.post("/submit")
    assert response.status_code == 200
    
    data = response.json()
    assert data["status"] == "success"
    assert "job_id" in data
    
    # Assert that our API successfully "tried" to push to Redis with the correct data
    mock_lpush.assert_called_once_with("job_queue", data["job_id"])

# TEST 3: Check the status endpoint
def test_get_status():
    test_id = "1234-abcd"
    response = client.get(f"/status/{test_id}")
    assert response.status_code == 200
    assert response.json() == {"job_id": test_id, "status": "processing"}
