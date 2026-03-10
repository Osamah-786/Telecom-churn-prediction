import pickle
import pandas as pd
from schemas.user_input import UserInput

with open("model/churn_model.pkl", "rb") as f:
    model = pickle.load(f)

def predict_output(data: UserInput):

    input_dict = data.model_dump()

    df = pd.DataFrame([input_dict])

    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    return {
        "churn_prediction": int(prediction),
        "churn_probability": float(probability)
    }