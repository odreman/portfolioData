# Clasificación de Sentimientos en Tweets

## 📋 Descripción

Este proyecto aborda un problema de clasificación de texto real trabajando con tweets descargados sobre las elecciones de EEUU en 2016. El enfoque principal está en el preprocesamiento, que es crucial en un problema en el que el protagonista es el texto. Se aplican técnicas avanzadas de limpieza y preparación de texto antes de la clasificación.

## 🎯 Objetivos

- Preprocesar texto de tweets para clasificación
- Aplicar técnicas de limpieza de texto específicas para redes sociales
- Clasificar sentimientos en tweets
- Evaluar modelos de clasificación
- Visualizar resultados y palabras frecuentes

## 📊 Datos

- `data/gop_tweets_train_psn.csv`: Dataset de entrenamiento con tweets etiquetados
- `data/gop_tweets_test_psn.csv`: Dataset de prueba con tweets etiquetados
  - Columnas: `sentiment` (etiqueta) y `text` (tweet)

## 🛠️ Herramientas Utilizadas

- **Python** para análisis y clasificación
- **Pandas** para manipulación de datos de tweets
- **NLTK** para procesamiento de lenguaje natural
- **Scikit-learn** para clasificación de texto
- **WordCloud** para visualización de palabras frecuentes
- **Matplotlib/Seaborn** para visualización y matrices de confusión
- **Jupyter Notebook** para análisis interactivo

## 📂 Estructura del Proyecto

```
clasificacion_sentimientos_tweets/
├── data/
│   ├── gop_tweets_train_psn.csv
│   └── gop_tweets_test_psn.csv
├── clasificacion_sentimientos_tweets.ipynb
└── README.md
```

## 🔍 Técnicas Aplicadas

### Preprocesamiento de Texto
- Limpieza de tweets (hashtags, menciones, URLs)
- Tokenización y normalización
- Eliminación de stopwords
- Extracción de características de texto

### Clasificación
- Vectorización de texto (CountVectorizer)
- Modelos de clasificación (LinearSVC)
- Pipeline de preprocesamiento y clasificación
- Evaluación con métricas (matriz de confusión, classification report)

### Visualización
- WordCloud de palabras frecuentes por sentimiento
- Matrices de confusión
- Análisis de resultados

## 📝 Temas Cubiertos

- Preprocesamiento de texto para clasificación
- Limpieza de tweets (hashtags, menciones, URLs)
- Tokenización y normalización
- Extracción de características de texto
- Clasificación de sentimientos
- Evaluación de modelos (matrices de confusión, métricas)
- Visualización de resultados

## 🚀 Ejecución

Para ejecutar el análisis:

```bash
cd clasificacion_sentimientos_tweets
jupyter notebook clasificacion_sentimientos_tweets.ipynb
```

## 📄 Notas

- El preprocesamiento es crucial para obtener buenos resultados en clasificación de texto
- Los tweets requieren limpieza específica debido a su formato (hashtags, menciones, URLs)
- Se requiere descargar recursos de NLTK la primera vez que se ejecuta

