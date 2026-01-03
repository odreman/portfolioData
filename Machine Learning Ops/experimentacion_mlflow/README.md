# Experimentación con MLflow: Predicción de Tarifas de Taxi en NYC

## 📋 Descripción

Este proyecto demuestra el uso práctico de MLflow para la experimentación y gestión de modelos de machine learning. Se trabaja con un dataset real de viajes de taxi en Nueva York (NYC Taxi Trip Data) con más de 1 millón de registros para predecir tarifas, utilizando MLflow para registrar experimentos, comparar modelos y gestionar el ciclo de vida de los modelos.

El objetivo principal no es solo obtener el mejor modelo, sino demostrar cómo MLflow puede guiar el proceso de experimentación y toma de decisiones en el desarrollo de modelos de machine learning.

## 🎯 Objetivos

- Entrenar y comparar múltiples algoritmos de machine learning (regresión)
- Utilizar MLflow para registrar experimentos, métricas, parámetros y modelos
- Ajustar hiperparámetros basándose en los resultados registrados en MLflow
- Comparar el rendimiento de diferentes algoritmos para seleccionar el mejor modelo
- Documentar el proceso de experimentación y los resultados obtenidos
- Demostrar cómo MLflow facilita la reproducibilidad y comparación sistemática de modelos

## 📊 Dataset

- **Dataset:** NYC Taxi Trip Data
- **Tamaño:** Más de 1 millón de registros (muestra de 1M para experimentación)
- **Variables principales:**
  - Fechas de pickup y dropoff
  - Coordenadas geográficas (pickup/dropoff)
  - Distancia del viaje
  - Número de pasajeros
  - Tarifa (variable objetivo)
- **Objetivo:** Predecir la tarifa del viaje (`fare_amount`)

## 🛠️ Herramientas Utilizadas

- **Python** para desarrollo y análisis
- **Pandas** para manipulación de datos
- **NumPy** para operaciones numéricas
- **Scikit-learn** para modelos de machine learning
- **XGBoost** para modelos de gradient boosting
- **MLflow** para tracking de experimentos y gestión de modelos
- **Matplotlib/Seaborn** para visualizaciones
- **Jupyter Notebook** para análisis interactivo

## 📂 Estructura del Proyecto

```
experimentacion_mlflow/
├── Taxi_Trip_Data.csv
├── experimentacion_mlflow.ipynb
├── experiment_report.md
├── [documentación en PDF]
├── [archivos de visualizaciones y resultados]
│   ├── eda_visualizations.png
│   ├── model_comparison.png
│   ├── feature_importance_*.png
│   ├── correlation_matrix.csv
│   └── [otros artefactos]
└── README.md
```

## 🔍 Proceso de Experimentación

### 1. Preparación y Exploración de Datos (EDA)

**Tracking con MLflow:**
- Registro de métricas iniciales del dataset
- Tracking de transformaciones de datos
- Logging de visualizaciones EDA como artefactos
- Análisis de valores faltantes y tipos de datos

**Preprocesamiento realizado:**
- Limpieza de datos (valores negativos, outliers)
- Conversión de fechas y creación de features temporales
- Feature engineering:
  - `hour`, `day_of_week`, `month`, `is_weekend`
  - `trip_duration` (duración del viaje en minutos)
  - `avg_speed` (velocidad promedio)
- Manejo de valores atípicos (método de desviación estándar)
- Escalado de características (StandardScaler)

**Visualizaciones generadas:**
- Distribución de tarifas
- Relación distancia vs tarifa
- Tarifa promedio por hora y día de la semana
- Matriz de correlación

### 2. Modelos Implementados

#### a. Modelo Base: Regresión Lineal
- **Propósito:** Baseline para comparaciones
- **Métricas registradas:** RMSE, MAE, R², varianza explicada
- **Características:** Coeficientes e intercept registrados
- **Visualizaciones:** Importancia de características basada en coeficientes

#### b. Random Forest con GridSearchCV
- **Búsqueda de hiperparámetros:**
  - `n_estimators`: [100, 200]
  - `max_depth`: [10, 20]
  - `min_samples_split`: [2, 5]
  - `min_samples_leaf`: [1, 2]
- **Tracking:** Resultados de cross-validation (3 folds)
- **Artefactos:** Feature importance, resultados de CV
- **Métricas:** RMSE, R², MAE en train y test

#### c. XGBoost con GridSearchCV
- **Búsqueda de hiperparámetros:**
  - `max_depth`: [3, 5]
  - `learning_rate`: [0.01, 0.1]
  - `n_estimators`: [100, 200]
  - `min_child_weight`: [1, 3]
  - `subsample`: [0.8, 1.0]
  - `colsample_bytree`: [0.8, 1.0]
- **Características avanzadas:**
  - Early stopping
  - Learning curves
  - Múltiples métricas de evaluación
- **Tracking:** Resultados detallados de CV, curvas de aprendizaje

#### d. Modelo Refinado
- **Mejoras:** Features polinómicas, validación cruzada extendida
- **Análisis:** Análisis de residuos detallado
- **Optimización:** Ajuste fino basado en resultados anteriores

### 3. Uso de MLflow para Guiar Decisiones

#### Tracking de Experimentos
- **Métricas:** RMSE, MAE, R², varianza explicada, error relativo
- **Parámetros:** Configuraciones de modelos, transformaciones, hiperparámetros
- **Artefactos:** Gráficos, resultados de CV, modelos serializados, visualizaciones

