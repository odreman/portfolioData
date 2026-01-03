# Portafolio de Machine Learning Operations (MLOps)

Bienvenido a mi portafolio de proyectos de Machine Learning Operations (MLOps). Este repositorio contiene proyectos que demuestran habilidades en experimentación, gestión y despliegue de modelos de machine learning utilizando herramientas profesionales de MLOps como MLflow y FastAPI.

## 📚 Proyectos

### 1. [Experimentación con MLflow: Predicción de Tarifas de Taxi en NYC](./experimentacion_mlflow/)

**📓 Notebook:** [experimentacion_mlflow.ipynb](./experimentacion_mlflow/experimentacion_mlflow.ipynb)

**Objetivo:** Demostrar el uso práctico de MLflow para la experimentación y gestión de modelos de machine learning, trabajando con un dataset real de viajes de taxi en Nueva York.

**Descripción:** Este proyecto trabaja con un dataset real de más de 1 millón de registros de viajes de taxi en NYC. Se entrenan y comparan múltiples algoritmos de regresión (Linear Regression, Lasso, Ridge, Random Forest, XGBoost) utilizando MLflow para registrar experimentos, métricas, parámetros y modelos. El objetivo principal es demostrar cómo MLflow puede guiar las decisiones en el proceso de experimentación y selección de modelos, no solo obtener el mejor modelo.

**Resultados destacados:**
- Mejor modelo: XGBoost con RMSE de 0.7433 y R² de 0.9836
- Comparación sistemática de 4 modelos diferentes
- Optimización de hiperparámetros con GridSearchCV
- Tracking completo de más de 10 experimentos

**Tecnologías utilizadas:**
- **MLflow** - Tracking de experimentos y gestión de modelos
- **Scikit-learn** - Modelos de machine learning
- **XGBoost** - Gradient boosting avanzado
- **Pandas/NumPy** - Manipulación de datos
- **Matplotlib/Seaborn** - Visualizaciones

**Temas cubiertos:**
- Experimentación sistemática con MLflow
- Tracking de experimentos, métricas y modelos
- Comparación de múltiples algoritmos
- Optimización de hiperparámetros
- Feature engineering
- Análisis de importancia de features
- Gestión del ciclo de vida de modelos

---

### 2. [Despliegue de Modelo como Servicio Web](./despliegue_modelo_servicio_web/)

**📁 Aplicación:** [app/main.py](./despliegue_modelo_servicio_web/app/main.py)

**Objetivo:** Desplegar el modelo entrenado en el proyecto anterior como un servicio web accesible mediante API REST y una interfaz web.

**Descripción:** Este proyecto demuestra cómo desplegar un modelo de machine learning entrenado y registrado en MLflow como un servicio web utilizando FastAPI. El servicio permite realizar predicciones de tarifas de taxi en tiempo real a través de una API REST y una interfaz web interactiva. Cada predicción se registra en MLflow para monitoreo y análisis posterior, demostrando un flujo completo de MLOps desde el entrenamiento hasta el despliegue.

**Características:**
- API REST con validación robusta de datos
- Interfaz web interactiva con Bootstrap
- Integración completa con MLflow Model Registry
- Monitoreo de predicciones en tiempo real
- Cálculo automático de features (distancia, duración, características temporales)

**Tecnologías utilizadas:**
- **FastAPI** - Framework para crear APIs REST
- **Pydantic** - Validación de datos
- **MLflow** - Carga de modelos desde Model Registry
- **Uvicorn** - Servidor ASGI
- **HTML/CSS/JavaScript** - Interfaz web

**Temas cubiertos:**
- Despliegue de modelos de machine learning
- Creación de APIs REST con FastAPI
- Validación de datos con Pydantic
- Integración de MLflow con servicios web
- Preprocesamiento de datos en producción
- Interfaz web para modelos de ML
- Monitoreo de predicciones

---

## 🛠️ Stack Tecnológico

- **Python 3.x**
- **MLflow** - Plataforma de MLOps para tracking y gestión de modelos
- **FastAPI** - Framework moderno para APIs REST
- **Scikit-learn** - Biblioteca de machine learning
- **XGBoost** - Gradient boosting avanzado
- **Pandas/NumPy** - Manipulación y procesamiento de datos
- **Pydantic** - Validación de datos
- **Matplotlib/Seaborn** - Visualización de datos
- **Uvicorn** - Servidor ASGI para FastAPI

## 📖 Temas Cubiertos

### Experimentación y Tracking
- Experimentación sistemática con MLflow
- Tracking de experimentos de machine learning
- Gestión del ciclo de vida de modelos (MLOps)
- Comparación y selección de modelos
- Optimización de hiperparámetros
- Reproducibilidad en machine learning

### Despliegue y Producción
- Despliegue de modelos como servicios web
- Creación de APIs REST para modelos de ML
- Validación de datos en producción
- Monitoreo y logging de predicciones
- Integración de MLflow con servicios web
- Preprocesamiento de datos en tiempo real

## 🚀 Cómo Navegar este Portafolio

Los proyectos están diseñados para seguir un flujo completo de MLOps:

1. **Experimentación con MLflow**: 
   - Entrenamiento, comparación y selección de modelos
   - Tracking de experimentos y métricas
   - Optimización de hiperparámetros
   - Registro del mejor modelo en MLflow Model Registry

2. **Despliegue de Modelo**: 
   - Carga del modelo desde MLflow Model Registry
   - Publicación del modelo como servicio web
   - API REST y interfaz web para predicciones
   - Monitoreo de predicciones en producción

Cada proyecto incluye:
- Documentación detallada en el README
- Código completo y comentado
- Instrucciones de ejecución
- Ejemplos de uso
- Documentación en PDF con detalles del proceso

## 📝 Notas

- Los proyectos están diseñados para trabajar en conjunto
- Se requiere MLflow server ejecutándose para ambos proyectos
- El modelo del primer proyecto se utiliza en el segundo
- Todos los proyectos incluyen documentación completa en PDF
- El flujo completo demuestra un pipeline de MLOps profesional

## 📄 Licencia

Este portafolio es de carácter educativo y personal.

---

**Última actualización:** 2024
