# Heart Disease Prediction API [Data Mining Project 1 NMIT]

## Overview

This project provides a **Heart Disease Prediction API** built using **Flask**. The model predicts the likelihood of heart disease based on medical data. It uses the **Cleveland Heart Disease dataset** with **303 rows**, after dropping rows with null values due to the low number of missing entries. 

Three models were trained, and the **K-Nearest Neighbors (KNN)** model was selected as the final model for prediction.

## Dataset

- **Dataset**: Cleveland Heart Disease dataset
- **Rows**: 303
- **Null Handling**: Rows with missing values were dropped.
  
The dataset includes features like **age**, **sex**, **cholesterol**, **blood pressure**, **chest pain type**, and other medical attributes to predict whether the individual is at risk of heart disease.

## Technologies Used

- **Flask**: Web framework for building the API.
- **Scikit-learn**: For training the KNN model.
- **Joblib**: For serializing the trained KNN model and scaler.
- **Docker**: For containerizing the application.
- **Swagger UI**: For interactive API documentation.

---

## Getting Started

To get started with this project, follow the steps below to set it up and run it locally.


To build and run the project in production, use the following command:

<pre>
docker compose up --build
</pre>


## API Routes
<pre>
 - /swagger    - API documentation
 - /prdict     - Prediction route of the Heart Disease Prediction API
</pre>
