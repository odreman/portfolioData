# Clasificación de Secuencias con LSTM

## 📋 Descripción

Este proyecto implementa un modelo de clasificación de sentimientos utilizando redes LSTM (Long Short-Term Memory) para analizar reseñas de películas del dataset IMDB. El modelo es capaz de clasificar reseñas como positivas o negativas basándose en el contenido del texto.

El proyecto incluye un análisis exhaustivo de diferentes arquitecturas y técnicas de optimización, desde una LSTM básica hasta combinaciones avanzadas con CNN, embeddings pre-entrenados (GloVe), y técnicas de regularización.

## 🎯 Objetivo

Desarrollar y optimizar un modelo LSTM que pueda procesar secuencias de texto y realizar clasificación binaria de sentimientos con alta precisión. El proyecto explora múltiples iteraciones de optimización para encontrar la mejor configuración del modelo.

## 🔧 Tecnologías Utilizadas

- **TensorFlow/Keras:** Framework principal para deep learning
- **LSTM:** Redes neuronales recurrentes para procesamiento de secuencias
- **GloVe:** Embeddings pre-entrenados para representación de palabras
- **NumPy:** Procesamiento numérico
- **Matplotlib:** Visualización de resultados

## 📊 Dataset

- **IMDB Movie Reviews:** Dataset de 50,000 reseñas de películas etiquetadas como positivas o negativas
- Preprocesamiento: Tokenización, padding de secuencias, limitación de vocabulario

## 🏗️ Arquitecturas Implementadas

El proyecto explora múltiples arquitecturas y configuraciones:

### Arquitectura Base
1. **Embedding Layer:** Convierte palabras en vectores densos
2. **LSTM Layer:** Procesa secuencias de texto
3. **Dense Layer:** Clasificación binaria (sigmoid)

### Variaciones Implementadas

1. **LSTM con Dropout:** Regularización para reducir sobreajuste
2. **CNN + LSTM + DNN:** Combinación de capas convolucionales para extracción de características locales, seguida de LSTM para procesamiento secuencial
3. **Bidirectional LSTM:** Procesamiento bidireccional para capturar contexto en ambas direcciones
4. **Stacked LSTM:** Múltiples capas LSTM apiladas
5. **GloVe + Fine-tuning:** Embeddings pre-entrenados con ajuste fino

## 📈 Características Principales

- **Análisis de curvas de aprendizaje:** Identificación de sobreajuste y problemas de generalización
- **Múltiples iteraciones de optimización:** 7+ variaciones del modelo probadas sistemáticamente
- **Técnicas de regularización:** Dropout, SpatialDropout1D, L2 regularization, recurrent dropout
- **Callbacks avanzados:** EarlyStopping y ReduceLROnPlateau para optimización automática
- **Comparación de arquitecturas:** LSTM pura, CNN+LSTM, Bidirectional LSTM, Stacked LSTM
- **Embeddings pre-entrenados:** Experimentación con GloVe (100 dimensiones) y fine-tuning
- **Evaluación rigurosa:** Análisis detallado de resultados en conjunto de test

## 🎯 Resultados Principales

### Mejores Resultados Obtenidos

| Iteración | Configuración | Test Accuracy |
|-----------|---------------|---------------|
| **Iteración 5** | **Bidirectional LSTM (64 unidades)** | **0.8766** ⭐ |
| Iteración 1 | Full data + EarlyStopping/ReduceLROnPlateau | 0.8734 |
| Iteración 2 | + Dropout final (0.5) | 0.8736 |
| Iteración 6 | SpatialDropout1D (0.3) | 0.8711 |
| Iteración 7 | Stacked LSTM (2×64 unidades) | 0.8669 |
| GloVe + Fine-tuning | Embeddings pre-entrenados | 0.8661 |
| Iteración 3 | Adam + recurrent dropout (0.3) | 0.8628 |
| Iteración 4 | L2 reg + dropout ajustado | 0.8642 |

### Hallazgos Clave

1. **Bidirectional LSTM fue la mejor arquitectura:** Captura contexto en ambas direcciones sin añadir excesivo ruido o parámetros que requieran más datos.

2. **Callbacks fueron la mejora más efectiva:** EarlyStopping y ReduceLROnPlateau mejoraron los resultados de ~0.83 a ~0.87 sin modificar la arquitectura.

3. **Dropout final tuvo impacto limitado:** La red ya estaba suficientemente regularizada con los callbacks.

