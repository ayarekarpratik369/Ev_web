from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from predict import predict_fault   
from predict import predict_fault, top10_features



app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return open("index.html").read()


@app.post("/predict", response_class=HTMLResponse)
def predict(
    f1: float = Form(...),
    f2: float = Form(...),
    f3: float = Form(...),
    f4: float = Form(...),
    f5: float = Form(...),
    f6: float = Form(...),
    f7: float = Form(...),
    f8: float = Form(...),
    f9: float = Form(...),
    f10: float = Form(...)
):
    values = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10]
    data = dict(zip(top10_features, values))

    result = predict_fault(data)

    return f"""
    <h2>Prediction: {result['fault']}</h2>
    <p>Label: {result['label']}</p>
    <a href="/">Go Back</a>
    """