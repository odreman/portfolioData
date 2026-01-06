# Preprocesamiento de Texto para Clasificación Multi-Etiqueta de StackOverflow

## 📋 Descripción

Este proyecto se enfoca en el preprocesamiento de texto y construcción de features para clasificación multi-etiqueta de posts de StackOverflow. Es la primera parte de un proyecto más amplio que incluye el entrenamiento de modelos en una segunda parte.

## 🎯 Objetivo

Preprocesar texto y construir features que permitan clasificar posts de StackOverflow con múltiples etiquetas. El objetivo es preparar los datos de manera adecuada para que los modelos de clasificación puedan aprender patrones efectivos.

## 📊 Dataset

- **Archivos:** 
  - `data/train.tsv` - Dataset de entrenamiento
  - `data/test.tsv` - Dataset de prueba
- **Estructura:** Títulos de posts de StackOverflow con etiquetas asociadas
- **Idioma:** Inglés
- **Etiquetas:** 100 etiquetas distintas posibles

## 🛠️ Tecnologías Utilizadas

- **NLTK** - Procesamiento básico de texto (stop words, tokenización)
- **Pandas** - Manipulación de datos
- **NumPy** - Computación numérica
- **Scikit-learn** - Herramientas de machine learning
- **SpaCy** - Procesamiento avanzado de lenguaje natural (opcional)

## 📖 Temas Cubiertos

- Preprocesamiento de texto
- Eliminación de stop words
- Normalización y tokenización
- Construcción de features para NLP
- Análisis de texto en inglés
- Preparación de datos para clasificación multi-etiqueta
- División de datos (train/validation/test)

## 📁 Estructura del Proyecto

```
preprocesamiento_texto_stackoverflow/
├── README.md
├── 2_preprocessing-TeoriaYChallenge/
│   ├── preprocesamiento_texto_stackoverflow.ipynb
│   ├── preprocesamiento_texto_teoria.ipynb
│   ├── data/
│   │   ├── train.tsv
│   │   └── test.tsv
│   ├── metrics.py
│   └── resources/
│       ├── 1607.01759.pdf
│       ├── quijote_largo.txt
│       └── skomoroch.png
└── environment.yml
```

## 🚀 Ejecución

1. Asegúrate de tener instaladas las dependencias:
```bash
pip install pandas numpy scikit-learn nltk spacy
```

2. Descarga los recursos de NLTK:
```python
import nltk
nltk.download('stopwords')
```

3. Abre el notebook `preprocesamiento_texto_stackoverflow.ipynb` en Jupyter

4. Ejecuta todas las celdas para ver el preprocesamiento completo

## 📈 Resultados Clave

- Texto preprocesado y normalizado
- Features construidas para clasificación
- Datos divididos en conjuntos de entrenamiento, validación y prueba
- Análisis exploratorio de los datos
- Preparación completa para la segunda parte del proyecto

## 💡 Notas Importantes

- Este proyecto es la **primera parte** de un sistema completo de clasificación
- Los datos están en **inglés**, por lo que algunas técnicas son específicas para ese idioma
- Las features construidas aquí se utilizarán en la segunda parte para entrenar modelos
- Se incluye un notebook de teoría (`preprocesamiento_texto_teoria.ipynb`) con conceptos fundamentales

## 🔗 Enlaces

- [Notebook principal](2_preprocessing-TeoriaYChallenge/preprocesamiento_texto_stackoverflow.ipynb)
- [Notebook de teoría](2_preprocessing-TeoriaYChallenge/preprocesamiento_texto_teoria.ipynb)
- [Volver al índice de NLP](../README.md)

