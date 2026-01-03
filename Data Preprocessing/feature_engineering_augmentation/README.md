# Feature Engineering y Data Augmentation

## 📋 Descripción

Este proyecto demuestra técnicas avanzadas de feature engineering y data augmentation trabajando con dos problemas diferentes: predicción de catástrofes en naves espaciales y detección de transmisiones enemigas. Se crean nuevas variables a partir de las existentes, se aplican técnicas de balanceo de clases (SMOTE) y se procesan imágenes para extracción de características.

## 🎯 Objetivos

- Crear nuevas variables (features) a partir de variables existentes
- Aplicar técnicas de data augmentation para imágenes
- Balancear clases desbalanceadas usando SMOTE
- Procesar imágenes con diferentes transformaciones
- Extraer características de imágenes para análisis

## 📊 Datos

- `data/starkiller_population.csv`: Dataset con información de población en naves espaciales
- `data/transmission_small.csv`: Dataset con información de transmisiones
- Imágenes en `imgs/`: Imágenes para procesamiento y transformación

## 🛠️ Herramientas Utilizadas

- **Python** para análisis y procesamiento
- **Pandas** para manipulación de datos
- **NumPy** para operaciones numéricas
- **Scikit-learn** para modelos de clasificación y preprocesamiento
- **Imbalanced-learn** para técnicas de balanceo (SMOTE, RandomUnderSampler, SMOTEENN)
- **PIL (Pillow)** para procesamiento de imágenes
- **OpenCV** para transformaciones de imágenes
- **Matplotlib/Seaborn** para visualización
- **Jupyter Notebook** para análisis interactivo

## 📂 Estructura del Proyecto

```
feature_engineering_augmentation/
├── data/
│   ├── starkiller_population.csv
│   └── transmission_small.csv
├── imgs/
│   └── [imágenes para procesamiento]
├── feature_engineering_augmentation.ipynb
└── README.md
```

## 🔍 Técnicas Aplicadas

### Feature Engineering
- Creación de variables de vulnerabilidad basadas en ubicación
- Generación de factores de rescate prioritario
- Creación de variables de privilegio y clase social
- Transformaciones de variables existentes

### Data Augmentation para Imágenes
- Conversión a escala de grises
- Ajuste de brillo y contraste
- Rotación de imágenes
- Aplicación de filtros (Gaussiano, Sobel, Laplaciano)
- Detección de bordes (Canny)
- Umbralización adaptativa
- Ecualización de histograma

### Balanceo de Clases
- SMOTE (Synthetic Minority Oversampling Technique)
- Random Under Sampling
- SMOTEENN (combinación de SMOTE y ENN)

## 📝 Temas Cubiertos

- Creación de nuevas variables (feature engineering)
- Transformaciones de variables existentes
- Data augmentation para imágenes
- Balanceo de clases desbalanceadas
- Procesamiento de imágenes (escala de grises, filtros, detección de bordes)
- Extracción de características de imágenes
- Preprocesamiento de datos para machine learning

## 🚀 Ejecución

Para ejecutar el análisis:

```bash
cd feature_engineering_augmentation
jupyter notebook feature_engineering_augmentation.ipynb
```

