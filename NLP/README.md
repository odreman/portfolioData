# Natural Language Processing (NLP)

Colección de 5 proyectos enfocados en procesamiento del lenguaje natural, incluyendo transcripción de audio, chatbots, preprocesamiento de texto, clasificación multi-etiqueta y word embeddings. Estos proyectos demuestran competencia en técnicas avanzadas de NLP aplicadas a problemas del mundo real.

## 📋 Proyectos Incluidos

### 1. [Transcripción de Audio con Whisper y Clasificación Zero-Shot](transcripcion_audio_whisper/)
**Notebook:** [transcripcion_audio_whisper.ipynb](transcripcion_audio_whisper.ipynb)

**Objetivo:** Demostrar cómo construir aplicaciones web con modelos Transformer para procesamiento del lenguaje natural, específicamente para transcripción de audio y clasificación de texto zero-shot.

**Descripción:** Este proyecto utiliza modelos Transformer para construir aplicaciones web interactivas. Incluye ejemplos de transcripción de audio con Whisper y clasificación de texto zero-shot, así como una demo completa de clasificador de audios zero-shot que combina ambas técnicas.

**Tecnologías utilizadas:** Transformers (Hugging Face), Gradio, Faster-Whisper, PyTorch, OpenAI Whisper

**Temas cubiertos:**
- Transcripción de audio con Whisper
- Clasificación zero-shot con modelos Transformer
- Construcción de interfaces web con Gradio
- Pipeline de procesamiento de audio y texto
- Aplicaciones interactivas de NLP

---

### 2. [Chatbot de Atención al Cliente con Gradio y OpenAI](chatbot_atencion_cliente_openai/)
**Notebook:** [chatbot_atencion_cliente_openai.ipynb](chatbot_atencion_cliente_openai.ipynb)

**Objetivo:** Implementar un chatbot de atención al cliente utilizando Gradio para la interfaz de usuario y la API de OpenAI para generar respuestas, manteniendo historial de conversación y calculando costes.

**Descripción:** Este proyecto implementa un chatbot completo para una tienda de electrónica (TechWorld) que responde preguntas sobre productos específicos. Utiliza la técnica de Chain of Thought con mensajes de rol "system" para guiar las respuestas del asistente, y calcula el coste de cada consulta al API de OpenAI.

**Tecnologías utilizadas:** OpenAI API, Gradio, Python

**Temas cubiertos:**
- Chatbots con OpenAI API
- Gestión de historial de conversación
- Chain of Thought (CoT)
- Cálculo de costes de API
- Interfaces web interactivas con Gradio
- Prompt engineering

---

### 3. [Preprocesamiento de Texto para Clasificación Multi-Etiqueta de StackOverflow](preprocesamiento_texto_stackoverflow/)
**Notebook:** [preprocesamiento_texto_stackoverflow.ipynb](preprocesamiento_texto_stackoverflow/preprocesamiento_texto_stackoverflow.ipynb)

**Objetivo:** Preprocesar texto y construir features para clasificación multi-etiqueta de posts de StackOverflow.

**Descripción:** Este proyecto es la primera parte de un sistema de clasificación multi-etiqueta para posts de StackOverflow. Se enfoca en el preprocesamiento de texto en inglés, incluyendo eliminación de stop words, normalización, tokenización y construcción de features que serán utilizadas en la segunda parte para entrenar modelos de clasificación.

**Tecnologías utilizadas:** NLTK, Pandas, NumPy, Scikit-learn, SpaCy (opcional)

**Temas cubiertos:**
- Preprocesamiento de texto
- Eliminación de stop words
- Normalización y tokenización
- Construcción de features para NLP
- Análisis de texto en inglés
- Preparación de datos para clasificación multi-etiqueta

---

### 4. [Clasificación Multi-Etiqueta de Posts de StackOverflow](clasificacion_multietiqueta_stackoverflow/)
**Notebook:** [clasificacion_multietiqueta_stackoverflow.ipynb](clasificacion_multietiqueta_stackoverflow/02_clasificador/clasificacion_multietiqueta_stackoverflow.ipynb)

**Objetivo:** Entrenar y evaluar modelos de clasificación multi-etiqueta para predecir etiquetas de posts de StackOverflow.

**Descripción:** Este proyecto es la segunda parte del sistema de clasificación multi-etiqueta. Utiliza las features construidas en la primera parte para entrenar modelos que puedan predecir múltiples etiquetas para cada post de StackOverflow, trabajando con un dataset etiquetado con 100 etiquetas distintas.