#### Comparación de Modelos
- Búsqueda sistemática de runs en MLflow
- Ordenamiento por métricas (RMSE ascendente)
- Análisis comparativo de rendimiento
- Identificación del mejor modelo

#### Análisis de Resultados
- Visualizaciones comparativas
- Análisis de trade-offs (precisión vs tiempo de ejecución)
- Evaluación de overfitting (diferencia train-test)
- Análisis de importancia de features

### 4. Decisiones Guiadas por MLflow

#### Selección de Features
- Tracking de importancia de características
- Análisis del impacto en métricas
- Identificación de features más relevantes

#### Optimización de Hiperparámetros
- Comparación de diferentes configuraciones
- Análisis de tendencias en métricas
- Selección basada en resultados de CV

#### Manejo de Overfitting
- Monitoreo de diferencias train-test
- Ajuste de complejidad del modelo
- Validación cruzada para evaluación robusta

## 📊 Resultados

### Mejor Modelo: XGBoost Detallado

**Métricas finales:**
- **RMSE:** 0.7433
- **R²:** 0.9836
- **MAE:** 0.2763
- **Mejora sobre baseline:** 11.12%
- **Tiempo de ejecución:** 289.91 segundos

### Comparación de Modelos

| Modelo | Test RMSE | Test R² | Test MAE | Train-Test Diff | Tiempo (s) |
|--------|-----------|---------|----------|-----------------|------------|
| XGBoost Detallado | 0.7433 | 0.9836 | 0.2763 | 0.0044 | 289.91 |
| Random Forest Detallado | 0.7434 | 0.9836 | 0.2699 | 0.0338 | 1023.92 |
| Modelo Refinado | 0.7525 | 0.9832 | 0.2680 | 0.0545 | 810.26 |
| Linear Regression | 0.8363 | 0.9792 | 0.3404 | 0.0456 | 2.57 |

### Hiperparámetros Óptimos (XGBoost)

- `max_depth`: 5
- `learning_rate`: 0.1
- `n_estimators`: 100
- `min_child_weight`: 3
- `subsample`: 1.0
- `colsample_bytree`: 0.8

## 📝 Temas Cubiertos

- Experimentación sistemática con MLflow
- Tracking de experimentos de machine learning
- Gestión del ciclo de vida de modelos (MLOps)
- Comparación de algoritmos de regresión
- Optimización de hiperparámetros con GridSearchCV
- Feature engineering y selección
- Análisis de importancia de features
- Visualización de resultados de modelos
- Análisis de residuos y overfitting
- Reproducibilidad en machine learning

## 🚀 Ejecución

### Requisitos Previos
- MLflow server ejecutándose en `http://localhost:5001`
- Python 3.x con las dependencias instaladas
- Dataset `Taxi_Trip_Data.csv` en el directorio del proyecto

### Instalación de Dependencias

Se recomienda crear un entorno virtual para este proyecto.

```bash
# Crear entorno virtual (opcional)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalación de librerías principales
pip install pandas numpy scikit-learn xgboost mlflow matplotlib seaborn tabulate
```

> [!NOTE]
> Las versiones específicas utilizadas en el desarrollo son:
> - pandas>=1.2
> - numpy>=1.20
> - scikit-learn
> - xgboost
> - mlflow
> - matplotlib>=3.4
> - seaborn>=0.11

### Iniciar MLflow Server

```bash
mlflow ui --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlruns --port 5001
```

### Ejecutar el Análisis

```bash
cd experimentacion_mlflow
jupyter notebook experimentacion_mlflow.ipynb
```

### Acceder a MLflow UI

Una vez ejecutado el notebook, puedes ver todos los experimentos en:
```
http://localhost:5001
```

## 📄 Resultados y Artefactos

El proyecto incluye:
- **experiment_report.md**: Reporte detallado de los experimentos con comparación de modelos
- **Documentación en PDF**: Documentación completa del proceso, metodología y resultados
- **Visualizaciones:**
  - Comparación de modelos
  - Importancia de features por modelo
  - Análisis de residuos
  - Curvas de aprendizaje (XGBoost)
- **Resultados de CV:** Archivos CSV con resultados detallados de cross-validation
- **Matrices de correlación:** Análisis de relaciones entre variables

## 💡 Lecciones Aprendidas

1. **MLflow facilitó la comparación sistemática de modelos** - La capacidad de comparar múltiples experimentos de forma visual y estructurada fue fundamental para la toma de decisiones.

2. **El tracking automático permitió identificar patrones de mejora** - Al registrar todos los parámetros y métricas, fue posible identificar qué configuraciones funcionaban mejor.

3. **La gestión de artefactos ayudó en el análisis visual** - Tener todas las visualizaciones y resultados centralizados facilitó el análisis y la documentación.

4. **Reproducibilidad mejorada** - El versionado automático de modelos y parámetros permite reproducir cualquier experimento en el futuro.

## 🔗 Siguiente Paso

Una vez seleccionado el mejor modelo (XGBoost), este se registra en MLflow Model Registry y se despliega como servicio web en el proyecto [Despliegue de Modelo como Servicio Web](./../despliegue_modelo_servicio_web/).

## 📄 Licencia

Este portafolio es de carácter educativo y personal.

---

**Última actualización:** 2024
