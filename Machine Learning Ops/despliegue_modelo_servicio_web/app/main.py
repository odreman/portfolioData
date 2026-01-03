from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, validator
import mlflow
import pandas as pd
import numpy as np
from datetime import datetime
from typing import Dict, Any
import json
import uuid

app = FastAPI(
    title="NYC Taxi Fare Predictor",
    description="API para predecir tarifas de taxi en Nueva York usando el mejor modelo entrenado y registrado en MLflow",
    version="1.0.0"
)

# Configuración de MLflow
try:
    mlflow.set_tracking_uri("http://localhost:5001")
    # Crear o obtener el experimento para predicciones
    EXPERIMENT_NAME = "taxi_fare_predictions"
    experiment = mlflow.get_experiment_by_name(EXPERIMENT_NAME)
    if experiment is None:
        experiment_id = mlflow.create_experiment(EXPERIMENT_NAME)
    else:
        experiment_id = experiment.experiment_id
    
    # Cargar el modelo
    model = mlflow.pyfunc.load_model("models:/taxi_fare_predictor/Production")
except Exception as e:
    print(f"Error en la configuración inicial: {str(e)}")
    model = None
    experiment_id = None

class TaxiRideInput(BaseModel):
    pickup_datetime: str
    pickup_longitude: float
    pickup_latitude: float
    dropoff_longitude: float
    dropoff_latitude: float
    passenger_count: int

    @validator('pickup_datetime')
    def validate_datetime(cls, v):
        try:
            pd.to_datetime(v)
            return v
        except:
            raise ValueError('Formato de fecha inválido. Use YYYY-MM-DD HH:MM:SS')

    @validator('passenger_count')
    def validate_passengers(cls, v):
        if not 1 <= v <= 6:
            raise ValueError('El número de pasajeros debe estar entre 1 y 6')
        return v

    @validator('pickup_latitude', 'dropoff_latitude')
    def validate_latitude(cls, v):
        if not -90 <= v <= 90:
            raise ValueError('Latitud debe estar entre -90 y 90')
        return v

    @validator('pickup_longitude', 'dropoff_longitude')
    def validate_longitude(cls, v):
        if not -180 <= v <= 180:
            raise ValueError('Longitud debe estar entre -180 y 180')
        return v

    class Config:
        json_schema_extra = {
            "example": {
                "pickup_datetime": "2024-03-15 10:30:00",
                "pickup_longitude": -73.98215,
                "pickup_latitude": 40.75890,
                "dropoff_longitude": -73.96463,
                "dropoff_latitude": 40.76565,
                "passenger_count": 1
            }
        }

def preprocess_input(ride: TaxiRideInput) -> pd.DataFrame:
    """Preprocesa los datos de entrada para que coincidan con el formato del modelo"""
    try:
        # Convertir a datetime
        pickup_datetime = pd.to_datetime(ride.pickup_datetime)
        
        # Calcular features
        hour = pickup_datetime.hour
        day_of_week = pickup_datetime.dayofweek
        month = pickup_datetime.month
        is_weekend = int(day_of_week >= 5)
        
        # Calcular distancia
        R = 6371  # Radio  en km
        lat1, lon1 = np.radians([ride.pickup_latitude, ride.pickup_longitude])
        lat2, lon2 = np.radians([ride.dropoff_latitude, ride.dropoff_longitude])
        
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        
        a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
        c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
        trip_distance = R * c * 0.621371  # Convertir a millas
        
        # Estimar duración y velocidad
        avg_speed = 20.0
        trip_duration = trip_distance / avg_speed * 60  # en minutos
        
        # Crear DataFrame
        features = pd.DataFrame({
            'trip_distance': [trip_distance],
            'passenger_count': [ride.passenger_count],
            'trip_duration': [trip_duration],
            'hour': [hour],
            'day_of_week': [day_of_week],
            'month': [month],
            'is_weekend': [is_weekend],
            'avg_speed': [avg_speed]
        })
        
        return features
    except Exception as e:
        raise ValueError(f"Error en el preprocesamiento: {str(e)}")

@app.post("/predict")
async def predict_fare(ride: TaxiRideInput) -> Dict[str, Any]:
    if model is None:
        raise HTTPException(status_code=500, detail="Modelo no disponible")
    if experiment_id is None:
        raise HTTPException(status_code=500, detail="MLflow no está configurado correctamente")
    
    try:
        # Generar un ID único para la predicción
        prediction_id = str(uuid.uuid4())[:8]
        
        # Preprocesar datos
        features = preprocess_input(ride)
        
        # Realizar predicción
        prediction = model.predict(features)
        predicted_fare = float(prediction[0])
        
        # Logging en MLflow
        with mlflow.start_run(run_name=f"prediction_{prediction_id}", experiment_id=experiment_id):
            # Log inputs
            mlflow.log_params({
                "pickup_datetime": ride.pickup_datetime,
                "pickup_coords": f"{ride.pickup_latitude},{ride.pickup_longitude}",
                "dropoff_coords": f"{ride.dropoff_latitude},{ride.dropoff_longitude}",
                "passenger_count": ride.passenger_count
            })
            
            # Log features calculadas
            mlflow.log_metrics({
                "trip_distance": float(features['trip_distance'].iloc[0]),
                "trip_duration": float(features['trip_duration'].iloc[0]),
                "predicted_fare": round(predicted_fare, 2)
            })
            
            # Log tiempo de predicción
            mlflow.log_metric("prediction_timestamp", datetime.now().timestamp())
        
        return {
            "status": "success",
            "prediction_id": prediction_id,
            "predicted_fare": round(predicted_fare, 2),
            "input_features": {
                "trip_distance": float(features['trip_distance'].iloc[0]),
                "hour": int(features['hour'].iloc[0]),
                "is_weekend": bool(features['is_weekend'].iloc[0]),
                "passenger_count": int(features['passenger_count'].iloc[0])
            }
        }
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en la predicción: {str(e)}")

@app.get("/health")
async def health_check() -> Dict[str, str]:
    return {
        "status": "healthy",
        "model_loaded": "yes" if model is not None else "no"
    }

@app.get("/")
async def root() -> Dict[str, str]:
    return {
        "message": "Bienvenido al Predictor de Tarifas de Taxi NYC",
        "docs": "/docs",
        "health": "/health"
    }