# 🧠 Deep Learning

Este portafolio contiene proyectos de Deep Learning que demuestran el uso de redes neuronales profundas para resolver problemas complejos de clasificación, procesamiento de secuencias y visión por computadora.

## 📚 Proyectos Incluidos

### 1. [Clasificación de Secuencias con LSTM](./clasificacion_secuencias_lstm/)
**Notebook:** [`clasificacion_secuencias_lstm.ipynb`](./clasificacion_secuencias_lstm/clasificacion_secuencias_lstm.ipynb)

**Objetivo:** Implementar un modelo LSTM para clasificación de sentimientos en reseñas de películas del dataset IMDB.

**Descripción:** Este proyecto utiliza redes LSTM (Long Short-Term Memory) para analizar secuencias de texto y clasificar reseñas de películas como positivas o negativas. Incluye un análisis exhaustivo de 7+ iteraciones de optimización, comparando diferentes arquitecturas (LSTM pura, CNN+LSTM, Bidirectional LSTM, Stacked LSTM) y técnicas de regularización.

**Resultados clave:**
- **Mejor resultado:** Bidirectional LSTM con 87.66% de test accuracy
- Callbacks (EarlyStopping + ReduceLROnPlateau) mejoraron resultados de ~83% a ~87%
- Experimentación con embeddings pre-entrenados (GloVe) y fine-tuning

**Tecnologías utilizadas:**
- TensorFlow/Keras
- LSTM (Long Short-Term Memory)
- Embeddings (GloVe)
- Procesamiento de secuencias

**Temas cubiertos:**
- Procesamiento de texto
- Redes neuronales recurrentes (RNN)
- LSTM para clasificación de secuencias
- Embeddings pre-entrenados
- Análisis de sentimientos

---

### 2. [Clasificación de Imágenes con CNN](./clasificacion_imagenes_cnn/)
**Notebooks:** 
- [`01_cnn_template.ipynb`](./clasificacion_imagenes_cnn/01_cnn_template.ipynb) - CNN desde cero
- [`02_cnn_template.ipynb`](./clasificacion_imagenes_cnn/02_cnn_template.ipynb) - Reducción de sobreentrenamiento
- [`03_cnn_template.ipynb`](./clasificacion_imagenes_cnn/03_cnn_template.ipynb) - Transfer learning
- [`04_cnn_template_.ipynb`](./clasificacion_imagenes_cnn/04_cnn_template_.ipynb) - Optimización avanzada

**Objetivo:** Construir y optimizar redes neuronales convolucionales (CNN) para clasificación de imágenes (perros vs gatos).

**Descripción:** Serie de proyectos que progresan desde la construcción de una CNN básica hasta técnicas avanzadas de optimización. Incluye experimentación exhaustiva con data augmentation, análisis sistemático de valores de dropout (0.1 a 0.9), transfer learning con Inception V3, y aplicación a diferentes dominios (perros/gatos → flores).

**Resultados clave:**
- **Mejor dropout:** 0.5 (val accuracy: 78.40%)
- **Inception V3:** Mejora de ~70% a ~74-76% en clasificación de flores
- Data augmentation reduce significativamente el sobreajuste
- Transfer learning funciona con diferentes tamaños de imagen (299x299 → 150x150)

**Tecnologías utilizadas:**
- TensorFlow/Keras
- CNN (Convolutional Neural Networks)
- Transfer Learning
- Data Augmentation
- Dropout

**Temas cubiertos:**
- Arquitecturas CNN
- Clasificación de imágenes
- Data augmentation
- Regularización (dropout)
- Transfer learning
- Fine-tuning

---

### 3. [Detección de Objetos con YOLO](./deteccion_objetos_yolo/)
**Notebook:** [`yolo.ipynb`](./deteccion_objetos_yolo/yolo.ipynb)

**Objetivo:** Implementar detección de objetos en tiempo real utilizando YOLOv5.

**Descripción:** Este proyecto utiliza YOLOv5 (You Only Look Once) para detectar y localizar objetos en imágenes. YOLO divide la imagen en cuadrículas y predice dónde están los objetos y qué son en una sola pasada, siendo mucho más rápido que otros métodos. Se entrena durante 50 épocas en COCO128 y se evalúa en diferentes tipos de imágenes.

**Resultados clave:**
- Entrenamiento exitoso durante 50 épocas en dataset COCO128
- Detección precisa de múltiples objetos en una sola pasada
- Visualización de detecciones en validación y en imágenes externas (Picsum)
- Aplicación práctica previa: Detección de personajes vs objetos en videos de Fortnite para un recomendador de emotes

