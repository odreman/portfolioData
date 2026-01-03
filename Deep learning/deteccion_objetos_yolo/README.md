# Detección de Objetos con YOLO

## 📋 Descripción

Este proyecto implementa detección de objetos en tiempo real utilizando YOLOv5 (You Only Look Once). YOLO es un algoritmo de detección de objetos que puede identificar y localizar múltiples objetos en una imagen en una sola pasada.

**¿Cómo funciona YOLO?**
YOLO divide la imagen en cuadrículas y, de una sola vez, predice dónde están los objetos y qué son. Es mucho más rápida que otros métodos porque no necesita analizar cada parte por separado, sino que ve toda la imagen de una vez. Por eso se llama "You Only Look Once".

Este proyecto demuestra la aplicación práctica de YOLO entrenando un modelo en el dataset COCO128 y evaluando su capacidad de detección en diferentes tipos de imágenes.

## 🎯 Objetivo

Entrenar y evaluar un modelo YOLOv5 para detectar objetos en imágenes, incluyendo la localización (bounding boxes) y clasificación de múltiples objetos simultáneamente.

## 🔧 Tecnologías Utilizadas

- **PyTorch:** Framework de deep learning
- **YOLOv5:** Arquitectura de detección de objetos
- **OpenCV:** Procesamiento de imágenes
- **Ultralytics:** Implementación de YOLOv5

## 📊 Dataset

- **COCO128:** Subset del dataset COCO para entrenamiento rápido
- Incluye múltiples clases de objetos
- Anotaciones en formato YOLO

### Estructura de Directorios Requerida

Para entrenar YOLO con COCO128, se debe respetar la siguiente estructura:

```
dataset/
├── images/
│   ├── train/
│   │   ├── img1.jpg
│   │   ├── img2.jpg
│   │   └── ...
│   └── val/
│       ├── img1.jpg
│       ├── img2.jpg
│       └── ...
└── labels/
    ├── train/
    │   ├── img1.txt
    │   ├── img2.txt
    │   └── ...
    └── val/
        ├── img1.txt
        ├── img2.txt
        └── ...
```

### Formato de Etiquetas YOLO

Las etiquetas en YOLO deben contener, para cada objeto en una imagen, una línea de texto con:
- **ID de la clase:** Un número empezando desde 0
- **Posición del centro:** Coordenadas X y Y normalizadas entre 0 y 1
- **Dimensiones:** Ancho y alto del objeto (también normalizados entre 0 y 1)

Formato: `class_id center_x center_y width height`

## 🏗️ Arquitectura

- **YOLOv5:** Arquitectura de detección de objetos de una sola pasada
- Backbone: CSPDarknet
- Neck: PANet
- Head: Detección multi-escala

## 📈 Características Principales

- **Entrenamiento del modelo:** 50 épocas en dataset COCO128
- **Evaluación de métricas:** mAP, precision, recall
- **Visualización de detecciones:**
  - Detecciones en conjunto de validación
  - Selección aleatoria del conjunto COCO
  - Selección aleatoria de imágenes externas (Picsum)
- **Inferencia en nuevas imágenes:** Capacidad de detectar objetos en imágenes no vistas durante el entrenamiento

## 🎯 Resultados del Entrenamiento

El modelo fue entrenado durante **50 épocas** en el dataset COCO128, logrando:
- Detección precisa de múltiples objetos en una sola pasada
- Localización mediante bounding boxes
- Clasificación simultánea de objetos
- Buen rendimiento en imágenes de validación y externas

## 💡 Aplicación Práctica

Este proyecto demuestra la versatilidad de YOLO para diferentes casos de uso. En un contexto previo, YOLO fue utilizado en un Trabajo de Fin de Máster para desarrollar un recomendador de emotes de Fortnite, donde se necesitaba extraer características de videos. Específicamente, se utilizó YOLO para evaluar si en una escena había objetos presentes o si era solo un baile o un gesto, entrenándolo para distinguir entre dos clases: **personaje** y **objetos** (cualquier cosa diferente a un personaje).

## 🚀 Ejecución

```bash
# Clonar YOLOv5
git clone https://github.com/ultralytics/yolov5
cd yolov5

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar notebook
jupyter notebook yolo.ipynb
```

## 📝 Notas

- Se requiere GPU para entrenamiento eficiente (especialmente para 50 épocas)
- El modelo puede entrenarse con diferentes tamaños (yolov5s, yolov5m, yolov5l, yolov5x)
- Los pesos pre-entrenados están disponibles para transfer learning
- El formato de etiquetas YOLO requiere coordenadas normalizadas (0-1)
- La estructura de directorios debe seguir el formato especificado para que YOLO funcione correctamente

