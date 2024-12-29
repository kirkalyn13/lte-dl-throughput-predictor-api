from fastapi import FastAPI
import joblib
import numpy as np

dltput_model = joblib.load("app/lte_download_throughput_predictor_model.joblib")
prb_expansion_model = joblib.load("app/prb_expansion_classifier_model.joblib")

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

@app.get('/api/v1/prb-expansion')
def read_prb_expansion_root():
    """
    Provide API information for PRB Expansion Classifier.

    Returns:
        dict: A dictionary containing the API info.
    """
    return {'message':'PRB Expansion Classifier API'}

@app.post('/api/v1/download-throughput/predict')
def predict_download_throughput(data: dict):
    """
    Predicts the download throughput from a given set of features.

    Args:
        data (dict): A dictionary containing the features to predict.
        format: {"features": [PRB_UTILIZATION, RRC_CONNECTED_USERS, PAYLOAD]} 
        e.g. {"features": [0.95, 152.35, 1137.15]} 

    Returns:
        dict: A dictionary containing the predicted value.
    """
    features = np.array(data['features']).reshape(1, -1)
    prediction = dltput_model.predict(features)[0]
    return {'predicted_value': prediction}

@app.post('/api/v1/prb-expansion/predict')
def predict_prb_expansion(data: dict):
    """
    Classifies for expansion sites from a given set of features.

    Args:
        data (dict): A dictionary containing the features to predict.
        format: {"features": ['PRB_UTILIZATION', 'RRC_USER', 'PAYLOAD']} 
        e.g. {"features": [0.8123, 46.4515, 6764.075]} 

    Returns:
        dict: A dictionary containing the predicted value.
    """

    features = np.array(data['features']).reshape(1, -1)
    prediction = prb_expansion_model.predict(features)[0]
    for_expansion = ["NO", "YES"]

    return {'for_expansion': for_expansion[prediction]}
