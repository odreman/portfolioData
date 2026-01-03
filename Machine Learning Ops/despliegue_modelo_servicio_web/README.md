# Despliegue de Modelo como Servicio Web

## 📋 Descripción

Este proyecto demuestra cómo desplegar un modelo de machine learning entrenado y registrado en MLflow (desde el proyecto de experimentación) como un servicio web utilizando FastAPI. El servicio permite realizar predicciones de tarifas de taxi en tiempo real a través de una API REST y una interfaz web interactiva. Cada predicción se registra en MLflow para monitoreo y análisis posterior.

## 🎯 Objetivos

- Desplegar un modelo de MLflow como servicio web accesible
- Crear una API REST con FastAPI para predicciones en tiempo real
- Implementar una interfaz web para interacción con el modelo
- Registrar predicciones en MLflow para monitoreo continuo
- Validar y preprocesar datos de entrada de forma robusta
- Demostrar integración completa entre MLflow y servicios web

## 🛠️ Herramientas Utilizadas

- **FastAPI** para crear la API REST
- **Pydantic** para validación de datos de entrada
- **MLflow** para cargar el modelo entrenado desde Model Registry
- **Pandas/NumPy** para preprocesamiento de datos
- **Uvicorn** como servidor ASGI
- **HTML/CSS/Bootstrap** para la interfaz web
- **JavaScript** para interacción del frontend

## 📂 Estructura del Proyecto

```
despliegue_modelo_servicio_web/
├── app/
│   ├── main.py              # Aplicación FastAPI principal
│   ├── requirements.txt      # Dependencias del proyecto
│   ├── run.sh               # Script de inicio del servidor
│   ├── templates/
│   │   └── index.html       # Interfaz web interactiva
│   └── [documentación en PDF]
├── [documentación en PDF]
└── README.md
```

## 🔍 Funcionalidades Implementadas

### API REST

#### Endpoint: `/predict` (POST)
- **Descripción:** Realiza una predicción de tarifa de taxi
- **Validación:** 
  - Formato de fecha y hora válido
  - Número de pasajeros entre 1 y 6
  - Coordenadas geográficas válidas (latitud: -90 a 90, longitud: -180 a 180)
- **Procesamiento:**
  - Extracción de características temporales (hora, día de semana, mes)
  - Cálculo de distancia usando fórmula de Haversine
  - Estimación de duración del viaje
  - Generación de features adicionales (is_weekend, avg_speed)
- **Respuesta:** Predicción de tarifa, ID de predicción, características calculadas
- **Tracking:** Cada predicción se registra en MLflow como un experimento

#### Endpoint: `/health` (GET)
- **Descripción:** Verifica el estado del servicio y disponibilidad del modelo
- **Respuesta:** Estado del servicio y confirmación de carga del modelo

#### Endpoint: `/` (GET)
- **Descripción:** Información básica del servicio y enlaces a documentación

#### Endpoint: `/docs` (GET)
- **Descripción:** Documentación interactiva automática de la API (Swagger UI)

### Interfaz Web

- **Formulario interactivo** para ingresar datos del viaje:
  - Fecha y hora de recogida
  - Coordenadas de pickup y dropoff
  - Número de pasajeros
- **Validación en tiempo real** de los campos
- **Visualización de resultados** de predicción
- **Diseño responsive** con Bootstrap

### Integración con MLflow

#### Carga del Modelo
- Modelo cargado desde MLflow Model Registry: `models:/taxi_fare_predictor/Production`
- Manejo de errores si el modelo no está disponible

#### Registro de Predicciones
- Cada predicción se registra como un run en MLflow
- **Parámetros registrados:**
  - Fecha y hora de pickup
  - Coordenadas de pickup y dropoff
  - Número de pasajeros
- **Métricas registradas:**
  - Distancia del viaje calculada
  - Duración estimada
  - Tarifa predicha
  - Timestamp de la predicción

## 📝 Temas Cubiertos

