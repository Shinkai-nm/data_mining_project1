from flask import Blueprint, render_template, request, jsonify
import numpy as np
from app.model import PredictionModel
from .log import logger

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html', prediction=None)

@main.route('/predict', methods=['POST'])
def prediction():
    logger.info("Start prediction process")

    # Get the JSON data from the request
    data = request.get_json()  # Parses the incoming JSON request
    logger.info(f"Received data: {data}")

    # Map input names from the frontend to model's expected names
    model_inputs = {
        'age': int(data.get('age', 55)),               # Age: Integer
        'sex': int(data.get('sex', 0)),                # Sex: Integer (0 or 1)
        'cp': int(data.get('cp', 1)),                  # Chest Pain Type: Integer (1, 2, 3, 4)
        'trestbps': int(data.get('trestbps', 120)),    # Resting Blood Pressure: Integer
        'chol': int(data.get('chol', 250)),            # Cholesterol: Integer
        'fbs': int(data.get('fbs', 0)),                # Fasting Blood Sugar > 120: Integer (0 or 1)
        'restecg': int(data.get('restecg', 0)),        # Resting ECG Results: Integer (0, 1, 2)
        'thalach': int(data.get('thalach', 160)),      # Max Heart Rate Achieved: Integer
        'exang': int(data.get('exang', 0)),            # Exercise Induced Angina: Integer (0 or 1)
        'oldpeak': float(data.get('oldpeak', 0.0)),    # ST Depression: Float
        'slope': int(data.get('slope', 1)),            # Slope of Peak Exercise ST Segment: Integer (1, 2, 3)
        'ca': float(data.get('ca', 0.0)),              # Number of Major Vessels: Float (0, 1, 2, 3)
        'thal': float(data.get('thal', 3.0))           # Thal: Float (3.0, 6.0, 7.0)
    }

    logger.info(f"Prepared input for model: {model_inputs}")

    # Perform prediction (using a mock model for now)
    try:
        prediction_module = PredictionModel(logger)
        prediction = prediction_module.predict(list(model_inputs.values()))
    except Exception as e:
        logger.error(f"Error during prediction: {e}")
        return jsonify({'error': 'Error during prediction'}), 500

    # Return the result as a JSON response
    logger.info(prediction)
    
    return jsonify(prediction)
