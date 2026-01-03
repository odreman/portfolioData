# Análisis y Visualización de Texto con WordCloud

## 📋 Descripción

Este proyecto construye un análisis de opiniones con un dataset que contiene opiniones con contenido positivo y negativo. Se utiliza un corpus de texto y se construye un WordCloud con estos datos preprocesando el texto previamente. Se aplican técnicas de procesamiento de lenguaje natural para limpiar y preparar el texto antes de la visualización.

## 🎯 Objetivos

- Preprocesar texto para análisis de sentimientos
- Generar WordClouds para visualización de palabras frecuentes
- Analizar diferencias entre opiniones positivas y negativas
- Aplicar técnicas de procesamiento de lenguaje natural
- Visualizar patrones en datos textuales

## 📊 Datos

- `reviews.txt`: Archivo de texto con reviews etiquetadas
  - Formato: `(0|1)<TABULADOR>texto`
  - 0 = opinión negativa
  - 1 = opinión positiva

## 🛠️ Herramientas Utilizadas

- **Python** para análisis de texto
- **Pandas** para manipulación de datos de texto
- **NLTK** para procesamiento de lenguaje natural (tokenización, stopwords)
- **WordCloud** para generación de nubes de palabras
- **Matplotlib** para visualización
- **Regex** para limpieza y procesamiento de texto
- **Jupyter Notebook** para análisis interactivo

## 📂 Estructura del Proyecto

```
analisis_texto_wordcloud/
├── reviews.txt
├── analisis_texto_wordcloud.ipynb
└── README.md
```

## 🔍 Técnicas Aplicadas

### Preprocesamiento de Texto
- Tokenización de palabras
- Eliminación de stopwords
- Normalización de texto (minúsculas)
- Análisis de frecuencias de palabras

### Visualización
- Generación de WordCloud para opiniones positivas
- Generación de WordCloud para opiniones negativas
- Comparación de palabras frecuentes entre ambos grupos

## 📝 Temas Cubiertos

- Preprocesamiento de texto
- Tokenización de palabras
- Eliminación de stopwords
- Análisis de frecuencias de palabras
- Generación de WordCloud
- Análisis de sentimientos básico
- Visualización de datos textuales

## 🚀 Ejecución

Para ejecutar el análisis:

```bash
cd analisis_texto_wordcloud
jupyter notebook analisis_texto_wordcloud.ipynb
```

## 📄 Notas

- Se requiere descargar recursos de NLTK (punkt, stopwords) la primera vez que se ejecuta
- Los WordClouds se generan con diferentes configuraciones para mejor visualización

