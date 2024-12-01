from flask import Blueprint, render_template, request, jsonify
import numpy as np
from app.model import predict  # Mocked for now
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

    # Check if the data contains all necessary fields (13 inputs)
    required_fields = [f"input{i}" for i in range(1, 14)]
    if not all(field in data for field in required_fields):
        logger.error("Missing required fields in input data")
        return jsonify({'error': 'Missing required fields in the input data'}), 400
    
    # Prepare the input data for prediction (converting to float)
    inputs = []
    for i in range(1, 14):
        try:
            inputs.append(float(data[f'input{i}']))
        except ValueError:
            logger.error(f"Invalid value for input{i}: {data[f'input{i}']}")
            inputs.append(0.0)  # Default to 0 if the value is invalid

    logger.info(f"Prepared input for model: {inputs}")

    # Perform prediction (using a mock model for now)
    # You can replace this with your real model once available
    try:
        result = predict(np.array(inputs).reshape(1, -1))  # Replace `predict` with your actual model function
    except Exception as e:
        logger.error(f"Error during prediction: {e}")
        return jsonify({'error': 'Error during prediction'}), 500

    # Return the result as a JSON response
    logger.info(f"Prediction result: {result}")
    
    return jsonify({'prediction': result[0]})

