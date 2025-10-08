from pathlib import Path
from fastapi.responses import JSONResponse
from fastapi import FastAPI
from pydantic import BaseModel
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Counter
import uvicorn
import pickle

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "sentiment_analysis_model.pkl"

with open(MODEL_PATH, "rb") as f:
    loaded_model = pickle.load(f)

class TextRequest(BaseModel):
    text: str

PREDICTION_ERRORS = Counter("prediction_errors_total", "Totale di errori durante la predizione")

app = FastAPI()

Instrumentator().instrument(app).expose(app)


def predict_text(text: str) -> str:
    """Utile per i test"""
    return loaded_model.predict([text])[0]

@app.get("/")
def read_root():
    return {"message": "Benvenuto nella Sentiment Analysis API"}


@app.post('/predict')
async def predict(data: TextRequest):
    """
    Endpoint per identificare la lingua del testo fornito
    - Input: JSON con campo "text"
    - Output: JSON con "sentiment"
    """

    if not data.text or not data.text.strip():
        return JSONResponse(status_code=400, content={'message': 'Il testo non può essere vuoto'})

    try:
        prediction = loaded_model.predict([data.text])
        sentiment = prediction[0]

        response = {
            'prediction': sentiment.upper(),
        }

        return response

    except Exception as e:
        PREDICTION_ERRORS.inc()
        return JSONResponse(status_code=500, content={'message': "Impossibile indentificare il sentimento del testo"})