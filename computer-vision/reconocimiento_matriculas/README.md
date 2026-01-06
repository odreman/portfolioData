# Reconocimiento de Matrículas

Este proyecto implementa una aplicación de video vigilancia capaz de reconocer las matrículas de los vehículos que aparecen en una secuencia de video, utilizando técnicas de OCR y procesamiento de imágenes.

## Descripción

El proyecto aborda el desafío del reconocimiento óptico de caracteres (OCR) aplicado específicamente a matrículas de vehículos. Se implementa un sistema completo que detecta regiones de interés, segmenta caracteres individuales y los clasifica utilizando técnicas de machine learning, proporcionando una solución robusta para aplicaciones de análisis de tráfico y sistemas de Smart Cities.

## Objetivo

Desarrollar un sistema de reconocimiento óptico de caracteres (OCR) especializado en la identificación y lectura de matrículas de vehículos. Las matrículas son un identificador único de los vehículos, por lo que ser capaz de reconocerlas es fundamental en aplicaciones de análisis de tráfico, control de acceso, gestión de estacionamientos y sistemas del ámbito de Smart Cities.

## Dataset

El proyecto utiliza imágenes del dataset de matrículas de la Universidad de Zagreb, disponible en: http://www.zemris.fer.hr/projects/LicensePlates/english/results.shtml

El dataset contiene 8 imágenes de matrículas de vehículos en diferentes condiciones de iluminación y ángulos. Cada imagen presenta desafíos típicos del reconocimiento de matrículas: variaciones en iluminación, ángulos de captura, y diferentes estilos de matrículas.

**Estructura del dataset:**
- `dataset/`: Carpeta con imágenes de matrículas (formato JPG)

## Herramientas y Técnicas Empleadas

### Bibliotecas Principales
- **scikit-image**: Procesamiento de imágenes, filtros y transformaciones
- **scikit-learn**: Clasificación con K-Nearest Neighbors (KNN)
- **OpenCV**: Operaciones avanzadas de visión por computadora
- **NumPy**: Operaciones numéricas y manipulación de arrays
- **Matplotlib**: Visualización de imágenes y resultados
- **ipywidgets**: Interfaz interactiva para ajuste de parámetros

### Técnicas de Procesamiento

1. **Preprocesamiento de Imágenes**
   - Conversión a escala de grises
   - Ajuste de contraste y brillo
   - Filtrado de ruido

2. **Detección de Regiones de Interés (ROI)**
   - Identificación de áreas que contienen matrículas
   - Extracción de ventanas de interés
   - Ajuste de perspectiva y rotación

3. **Segmentación de Caracteres**
   - Umbralización adaptativa para binarización
   - Etiquetado de componentes conectados
   - Separación de caracteres individuales
   - Filtrado de componentes por tamaño y forma

4. **Extracción de Características**
   - Generación de descriptores para cada carácter
   - Normalización de características
   - Preparación de datos para clasificación

5. **Clasificación de Caracteres**
   - Entrenamiento de modelo K-Nearest Neighbors (KNN)
   - Clasificación de caracteres individuales
   - Reconstrucción de la matrícula completa

6. **Post-procesamiento**
   - Validación de resultados
   - Corrección de errores comunes
   - Formateo de la matrícula reconocida

## Temas Cubiertos

- Reconocimiento óptico de caracteres (OCR)
- Detección de regiones de interés (ROI)
- Segmentación de caracteres
- Extracción de características de imágenes
- Clasificación con K-Nearest Neighbors
- Preprocesamiento de imágenes para OCR
- Validación y post-procesamiento de resultados

## Ejecución

### Dependencias

```bash
pip install numpy pandas matplotlib scikit-image scikit-learn opencv-python ipywidgets
```

### Cómo Usar

1. Asegúrate de tener las imágenes de matrículas en la carpeta `dataset/`
2. Asegúrate de tener el archivo `ocr.py` con las funciones auxiliares
3. Abre el notebook `reconocimiento_matriculas.ipynb`
4. Ejecuta las celdas en orden secuencial
5. El notebook procesará cada imagen y mostrará las matrículas reconocidas

### Estructura de Ejecución

El pipeline sigue estos pasos:
1. Carga del dataset de imágenes
2. Conversión a escala de grises
3. Preprocesamiento y mejora de contraste
4. Detección de regiones de interés (ROI)
5. Segmentación de caracteres individuales
6. Extracción de características
7. Clasificación con modelo KNN
8. Reconstrucción de la matrícula completa
9. Visualización de resultados

## Resultados Obtenidos

### Reconocimiento de Matrículas

- El sistema detecta exitosamente las regiones que contienen matrículas en las imágenes
- Los caracteres se segmentan correctamente de manera individual
- El modelo KNN clasifica los caracteres con alta precisión

### Precisión del Sistema

- El sistema logra reconocer matrículas en diferentes condiciones de iluminación
- La segmentación de caracteres funciona correctamente incluso con variaciones en el estilo de matrícula
- El modelo de clasificación proporciona resultados confiables para caracteres alfanuméricos

## Insights Clave

1. **Importancia del Preprocesamiento**: El preprocesamiento adecuado (ajuste de contraste, filtrado de ruido) es crucial para una segmentación precisa de caracteres.

2. **Segmentación de Caracteres**: La segmentación correcta de caracteres individuales es el paso más crítico del pipeline. Errores en esta etapa se propagan a la clasificación.

3. **Modelo KNN**: El clasificador K-Nearest Neighbors es efectivo para este tipo de problema, especialmente cuando se tienen suficientes ejemplos de entrenamiento para cada carácter.

4. **Validación de Resultados**: La validación y post-procesamiento son esenciales para corregir errores comunes y mejorar la precisión final del sistema.

## Estructura del Proyecto

```
reconocimiento_matriculas/
├── reconocimiento_matriculas.ipynb    # Notebook principal con el sistema OCR completo
├── README.md                            # Este archivo
├── dataset/                             # Dataset de imágenes con matrículas
│   └── *.jpg                            # Imágenes de matrículas
└── ocr.py                               # Funciones auxiliares (si está presente)
```

## Notebook

- **[Reconocimiento de Matrículas](./reconocimiento_matriculas.ipynb)** - Implementación completa del sistema OCR para reconocimiento de matrículas

## Licencia

Este proyecto es parte de un portafolio personal de proyectos de ciencia de datos y visión por computadora.

[Volver a Computer Vision →](../README.md)