**Tecnologías utilizadas:** Scikit-learn, Pandas, NumPy, NLTK

**Temas cubiertos:**
- Clasificación multi-etiqueta
- Entrenamiento de modelos de clasificación
- Evaluación de modelos multi-etiqueta
- Feature engineering para NLP
- Análisis de rendimiento de modelos

---

### 5. [Word Embeddings para Encontrar Preguntas Similares en StackOverflow](word_embeddings_similitud_stackoverflow/)
**Notebook:** [word_embeddings_similitud_stackoverflow.ipynb](word_embeddings_similitud_stackoverflow/03_word_embeddings_challenge/word_embeddings_similitud_stackoverflow.ipynb)

**Objetivo:** Resolver el problema de encontrar preguntas duplicadas o similares en StackOverflow utilizando word embeddings y técnicas de similitud semántica.

**Descripción:** Este proyecto implementa un sistema de búsqueda de preguntas similares en StackOverflow utilizando word embeddings. Cuando un usuario escribe el título de una nueva pregunta, el sistema muestra un conjunto de preguntas similares para verificar si ya existe una pregunta duplicada. Utiliza embeddings pre-entrenados (Word2Vec de Google) y sentence embeddings (SentenceTransformers) para medir similitud semántica.

**Tecnologías utilizadas:** Gensim, SentenceTransformers, NumPy, Scikit-learn, NLTK

**Temas cubiertos:**
- Word embeddings (Word2Vec)
- Sentence embeddings
- Similitud semántica
- Problemas de ranking e information retrieval
- Métricas: Hits@K, DCG@K
- Preprocesamiento de texto para embeddings
- Entrenamiento de embeddings personalizados

---

## 🛠️ Tecnologías Utilizadas

### Procesamiento de Lenguaje Natural
- **Transformers (Hugging Face)** - Modelos pre-entrenados de NLP
- **NLTK** - Procesamiento básico de texto
- **SpaCy** - Procesamiento avanzado de lenguaje natural
- **Gensim** - Word embeddings y topic modeling
- **SentenceTransformers** - Sentence embeddings

### Modelos y APIs
- **OpenAI API** - Modelos de lenguaje para chatbots
- **Whisper** - Transcripción de audio
- **Faster-Whisper** - Implementación optimizada de Whisper
- **Word2Vec** - Word embeddings pre-entrenados

### Interfaz y Desarrollo
- **Gradio** - Construcción de interfaces web interactivas
- **PyTorch** - Framework de deep learning
- **Pandas** - Manipulación de datos
- **NumPy** - Computación numérica
- **Scikit-learn** - Machine learning y evaluación

---

## 📖 Temas Cubiertos

### Procesamiento de Audio
- Transcripción de audio con Whisper
- Procesamiento de señales de audio
- Clasificación de contenido de audio

### Chatbots y Conversación
- Construcción de chatbots con APIs
- Gestión de historial de conversación
- Chain of Thought (CoT)
- Prompt engineering
- Cálculo de costes de APIs

### Preprocesamiento de Texto
- Eliminación de stop words
- Normalización y tokenización
- Limpieza de texto
- Construcción de features

### Clasificación de Texto
- Clasificación multi-etiqueta
- Entrenamiento de modelos de clasificación
- Evaluación de modelos multi-etiqueta

### Word Embeddings y Similitud
- Word embeddings (Word2Vec, FastText)
- Sentence embeddings
- Similitud semántica
- Problemas de ranking
- Information retrieval
- Entrenamiento de embeddings personalizados

---

## 🚀 Cómo Navegar este Portafolio

1. **README Principal (este archivo)**: Visión general de todos los proyectos de NLP
2. **READMEs de Proyecto**: Cada proyecto tiene su propio README con información detallada
3. **Notebooks Jupyter**: Cada proyecto incluye un notebook completo con código, análisis y demostraciones

---

## 📝 Notas

- Todos los proyectos utilizan datasets reales o basados en datos reales
- Los notebooks incluyen análisis detallados, visualizaciones y explicaciones paso a paso
- Algunos proyectos requieren GPU para ejecutarse eficientemente (especialmente los que usan modelos Transformer grandes)
- Los proyectos demuestran diferentes aspectos del NLP, desde técnicas básicas hasta aplicaciones avanzadas con modelos Transformer
- Algunos proyectos requieren claves API (OpenAI) que deben configurarse adecuadamente

---

## 📄 Licencia

Este portafolio es de uso personal y educativo. Los datasets utilizados pueden tener sus propias licencias.

