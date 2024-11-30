from flask import Blueprint, render_template, request
import numpy as np
from app.model import predict

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html', prediction=None)

@main.route('/predict', methods=['POST'])
def prediction():
    # Collect input data from the form
    inputs = []
    for i in range(1, 14):
        try:
            inputs.append(float(request.form[f'input{i}']))
        except ValueError:
            inputs.append(0)  # Default value if input is invalid
    
    print(inputs)
    
    # Perform prediction
    result = predict(np.array(inputs).reshape(1, -1))
    
    # Render the result back to the form
    return render_template('index.html', prediction=result)
