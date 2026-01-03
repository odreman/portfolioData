# Portafolio de Preprocesamiento de Datos

Bienvenido a mi portafolio de proyectos de preprocesamiento de datos. Este repositorio contiene una colección de proyectos que demuestran habilidades en limpieza, transformación, anonimización y preparación de datos para análisis, aplicando técnicas fundamentales de ciencia de datos.

## 📚 Proyectos

### 1. [Anonimización de Datos: Airbnb Madrid](./anonimizacion_airbnb/)

**📓 Notebook:** [anonimizacion_airbnb.ipynb](./anonimizacion_airbnb/anonimizacion_airbnb.ipynb)

**Objetivo:** Aplicar técnicas de anonimización de datos a un dataset real de Airbnb, transformando datos de Madrid a Valladolid mientras se preserva la privacidad de la información sensible.

**Descripción:** Este proyecto trabaja con un dataset real que contiene los datos de los alojamientos disponibles de Airbnb para la comunidad de Madrid. Se aplican técnicas de anonimización y transformación de datos geográficos para convertir el dataset de AirBnBMadrid a AirBnBValladolid, preservando la estructura y características de los datos mientras se protege la información sensible.

**Tecnologías utilizadas:**
- **Pandas** - Manipulación y transformación de datos
- **NumPy** - Operaciones numéricas
- **Faker** - Generación de datos sintéticos para anonimización
- **SpaCy** - Procesamiento de lenguaje natural para identificación de entidades

**Temas cubiertos:**
- Anonimización de datos personales
- Transformación de datos geográficos (coordenadas, códigos postales)
- Reemplazo de información sensible con datos sintéticos
- Preservación de la estructura de datos durante la anonimización

---

### 2. [Análisis Exploratorio: Dataset de Airbnb](./analisis_airbnb/)

**📓 Notebook:** [analisis_airbnb.ipynb](./analisis_airbnb/analisis_airbnb.ipynb)

**Objetivo:** Realizar un análisis exploratorio completo de un dataset de Airbnb, respondiendo preguntas específicas sobre los datos mediante técnicas de exploración y análisis.

**Descripción:** Este análisis se enfoca en responder preguntas específicas sobre un dataset real de Airbnb, aplicando técnicas de exploración y análisis de datos. Se examinan diferentes aspectos del dataset, incluyendo características de los alojamientos, precios, ubicaciones y otros atributos relevantes.

**Tecnologías utilizadas:**
- **Pandas** - Exploración y análisis de datos
- **NumPy** - Cálculos numéricos
- **Matplotlib** - Visualización de datos

**Temas cubiertos:**
- Exploración inicial de datasets
- Análisis de tipos de datos y valores faltantes
- Estadísticas descriptivas
- Identificación de patrones y relaciones

---

### 3. [Imputación de Datos y Detección de Anomalías](./imputacion_anomalias/)

**📓 Notebook:** [imputacion_anomalias.ipynb](./imputacion_anomalias/imputacion_anomalias.ipynb)

**Objetivo:** Aplicar técnicas de imputación de valores faltantes y detección de anomalías en datasets con datos incompletos y outliers.

**Descripción:** Este proyecto trabaja con datasets que contienen datos sobre inmuebles en California y la producción de electricidad. Estos datasets tienen la particularidad de poseer valores nulos/faltantes y outliers en algunas de sus variables. Se aplican técnicas de imputación de datos y detección de anomalías para lidiar con estas situaciones, incluyendo métodos estadísticos y de series temporales.

**Tecnologías utilizadas:**
- **Pandas** - Manipulación de datos con valores faltantes
- **NumPy** - Operaciones numéricas
- **Scikit-learn** - Técnicas de imputación (SimpleImputer)
- **Statsmodels** - Análisis de series temporales y descomposición estacional
- **Matplotlib** - Visualización de datos y anomalías

**Temas cubiertos:**
- Identificación y análisis de valores faltantes
- Técnicas de imputación (media, mediana, forward fill, etc.)
- Detección de outliers y anomalías
- Análisis de series temporales
- Descomposición estacional (STL)
- Visualización de datos imputados y anomalías detectadas

---

### 4. [Feature Engineering y Data Augmentation](./feature_engineering_augmentation/)

**📓 Notebook:** [feature_engineering_augmentation.ipynb](./feature_engineering_augmentation/feature_engineering_augmentation.ipynb)

**Objetivo:** Demostrar técnicas avanzadas de feature engineering y data augmentation trabajando con problemas de predicción y clasificación.

**Descripción:** Este proyecto demuestra técnicas avanzadas de feature engineering y data augmentation trabajando con dos problemas diferentes: predicción de catástrofes en naves espaciales y detección de transmisiones enemigas. Se crean nuevas variables a partir de las existentes, se aplican técnicas de balanceo de clases (SMOTE) y se procesan imágenes para extracción de características.

**Tecnologías utilizadas:**
- **Pandas** - Manipulación de datos
- **NumPy** - Operaciones numéricas
- **Scikit-learn** - Modelos de clasificación, preprocesamiento (StandardScaler)
- **Imbalanced-learn** - Técnicas de balanceo (SMOTE, RandomUnderSampler, SMOTEENN)
- **PIL (Pillow)** - Procesamiento de imágenes
- **OpenCV** - Transformaciones de imágenes (rotación, brillo, contraste, filtros)
- **Matplotlib/Seaborn** - Visualización

