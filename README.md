# ML Predictor — Setup Guide

## Project Structure

```
.
├── index.html        # Frontend (open in browser)
├── main.py           # FastAPI backend
├── predict.py        # Your prediction logic  ← EDIT THIS
└── requirements.txt  # Python dependencies
```

---

## 1. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 2. Add your model logic to `predict.py`

Open `predict.py` and replace the placeholder inside the `predict()` function with your real model code, for example:

```python
import joblib

model = joblib.load("model.pkl")

def predict(features: list[float]) -> dict:
    prediction = model.predict([features])[0]
    probability = model.predict_proba([features])[0].max()
    return {
        "result": int(prediction),
        "confidence": float(probability),
    }
```

The function must:
- Accept `features: list[float]` with exactly 10 values
- Return a `dict` — all keys/values are shown in the UI automatically

---

## 3. Start the FastAPI server

```bash
uvicorn main:app --reload
```

Server runs at: http://127.0.0.1:8000

Interactive API docs: http://127.0.0.1:8000/docs

---

## 4. Open the frontend

Simply open `index.html` in your browser (double-click or `open index.html`).

The page sends a `POST /predict` request to `http://127.0.0.1:8000/predict`.
You can change the API URL in the input field at the top of the page.

---

## API Reference

**POST** `/predict`

Request body:
```json
{ "features": [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0] }
```

Response:
```json
{
  "success": true,
  "prediction": { "result": "Positive", "confidence": 0.55 },
  "features_received": [1.0, 2.0, ...]
}
```
