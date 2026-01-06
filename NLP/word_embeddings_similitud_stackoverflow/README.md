# Word Embeddings para Encontrar Preguntas Similares en StackOverflow

## 📋 Descripción

Este proyecto resuelve el problema de encontrar preguntas duplicadas o similares en un foro, aplicado específicamente a los títulos de preguntas en StackOverflow. La estrategia se basa en encontrar textos que son similares semánticamente utilizando word embeddings.

## 🎯 Objetivo

Implementar un sistema de búsqueda de preguntas similares en StackOverflow que:
- Cuando un usuario escribe el título de una nueva pregunta, muestre un conjunto de preguntas similares
- Permita verificar si ya existe una pregunta duplicada
- Utilice word embeddings para medir similitud semántica
- Evalúe la eficacia del sistema utilizando métricas de ranking

## 📊 Dataset

- **Fuente:** Títulos de preguntas de StackOverflow
- **Estructura:** Dataset con preguntas y sus duplicados identificados
- **Idioma:** Inglés
- **Uso:** Identificar preguntas similares o duplicadas

## 🛠️ Tecnologías Utilizadas

- **Gensim** - Word embeddings (Word2Vec)
- **SentenceTransformers** - Sentence embeddings
- **NumPy** - Computación numérica
- **Scikit-learn** - Herramientas de machine learning y evaluación
- **NLTK** - Procesamiento de texto

## 📖 Temas Cubiertos

- Word embeddings (Word2Vec de Google News)
- Sentence embeddings
- Similitud semántica entre textos
- Problemas de ranking e information retrieval
- Métricas: Hits@K, DCG@K
- Preprocesamiento de texto para embeddings
- Conversión de texto a embeddings (Question2Vec)
- Entrenamiento de embeddings personalizados con Gensim
- Comparación de diferentes enfoques de embeddings

## 📁 Estructura del Proyecto

```
word_embeddings_similitud_stackoverflow/
├── README.md
└── 03_word_embeddings_challenge/
    ├── word_embeddings_similitud_stackoverflow.ipynb
    ├── s03_utils.py
    ├── custom_word2vec.model
    ├── data/
    └── resources/
        ├── 1607.01759.pdf
        ├── CBOW.png
        ├── Skip-gram.png
        └── sparse_vs_dense.png
```

## 🚀 Ejecución

1. Asegúrate de tener instaladas las dependencias:
```bash
pip install gensim sentence-transformers numpy scikit-learn nltk
```

2. **Descarga de embeddings**: El proyecto utiliza Word2Vec pre-entrenado de Google News. Se descargará automáticamente la primera vez que se ejecute, o puedes descargarlo manualmente.

3. **GPU recomendada**: Para la segunda parte del análisis (sentence transformers), se recomienda el uso de GPU para mejor rendimiento.

4. Abre el notebook `word_embeddings_similitud_stackoverflow.ipynb` en Jupyter

5. Ejecuta todas las celdas para ver el análisis completo

## 📈 Resultados Clave

- Sistema de búsqueda de preguntas similares funcional
- Comparación de diferentes enfoques de embeddings
- Evaluación con métricas de ranking (Hits@K, DCG@K)
- Análisis de la efectividad de word embeddings vs sentence embeddings
- Entrenamiento de embeddings personalizados

## 💡 Características Especiales

- **Múltiples enfoques**: Compara Word2Vec, SentenceTransformers y embeddings personalizados
- **Métricas de ranking**: Utiliza Hits@K y DCG@K para evaluar el sistema
- **Preprocesamiento**: Incluye técnicas de preprocesamiento específicas para embeddings
- **Extras**: Incluye secciones adicionales sobre FastText, efecto del preprocesado en Transformers, y entrenamiento de embeddings personalizados

## 🔍 Métricas Utilizadas

- **Hits@K**: Porcentaje de casos donde la pregunta correcta está en el top K resultados
- **DCG@K**: Discounted Cumulative Gain, mide la calidad del ranking considerando la posición

## 🔗 Enlaces

- [Notebook completo](03_word_embeddings_challenge/word_embeddings_similitud_stackoverflow.ipynb)
- [Volver al índice de NLP](../README.md)