4. **Regularizaciones internas degradaron el rendimiento:** Recurrent dropout y L2 regularization introdujeron demasiado "ruido" en la memoria secuencial, penalizando la capacidad de retener contexto.

5. **Arquitecturas más complejas no mejoraron:** Stacked LSTM y combinaciones complejas habrían necesitado más datos o embeddings mejor adaptados para no sobreajustar.

6. **GloVe no superó el modelo puro:** Aunque proporcionó curvas más estables, el embedding general (Wikipedia+Gigaword) no se adaptó completamente al dominio específico de reseñas de cine.

### Análisis de Sobreajuste

- **Problema inicial:** El modelo base mostraba memorización rápida (train accuracy ~99-100%) pero generalización pobre (val accuracy ~80-82%).
  - La pérdida de validación rebotaba (picos en épocas 3, 6, 8, 10...) en lugar de descender de forma sostenida, señal de que el modelo "aprendía ruido" del conjunto de entrenamiento.
- **Solución:** Implementación de técnicas de regularización y callbacks que redujeron el gap entre entrenamiento y validación.
- **Resultado final:** Modelo con mejor balance entre capacidad de aprendizaje y generalización.

### Detalles de Iteraciones Específicas

**Iteración 1 (Full data + Callbacks):**
- Split 80/20 para entrenamiento/validación
- EarlyStopping y ReduceLROnPlateau implementados
- Mejora más efectiva: de ~0.83 a ~0.87 sin modificar arquitectura

**Iteración 2 (+ Dropout final):**
- Dropout de 0.5 antes de la capa de salida
- Impacto marginal porque la red ya estaba suficientemente regularizada

**Iteración 5 (Bidirectional LSTM):**
- 64 unidades en cada dirección
- Mejor resultado individual: 0.8766 test accuracy
- Captura contexto en ambas direcciones sin añadir excesivo ruido

**Iteración 6 (SpatialDropout1D):**
- SpatialDropout1D de 0.3 tras el Embedding
- Regularizó demasiado la entrada, dificultando la retención de secuencias clave

**Iteración 7 (Stacked LSTM):**
- Dos capas LSTM de 64 unidades cada una
- Duplicó parámetros recurrentes, insuficiente con ~20,000 ejemplos para afinar ambas capas sin sobreajustar

**GloVe + Fine-tuning:**
- Embeddings GloVe 100d (Wikipedia + Gigaword)
- Curvas muy estables con gap mínimo entre train/val
- No superó el 87% porque el embedding general no se adaptó completamente al dominio de reseñas de cine

## 🚀 Ejecución

```bash
# Instalar dependencias
pip install tensorflow numpy matplotlib

# Ejecutar notebook
jupyter notebook clasificacion_secuencias_lstm.ipynb
```

## 🔬 Metodología de Experimentación

El proyecto sigue una metodología sistemática de experimentación:

1. **Análisis inicial:** Identificación de problemas de sobreajuste mediante curvas de aprendizaje
2. **Iteración incremental:** Cada variación se basa en los resultados anteriores
3. **Comparación rigurosa:** Todas las configuraciones se evalúan en el mismo conjunto de test
4. **Análisis de resultados:** Hipótesis sobre por qué ciertas técnicas funcionan o no

### Técnicas Evaluadas

- ✅ **EarlyStopping y ReduceLROnPlateau:** Mejora más efectiva
- ✅ **Bidirectional LSTM:** Mejor arquitectura individual
- ✅ **Dropout final:** Mejora marginal pero útil
- ⚠️ **SpatialDropout1D:** Regularizó demasiado la entrada
- ❌ **Recurrent dropout:** Penalizó la memoria secuencial
- ❌ **L2 regularization:** Introdujo ruido en el aprendizaje
- ❌ **Stacked LSTM:** Requería más datos para evitar sobreajuste
- ⚠️ **GloVe + Fine-tuning:** Estable pero no superó el modelo puro

## 📝 Notas

- Se recomienda usar GPU para entrenamiento más rápido
- El modelo puede guardarse en formato `.keras` para reutilización
- Los embeddings GloVe deben descargarse previamente (glove.6B.100d.txt)
- Los modelos entrenados están guardados en formato `.keras` (best_glove_frozen.keras, best_glove_tuned.keras, best_iter*.keras)
- El dataset IMDB se carga automáticamente desde Keras

