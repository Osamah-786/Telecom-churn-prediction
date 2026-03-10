from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schemas.user_input import UserInput
from model.predict import predict_output

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Telecom Customer Churn Prediction API"}


@app.get("/health")
def health_check():
    return {"status": "OK"}


@app.post("/predict")
def predict(data: UserInput):
    result = predict_output(data)
    return JSONResponse(content=result)