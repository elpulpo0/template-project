# import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Projet 2 - API de prédiction des coûts médicaux"}


def test_predict():
    payload = {
        "age": 30,
        "bmi": 25.5,
        "children": 2,
        "sex": "male",
        "smoker": "yes",
        "region": "southeast"
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "predicted_charges" in response.json()