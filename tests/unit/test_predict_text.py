import pytest
import app.app as app_module  # modulo app/app.py

class DummyModel:
    def predict(self, X):
        return ['positive' if 'good' in x.lower() else 'negative' for x in X]

def _patch_model(monkeypatch):
    monkeypatch.setattr(app_module, "loaded_model", DummyModel(), raising=False)

@pytest.mark.asyncio
async def test_predict_text_positive(monkeypatch):
    _patch_model(monkeypatch)
    req = app_module.TextRequest(text="This is really good")
    res = await app_module.predict(req)
    assert res["prediction"] == "POSITIVE"

@pytest.mark.asyncio
async def test_predict_text_negative(monkeypatch):
    _patch_model(monkeypatch)
    req = app_module.TextRequest(text="I hate this")
    res = await app_module.predict(req)
    assert res["prediction"] == "NEGATIVE"
