from fastapi.testclient import TestClient
from url_shortener.app.main import app

client = TestClient(app)

def test_shorten_url():
    response = client.post("/shorten", json={"long_url": "https://example.com"})
    assert response.status_code == 200
    data = response.json()
    assert "code" in data
    assert data["long_url"] == "https://example.com"

def test_redirect_url():
    response = client.post("/shorten", json={"long_url": "https://example.com"})
    code = response.json()["code"]
    response = client.get(f"/{code}")
    assert response.status_code == 200
    assert "redirect_to" in response.json()

def test_analytics():
    response = client.post("/shorten", json={"long_url": "https://example.com"})
    code = response.json()["code"]
    response = client.get(f"/analytics/{code}")
    assert response.status_code == 200
    data = response.json()
    assert data["clicks"] >= 0
    assert "created_at" in data