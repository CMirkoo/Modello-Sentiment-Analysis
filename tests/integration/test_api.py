import pytest
from fastapi.testclient import TestClient
import app.app as app_module

class DummyModel:
    def predict(self, X):
        return ['positive' if 'good' in x.lower() else 'negative' for x in X]

@pytest.fixture
def client(monkeypatch):
    monkeypatch.setattr(app_module, "loaded_model", DummyModel(), raising=False)
    return TestClient(app_module.app)

@pytest.mark.integration
def test_predict_endpoint_positive(client):
    r = client.post("/predict", json={"text": "This is good"})
    assert r.status_code == 200
    assert r.json()["prediction"] == "POSITIVE"

@pytest.mark.integration
def test_predict_endpoint_negative(client):
    r = client.post("/predict", json={"text": "This is bad"})
    assert r.status_code == 200
    assert r.json()["prediction"] == "NEGATIVE"

@pytest.mark.integration
def test_predict_endpoint_empty_text(client):
    r = client.post("/predict", json={"text": "   "})
    assert r.status_code == 400
    assert r.json()["message"] == "Il testo non può essere vuoto"
