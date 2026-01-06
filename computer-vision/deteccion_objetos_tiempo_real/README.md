# Detección de Objetos en Tiempo Real

Este proyecto implementa un reconocedor de objetos capaz de procesar una fuente de video en tiempo real, utilizando modelos de deep learning para detectar y clasificar objetos.

## Descripción

El proyecto aborda el desafío de la detección de objetos en tiempo real mediante el uso de modelos de deep learning pre-entrenados. Se implementa un sistema completo que captura frames de video (desde webcam o archivo), los procesa con modelos de deep learning y muestra las detecciones en tiempo real con bounding boxes y etiquetas de clase.

## Objetivo

Desarrollar una aplicación que pueda detectar objetos en tiempo real desde una fuente de video (webcam o archivo de video), aplicando modelos de deep learning pre-entrenados para reconocimiento de objetos. El sistema debe procesar frames de manera eficiente y mostrar resultados en tiempo real.

## Dataset

El proyecto puede utilizar dos fuentes de video:

1. **Webcam en tiempo real**: Captura de frames directamente desde la cámara del sistema
2. **Archivo de video**: Procesamiento de un archivo de video pre-grabado (`video/s6.challenge.mp4`)

**Estructura del dataset:**
- `video/`: Carpeta con archivos de video de entrada (opcional)
  - `s6.challenge.mp4`: Video de prueba para procesamiento

## Herramientas y Técnicas Empleadas

### Bibliotecas Principales
- **TensorFlow/Keras**: Modelos de deep learning pre-entrenados
- **OpenCV**: Captura de video y procesamiento de frames
- **scikit-image**: Procesamiento de imágenes
- **NumPy**: Operaciones numéricas y manipulación de arrays
- **Matplotlib**: Visualización de resultados

### Técnicas de Procesamiento

1. **Captura de Video**
   - Conexión a webcam mediante OpenCV
   - Lectura de frames desde archivo de video
   - Procesamiento frame por frame

2. **Preprocesamiento**
   - Redimensionamiento de frames para entrada al modelo
   - Normalización de valores de píxeles
   - Preparación de datos para predicción

3. **Detección de Objetos**
   - Aplicación de modelos pre-entrenados (ResNet50, MobileNet, etc.)
   - Clasificación de objetos en cada frame
   - Decodificación de predicciones

4. **Post-procesamiento**
   - Filtrado de detecciones por confianza
   - Supresión de no-máximos (NMS) para eliminar duplicados
   - Formateo de resultados

5. **Visualización en Tiempo Real**
   - Renderizado de bounding boxes
   - Etiquetado de objetos detectados
   - Mostrar frames procesados en tiempo real

## Temas Cubiertos

- Captura de video en tiempo real
- Procesamiento de frames con modelos de deep learning
- Modelos pre-entrenados (ResNet50, MobileNet)
- Clasificación de objetos
- Visualización en tiempo real
- Optimización para procesamiento en tiempo real

## Ejecución

### Dependencias

```bash
pip install numpy pandas matplotlib scikit-image opencv-python tensorflow
```

### Cómo Usar

1. Si usas webcam, asegúrate de tener una cámara conectada
2. Si usas archivo de video, colócalo en la carpeta `video/`
3. Abre el notebook `deteccion_objetos_tiempo_real.ipynb`
4. Ejecuta las celdas en orden secuencial
5. El notebook procesará los frames y mostrará las detecciones en tiempo real

### Estructura de Ejecución

El pipeline sigue estos pasos:
1. Carga del modelo de deep learning pre-entrenado
2. Conexión a fuente de video (webcam o archivo)
3. Captura de frames
4. Preprocesamiento de frames
5. Predicción con el modelo
6. Post-procesamiento de resultados
7. Visualización en tiempo real
8. Repetición del proceso para cada frame

## Resultados Obtenidos

### Detección en Tiempo Real

- El sistema detecta exitosamente objetos en frames de video
- Las detecciones se muestran con bounding boxes y etiquetas
- El procesamiento se realiza a una velocidad adecuada para tiempo real

### Precisión del Sistema

- Los modelos pre-entrenados proporcionan alta precisión en la clasificación
- El sistema identifica correctamente múltiples objetos en la escena
- Las predicciones incluyen niveles de confianza para cada detección

## Insights Clave

1. **Modelos Pre-entrenados**: El uso de modelos pre-entrenados permite obtener resultados de alta calidad sin necesidad de entrenar desde cero, reduciendo significativamente el tiempo de desarrollo.

2. **Optimización para Tiempo Real**: El redimensionamiento de frames y la optimización del pipeline son esenciales para mantener una velocidad de procesamiento adecuada para tiempo real.

3. **Preprocesamiento**: El preprocesamiento correcto de frames (normalización, redimensionamiento) es crucial para obtener predicciones precisas del modelo.

4. **Visualización**: La visualización en tiempo real con bounding boxes y etiquetas proporciona feedback inmediato sobre el rendimiento del sistema.

## Estructura del Proyecto

```
deteccion_objetos_tiempo_real/
├── deteccion_objetos_tiempo_real.ipynb    # Notebook principal con el sistema completo
├── README.md                                # Este archivo
├── video/                                   # Directorio de videos de entrada (opcional)
│   └── s6.challenge.mp4                    # Video de prueba
└── utils.py                                 # Funciones auxiliares (si está presente)
```

## Notebook

- **[Detección de Objetos en Tiempo Real](./deteccion_objetos_tiempo_real.ipynb)** - Implementación completa del sistema de detección de objetos en tiempo real

## Licencia

Este proyecto es parte de un portafolio personal de proyectos de ciencia de datos y visión por computadora.

[Volver a Computer Vision →](../README.md)
