# Clasificación de Satisfacción de Pasajeros de Aerolínea

## 📋 Descripción

Este proyecto realiza un análisis completo de satisfacción de pasajeros de aerolínea utilizando múltiples algoritmos de machine learning. El proyecto incluye análisis exploratorio exhaustivo, preprocesamiento avanzado de datos, feature engineering, y comparación de múltiples modelos incluyendo MLP, SVM, y ensembles (Random Forest, XGBoost) con optimización de hiperparámetros.

## 🎯 Objetivo

Desarrollar modelos de clasificación para predecir la satisfacción de pasajeros de aerolínea, comparando diferentes algoritmos de machine learning y seleccionando el mejor modelo basado en métricas de evaluación. El proyecto demuestra un flujo completo desde el análisis exploratorio hasta la optimización y evaluación de modelos.

## 📊 Dataset

- **Dataset:** `airline.csv`
- **Tamaño:** 25,976 registros
- **Variables:** 25 columnas incluyendo:
  - Datos demográficos (edad, género)
  - Preferencias de viaje (tipo de cliente, clase, tipo de viaje)
  - Experiencia de vuelo (distancia, retrasos, servicios a bordo)
  - Variable objetivo: satisfacción (satisfecho/neutral o insatisfecho)

## 🛠️ Herramientas Utilizadas

- **Python** para desarrollo y análisis
- **Pandas** para manipulación de datos
- **NumPy** para operaciones numéricas
- **Scikit-learn** para modelos de machine learning:
  - MLPClassifier (Red Neuronal)
  - SVC (Support Vector Machine)
  - RandomForestClassifier
  - XGBoost
  - DecisionTreeClassifier
  - KNeighborsClassifier
  - GridSearchCV y RandomizedSearchCV para optimización
- **Matplotlib/Seaborn** para visualizaciones
- **Statsmodels** para análisis de multicolinealidad (VIF)
- **Jupyter Notebook** para análisis interactivo

## 📝 Temas Cubiertos

### Análisis de Datos
- Análisis exploratorio de datos (EDA)
- Análisis de distribución de variables
- Análisis de correlaciones
- Identificación de outliers
- Análisis de balance de clases
- Análisis de multicolinealidad (VIF)

### Preprocesamiento
- Manejo de valores faltantes
- Feature engineering (creación de features compuestas)
- One-hot encoding de variables categóricas
- Reducción de multicolinealidad con PCA
- Tratamiento de outliers (capping)
- Escalado de features (StandardScaler)

### Modelado
- **MLP (Multi-Layer Perceptron)**: Red neuronal con optimización de hiperparámetros
- **SVM (Support Vector Machine)**: Optimizado con GridSearchCV
- **Ensembles**: Random Forest y XGBoost con optimización avanzada
- Optimización de hiperparámetros con GridSearchCV y RandomizedSearchCV
- Validación cruzada
- Optimización de threshold de clasificación

### Evaluación
- Métricas: Accuracy, Precision, Recall, F1-Score
- Matrices de confusión
- Análisis de importancia de features
- Comparación de modelos
- Análisis de errores (falsos positivos/negativos)

## 🚀 Ejecución

### Requisitos Previos
- Python 3.x
- Dataset `airline.csv` en el directorio del proyecto

### Instalación de Dependencias

Se recomienda crear un entorno virtual para este proyecto.

```bash
# Crear entorno virtual (opcional)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalación de librerías principales
pip install pandas numpy scikit-learn matplotlib seaborn xgboost statsmodels
```

### Ejecutar el Análisis

```bash
cd clasificacion_satisfaccion_aerolinea
jupyter notebook clasificacion_satisfaccion_aerolinea.ipynb
```

## 📊 Resultados Destacados

### Mejor Modelo: XGBoost Optimizado
- **Accuracy:** 88.45%
- **F1-Score:** 86.21%
- **Precision:** 89.33%
- **Recall:** 83.30%

### Comparación de Modelos
- **MLP (Optimizado):** Red neuronal con GridSearchCV
- **SVM (Optimizado):** Support Vector Machine con optimización de hiperparámetros
- **Random Forest:** Ensemble con 100 estimadores
- **XGBoost:** Gradient boosting con optimización avanzada
- **Decision Tree:** Modelo base
- **KNN:** K-Nearest Neighbors

### Insights Clave
- Las features más importantes son: clase de vuelo, tipo de viaje, y lealtad del cliente
- La experiencia digital (online boarding, wifi, entretenimiento) tiene alta correlación con satisfacción
- Los retrasos significativos (>30 min) impactan negativamente la satisfacción

## 📄 Estructura del Proyecto

```
clasificacion_satisfaccion_aerolinea/
├── clasificacion_satisfaccion_aerolinea.ipynb
├── airline.csv
└── README.md
```

## 📄 Licencia

Este portafolio es de carácter educativo y personal.

---

**Última actualización:** 2024

