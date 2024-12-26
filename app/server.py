from fastapi import FastAPI
import joblib
import numpy as np

model = joblib.load("app/model.joblib")

app = FastAPI()

@app.get('/')
def read_root():
    """
    Provide API information.

    Returns:
        dict: A dictionary containing the API info.
    """
    return {'message':'LTE DL Throughput Predictor API'}

@app.post('/predict')
def predict(data: dict):
    """
    Predicts the class of a given set of features.

    Args:
        data (dict): A dictionary containing the features to predict.
        format: {"features": [PRB_UTILIZATION, RRC_CONNECTED_USERS, PAYLOAD]} 
        e.g. {"features": [0.95, 152.35, 1137.15]} 

    Returns:
        dict: A dictionary containing the predicted class.
    """
    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)[0]
    return {'predicted_value': prediction}
