# Imputación de Datos y Detección de Anomalías

## 📋 Descripción

Este proyecto trabaja con datasets que contienen datos sobre inmuebles en California y la producción de electricidad. Estos datasets tienen la particularidad de poseer valores nulos/faltantes y outliers en algunas de sus variables. Se aplican técnicas de imputación de datos y detección de anomalías para lidiar con estas situaciones, incluyendo métodos estadísticos y de series temporales.

## 🎯 Objetivos

- Identificar y analizar valores faltantes en los datasets
- Aplicar técnicas de imputación de datos
- Detectar y tratar anomalías y outliers
- Analizar series temporales con descomposición estacional
- Visualizar datos imputados y anomalías detectadas

## 📊 Datos

- `housing.csv`: Dataset con información de inmuebles en California
- `electric_production.csv`: Dataset con datos de producción de electricidad (serie temporal)

## 🛠️ Herramientas Utilizadas

- **Python** para análisis de datos
- **Pandas** para manipulación de datos con valores faltantes
- **NumPy** para operaciones numéricas
- **Scikit-learn** para técnicas de imputación (SimpleImputer)
- **Statsmodels** para análisis de series temporales y descomposición estacional
- **Matplotlib** para visualización de datos y anomalías
- **Jupyter Notebook** para análisis interactivo

## 📂 Estructura del Proyecto

```
imputacion_anomalias/
├── housing.csv
├── electric_production.csv
├── imputacion_anomalias.ipynb
└── README.md
```

## 🔍 Técnicas Aplicadas

### Imputación de Valores Faltantes
- Imputación por media y mediana
- Forward fill y backward fill para series temporales
- Imputación basada en modelos

### Detección de Anomalías
- Análisis de outliers usando métodos estadísticos
- Detección basada en desviaciones estándar
- Análisis de series temporales con rolling windows
- Visualización de anomalías detectadas

### Análisis de Series Temporales
- Descomposición estacional (STL)
- Análisis de tendencias
- Identificación de patrones temporales

## 📝 Temas Cubiertos

- Identificación y análisis de valores faltantes
- Técnicas de imputación (media, mediana, forward fill, etc.)
- Detección de outliers y anomalías
- Análisis de series temporales
- Descomposición estacional
- Visualización de datos imputados y anomalías

## 🚀 Ejecución

Para ejecutar el análisis:

```bash
cd imputacion_anomalias
jupyter notebook imputacion_anomalias.ipynb
```

