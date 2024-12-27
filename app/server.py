from fastapi import FastAPI
import joblib
import numpy as np

model = joblib.load("app/lte_download_throughput_predictor_model.joblib")

app = FastAPI()

@app.get('/api/v1')
def read_root():
    """
    Provide API information.

    Returns:
        dict: A dictionary containing the API info.
    """
    return {'message':'Network Metrics Predictor API'}

@app.get('/api/v1/download-throughput')
def read_download_throughput_root():
    """
    Provide API information for LTE Download Throughput Predictor.

    Returns:
        dict: A dictionary containing the API info.
    """
    return {'message':'LTE Download Throughput Predictor API'}

@app.get('/api/v1/technology')
def read_technology_root():
    """
    Provide API information for Technology Predictor.

    Returns:
        dict: A dictionary containing the API info.
    """
    return {'message':'Network Metrics Predictor API'}

@app.post('/api/v1/predict/download-throughput')
def predict_download_throughput(data: dict):
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
