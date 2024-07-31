from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Meme API"}

def test_create_meme():
    response = client.post("/memes/", json={"text": "Test Meme", "image_url": "http://example.com/image.jpg"})
    assert response.status_code == 200
    assert response.json()["text"] == "Test Meme"