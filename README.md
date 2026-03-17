# Product Recommendation System API

Deep Learning recommendation system deployed as a Flask API.

## Features

- ML model trained with product interaction data
- Custom preprocessing pipeline
- REST API for predictions
- Modular project structure

## Project Structure

API/
  helper/
    formatter.py
  app.py

Model/
  recommendation_model.keras

## API Usage

POST /predict

Example input:

{
 "features": [10,3,4.6,"male",500,4.3,"PUMA",0.82,600,"Yes","summer","plains"]
}

## Tech Stack

Python - 3.13.9    
Flask  - 3.1.3  
NumPy  - 2.4.2  
Pandas  - 3.0.0  
TensorFlow - 2.20.0  