**Temas cubiertos:**
- Creación de nuevas variables (feature engineering)
- Transformaciones de variables existentes
- Data augmentation para imágenes
- Balanceo de clases desbalanceadas
- Procesamiento de imágenes (escala de grises, filtros, detección de bordes)
- Extracción de características de imágenes
- Preprocesamiento de datos para machine learning

---

### 5. [Análisis y Visualización de Texto con WordCloud](./analisis_texto_wordcloud/)

**📓 Notebook:** [analisis_texto_wordcloud.ipynb](./analisis_texto_wordcloud/analisis_texto_wordcloud.ipynb)

**Objetivo:** Construir un análisis de opiniones y crear visualizaciones de texto utilizando WordCloud, aplicando técnicas de preprocesamiento de texto.

**Descripción:** Este proyecto construye un análisis de opiniones con un dataset que contiene opiniones con contenido positivo y negativo. Se utiliza un corpus de texto y se construye un WordCloud con estos datos preprocesando el texto previamente. Se aplican técnicas de procesamiento de lenguaje natural para limpiar y preparar el texto antes de la visualización.

**Tecnologías utilizadas:**
- **Pandas** - Manipulación de datos de texto
- **NLTK** - Procesamiento de lenguaje natural (tokenización, stopwords)
- **WordCloud** - Generación de nubes de palabras
- **Matplotlib** - Visualización
- **Regex** - Limpieza y procesamiento de texto

**Temas cubiertos:**
- Preprocesamiento de texto
- Tokenización de palabras
- Eliminación de stopwords
- Análisis de frecuencias de palabras
- Generación de WordCloud
- Análisis de sentimientos básico
- Visualización de datos textuales

---

### 6. [Clasificación de Sentimientos en Tweets](./clasificacion_sentimientos_tweets/)

**📓 Notebook:** [clasificacion_sentimientos_tweets.ipynb](./clasificacion_sentimientos_tweets/clasificacion_sentimientos_tweets.ipynb)

**Objetivo:** Enfrentarse a un problema de clasificación de texto real: tweets sobre las elecciones de EEUU en 2016, centrándose en el preprocesamiento de texto.

**Descripción:** Este proyecto aborda un problema de clasificación de texto real trabajando con tweets descargados sobre las elecciones de EEUU en 2016. El enfoque principal está en el preprocesamiento, que es crucial en un problema en el que el protagonista es el texto. Se aplican técnicas avanzadas de limpieza y preparación de texto antes de la clasificación.

**Tecnologías utilizadas:**
- **Pandas** - Manipulación de datos de tweets
- **NLTK** - Procesamiento de lenguaje natural
- **Scikit-learn** - Clasificación de texto
- **WordCloud** - Visualización de palabras frecuentes
- **Matplotlib/Seaborn** - Visualización y matrices de confusión

**Temas cubiertos:**
- Preprocesamiento de texto para clasificación
- Limpieza de tweets (hashtags, menciones, URLs)
- Tokenización y normalización
- Extracción de características de texto
- Clasificación de sentimientos
- Evaluación de modelos (matrices de confusión, métricas)
- Visualización de resultados

---

## 🛠️ Tecnologías Utilizadas

- **Python 3.x**
- **Pandas** - Manipulación y análisis de datos
- **NumPy** - Computación numérica
- **Scikit-learn** - Machine Learning y preprocesamiento
- **NLTK** - Procesamiento de lenguaje natural
- **Faker** - Generación de datos sintéticos
- **SpaCy** - Procesamiento avanzado de lenguaje natural
- **Imbalanced-learn** - Técnicas de balanceo de clases
- **OpenCV** - Procesamiento de imágenes
- **PIL (Pillow)** - Manipulación de imágenes
- **WordCloud** - Visualización de texto
- **Matplotlib/Seaborn** - Visualización de datos
- **Statsmodels** - Análisis de series temporales

## 📖 Temas Cubiertos

- Anonimización y privacidad de datos
- Limpieza y transformación de datos
- Manejo de valores faltantes (imputación)
- Detección y tratamiento de anomalías
- Feature engineering
- Data augmentation
- Preprocesamiento de texto
- Procesamiento de imágenes
- Balanceo de clases
- Análisis exploratorio de datos

## 🚀 Cómo Navegar este Portafolio

Cada proyecto es un notebook Jupyter independiente que contiene:
- Descripción del problema
- Análisis paso a paso
- Técnicas aplicadas
- Visualizaciones
- Interpretación de resultados

Para ejecutar un proyecto:
```bash
cd "Data Preprocessing"
jupyter notebook nombre_del_proyecto.ipynb
```

## 📝 Notas

- Todos los proyectos utilizan datos reales o de ejemplo
- Los notebooks están listos para ejecutarse
- Cada proyecto es independiente y puede ejecutarse por separado
- Los datos se cargan desde archivos CSV incluidos en los directorios

## 📄 Licencia

Este portafolio es de carácter educativo y personal.

---

**Última actualización:** 2024

