from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_get_item_not_found():
    response = client.get("/items/99")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}    

def test_root():
    response = client.get("/")
    assert response.status_code == ...
    assert response.json() == ...


def test_get_item():
    response = client.get("/items/1")
    assert response.status_code == ...
    assert response.json() == ...    