- Despliegue de modelos de machine learning en producción
- Creación de APIs REST con FastAPI
- Validación de datos con Pydantic
- Integración de MLflow con servicios web
- Preprocesamiento de datos en producción
- Interfaz web para modelos de ML
- Monitoreo de predicciones con MLflow
- Manejo de errores y validación robusta
- Cálculo de distancias geográficas (fórmula de Haversine)

## 🚀 Ejecución

### Requisitos Previos
- Modelo entrenado y registrado en MLflow Model Registry como `taxi_fare_predictor` en stage `Production`
- MLflow server ejecutándose en `http://localhost:5001`
- Python 3.x

### Instalación de Dependencias

```bash
cd app
# Se recomienda crear un entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

pip install -r requirements.txt
```

> [!NOTE]
> Las versiones principales utilizadas son:
> - fastapi==0.109.2
> - uvicorn==0.27.1
> - mlflow==2.11.1
> - pandas==2.2.0
> - scikit-learn==1.4.0

### Ejecutar el Servicio

```bash
# Opción 1: Usar el script proporcionado
cd app
./run.sh

# Opción 2: Ejecutar directamente con uvicorn
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Acceder al Servicio

- **API Base:** http://localhost:8000
- **Documentación interactiva (Swagger):** http://localhost:8000/docs
- **Interfaz web:** http://localhost:8000 (raíz)
- **Health check:** http://localhost:8000/health

## 📊 Ejemplo de Uso

### Request (POST /predict)

```json
{
  "pickup_datetime": "2024-03-15 10:30:00",
  "pickup_longitude": -73.98215,
  "pickup_latitude": 40.75890,
  "dropoff_longitude": -73.96463,
  "dropoff_latitude": 40.76565,
  "passenger_count": 1
}
```

### Response

```json
{
  "status": "success",
  "prediction_id": "abc12345",
  "predicted_fare": 12.50,
  "input_features": {
    "trip_distance": 1.2,
    "hour": 10,
    "is_weekend": false,
    "passenger_count": 1
  }
}
```

### Uso con cURL

```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "pickup_datetime": "2024-03-15 10:30:00",
    "pickup_longitude": -73.98215,
    "pickup_latitude": 40.75890,
    "dropoff_longitude": -73.96463,
    "dropoff_latitude": 40.76565,
    "passenger_count": 1
  }'
```

## 🔍 Características Técnicas

### Validación de Datos
- **Pydantic BaseModel** para validación automática
- Validadores personalizados para:
  - Formato de fecha y hora
  - Rango de pasajeros (1-6)
  - Coordenadas geográficas válidas
- Manejo de errores descriptivos

### Preprocesamiento
- **Extracción de features temporales:**
  - Hora del día
  - Día de la semana
  - Mes
  - Indicador de fin de semana
- **Cálculo de distancia:**
  - Fórmula de Haversine para distancia geodésica
  - Conversión a millas
- **Estimación de duración:**
  - Basada en distancia y velocidad promedio
  - Conversión a minutos

### Monitoreo con MLflow
- Cada predicción genera un run en MLflow
- Tracking de inputs, features calculadas y outputs
- Timestamp de cada predicción
- Facilita análisis posterior de patrones de uso

## 📄 Documentación Adicional

- **Documentación en PDF**: Documentación detallada del proceso de despliegue y referencia del proyecto de experimentación

## 🔗 Proyecto Relacionado

Este servicio utiliza el modelo entrenado en el proyecto [Experimentación con MLflow](./../experimentacion_mlflow/), específicamente el modelo XGBoost que obtuvo el mejor rendimiento (RMSE: 0.7433, R²: 0.9836).

## 📝 Notas

- El modelo debe estar registrado en MLflow Model Registry antes de ejecutar el servicio
- Se requiere que MLflow server esté ejecutándose para cargar el modelo
- Las predicciones se registran en un experimento separado en MLflow para monitoreo
- El servicio incluye manejo robusto de errores para diferentes escenarios

## 📄 Licencia

Este portafolio es de carácter educativo y personal.

---

**Última actualización:** 2024