**Tecnologías utilizadas:**
- PyTorch
- YOLOv5
- OpenCV
- Detección de objetos

**Temas cubiertos:**
- Detección de objetos
- YOLO (You Only Look Once)
- Entrenamiento de modelos de visión
- Evaluación de detección

---

### 4. [Redes Neuronales DNN](./redes_neuronales_dnn/)
**Notebooks:**
- [`S5_DL_practice1_XOR.ipynb`](./redes_neuronales_dnn/notebooks/S5_DL_practice1_XOR.ipynb) - Problema XOR
- [`S5_DL_practice1_FasMNIST.ipynb`](./redes_neuronales_dnn/notebooks/S5_DL_practice1_FasMNIST.ipynb) - Fashion MNIST

**Objetivo:** Implementar y optimizar redes neuronales densas (DNN) para problemas de clasificación.

**Descripción:** Dos proyectos que demuestran el uso de redes neuronales multicapa: uno resuelve el problema clásico XOR (no linealmente separable) y otro clasifica imágenes de ropa del dataset Fashion MNIST. El proyecto Fashion MNIST incluye experimentación exhaustiva con normalización (3 tipos), optimización de learning rate, y callbacks avanzados.

**Resultados clave:**
- **Fashion MNIST:** ReduceLROnPlateau mejora de 88.25% a 90.14% de precisión
- **Mejor normalización:** Estandarización N(0,1) con 88.71% de precisión
- **Learning rate óptimo:** 0.001 (balance entre velocidad y precisión)
- **XOR:** Resolución exitosa con arquitectura 2-2-1, demostrando la necesidad de capas ocultas

**Tecnologías utilizadas:**
- TensorFlow/Keras
- DNN (Deep Neural Networks)
- Optimización de hiperparámetros
- Procesamiento de imágenes

**Temas cubiertos:**
- Redes neuronales densas
- Problemas no linealmente separables
- Clasificación multiclase
- Optimización de modelos
- Preprocesamiento de datos

---

## 🛠️ Tecnologías Utilizadas

- **Frameworks:** TensorFlow, Keras, PyTorch
- **Redes Neuronales:** LSTM (Bidirectional, Stacked), CNN, DNN, YOLO
- **Modelos Pre-entrenados:** Inception V3, VGG, ResNet, GloVe
- **Procesamiento:** Texto, Imágenes, Secuencias
- **Técnicas:** Transfer Learning, Data Augmentation, Regularización (Dropout, L2, SpatialDropout1D)
- **Callbacks:** ReduceLROnPlateau, EarlyStopping
- **Optimización:** SGD, Adam, AdamW

## 📖 Temas Cubiertos

### Fundamentos
- Redes neuronales profundas (DNN)
- Problemas no linealmente separables (XOR)
- Normalización de datos (escalado, centrado, estandarización)
- Optimización de learning rate
- Callbacks avanzados (ReduceLROnPlateau, EarlyStopping)

### Procesamiento de Secuencias
- LSTM (Long Short-Term Memory)
- Bidirectional LSTM
- Stacked LSTM
- CNN + LSTM para secuencias
- Embeddings pre-entrenados (GloVe)
- Análisis de sentimientos en texto

### Visión por Computadora
- CNN (Convolutional Neural Networks)
- Data augmentation exhaustivo
- Regularización (Dropout, SpatialDropout1D)
- Transfer learning (Inception V3, VGG, ResNet)
- Fine-tuning de modelos pre-entrenados
- Detección de objetos (YOLO)

### Optimización y Regularización
- Experimentación sistemática con hiperparámetros
- Análisis de curvas de aprendizaje
- Técnicas de regularización avanzadas
- Comparación de arquitecturas

## 🚀 Cómo Navegar este Portafolio

1. Cada proyecto tiene su propia carpeta con el notebook correspondiente
2. Los notebooks están listos para ejecutarse (requieren las dependencias instaladas)
3. Cada proyecto incluye explicaciones y análisis de resultados
4. Los modelos están entrenados y listos para evaluación

## 📝 Notas

- Algunos proyectos requieren GPU para entrenamiento eficiente
- Los datasets se descargan automáticamente o están incluidos
- Los modelos entrenados pueden estar guardados en formato `.keras` o `.h5`

## 📄 Licencia

Este portafolio es de uso personal y educativo.

