import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

class PredictionModel():

    def __init__(self, logger):
        self.logger = logger 

    def load_model_and_scaler(self):
        try:
            # Load pre-trained KNN model and scaler from pickle files
            model = joblib.load('Model Experiment /Raw Data/knn_model.pkl')  
            scaler = joblib.load('Model Experiment /Raw Data/scaler.pkl') 
            return model, scaler
        except Exception as e:
            self.logger.error(f"Error loading model or scaler: {e}")
            return None, None

    # Predict function
    def predict(self, data):
        try:
            # Load the model and scaler
            model, scaler = self.load_model_and_scaler()
            if not model or not scaler:
                return {"error": "Error loading model/scaler"}

            # Column names used during model training (must match the trained model's features)
            columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 
                       'oldpeak', 'slope', 'ca', 'thal']

            # Convert JSON data to pandas DataFrame
            # If the input is a single sample, wrap it in a list to create a DataFrame
            input_df = pd.DataFrame([data], columns=columns)
            self.logger.info(f"Input data converted to DataFrame: {input_df}")

            # Scale the input data
            scaled_inputs = scaler.transform(input_df)

            # Log the scaled inputs for debugging
            self.logger.info(f"Scaled input data: {scaled_inputs}")

            # Predict using the KNN model
            prediction = model.predict(scaled_inputs)

            # Return prediction result
            prediction_result = int(prediction[0])
            self.logger.info(f"Prediction result: {prediction_result}")
            
            return {"prediction": prediction_result}

        except Exception as e:
            self.logger.error(f"Error during prediction: {e}")
            return {"error": "Prediction failed"}
