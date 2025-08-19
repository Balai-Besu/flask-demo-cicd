import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello from Flask GitHub Actions Demo!" in response.data

def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert b"UP" in response.data
