# Detección y Conteo de Vehículos

Este proyecto implementa un algoritmo capaz de detectar y contar vehículos que circulan en una carretera a partir de una secuencia de video de entrada, utilizando técnicas de detección de movimiento, análisis de blobs y operaciones morfológicas.

## Descripción

El proyecto aborda el desafío de analizar el tráfico vehicular mediante el procesamiento de secuencias de video. Se implementa un sistema completo que detecta objetos en movimiento, los identifica como vehículos y los cuenta de manera automática, proporcionando información valiosa para análisis de tráfico y sistemas de transporte inteligente.

## Objetivo

Desarrollar un sistema de análisis de tráfico que pueda identificar y contar automáticamente los vehículos que aparecen en una secuencia de video, utilizando técnicas de procesamiento de imágenes y detección de movimiento para proporcionar conteos precisos y confiables.

## Dataset

El proyecto utiliza una secuencia de video de una carretera (`highway.mp4`) que ha sido dividida en frames individuales almacenados en la carpeta `highway/`. La secuencia contiene 10 frames que muestran vehículos circulando por una carretera. Cada frame tiene dimensiones de 354x630 píxeles en formato RGB.

**Estructura del dataset:**
- `highway/`: Carpeta con frames del video (highway_00001.png a highway_00010.png)
- `highway.mp4`: Video original completo

## Herramientas y Técnicas Empleadas

### Bibliotecas Principales
- **scikit-image**: Procesamiento de imágenes, detección de blobs y operaciones morfológicas
- **NumPy**: Operaciones numéricas y manipulación de arrays
- **Matplotlib**: Visualización de frames y resultados
- **Pandas**: Manejo de datos estructurados (opcional)

### Técnicas de Procesamiento

1. **Conversión a Escala de Grises**
   - Reducción de dimensionalidad para simplificar el procesamiento
   - Conversión de frames RGB a escala de grises

2. **Extracción de Fondo**
   - Cálculo del fondo mediante estadísticos (mediana) de todos los frames
   - Identificación de la escena estática que representa el fondo

3. **Análisis de Diferencias**
   - Comparación de cada frame con el fondo calculado
   - Detección de píxeles que han cambiado (objetos en movimiento)

4. **Binarización**
   - Umbralización adaptativa de Otsu para segmentar objetos en movimiento
   - Conversión a imágenes binarias (0 o 255)

5. **Filtrado Morfológico**
   - Apertura: Eliminación de ruido y pequeños artefactos
   - Cierre: Relleno de huecos pequeños en los objetos
   - Erosión: Separación de objetos cercanos
   - Dilatación: Agrandamiento de regiones detectadas
   - Cierre final: Suavizado de bordes

6. **Análisis de Blobs**
   - Etiquetado de componentes conectados
   - Extracción de propiedades de cada blob (área, centroide, bounding box)
   - Filtrado por área mínima y máxima para eliminar falsos positivos

7. **Filtrado de Blobs**
   - Filtrado por área para eliminar blobs demasiado pequeños o grandes
   - Filtrado por relación de aspecto para mantener formas típicas de vehículos
   - Eliminación de blobs con características atípicas

## Temas Cubiertos

- Procesamiento de secuencias de video
- Detección de movimiento mediante análisis de diferencias
- Extracción de fondo mediante estadísticos temporales
- Segmentación mediante umbralización adaptativa
- Operaciones morfológicas para limpieza de detecciones
- Análisis de componentes conectados (blobs)
- Filtrado de detecciones basado en características geométricas
- Visualización de resultados con bounding boxes

## Ejecución

### Dependencias

```bash
pip install numpy pandas matplotlib scikit-image
```

### Cómo Usar

1. Asegúrate de tener la secuencia de frames en la carpeta `highway/`
2. Abre el notebook `deteccion_conteo_vehiculos.ipynb`
3. Ejecuta las celdas en orden secuencial
4. El notebook procesará cada frame y mostrará los vehículos detectados con bounding boxes

### Estructura de Ejecución

El pipeline sigue estos pasos:
1. Carga de la secuencia de frames
2. Conversión a escala de grises
3. Extracción del fondo mediante mediana
4. Análisis de diferencias con el fondo
5. Binarización mediante umbralización de Otsu
6. Filtrado morfológico (apertura, cierre, erosión, dilatación)
7. Extracción de blobs mediante componentes conectados
8. Filtrado de blobs por área y relación de aspecto
9. Visualización de resultados con conteo

## Resultados Obtenidos

### Detección de Vehículos

- El algoritmo detecta exitosamente vehículos en movimiento en la secuencia de video
- Los blobs detectados se visualizan con bounding boxes rojas
- Se proporciona información detallada de cada blob: área, centroide y bounding box

### Filtrado de Blobs

- El filtrado por área elimina falsos positivos (ruido, sombras)
- El filtrado por relación de aspecto mantiene solo formas típicas de vehículos
- La combinación de filtros mejora significativamente la precisión del conteo

### Conteo de Vehículos

- El sistema cuenta automáticamente los vehículos presentes en cada frame
- Se proporciona información detallada de cada vehículo detectado
- Los resultados se visualizan con bounding boxes y etiquetas

## Insights Clave

1. **Importancia del Fondo**: El cálculo correcto del fondo es crucial para una detección precisa. La mediana es robusta a valores atípicos (vehículos en movimiento) y captura mejor el fondo estático que la media.

2. **Filtrado Morfológico**: Las operaciones morfológicas son esenciales para limpiar las detecciones y eliminar ruido. La secuencia de apertura → cierre → erosión → dilatación → cierre final proporciona resultados óptimos.

3. **Filtrado de Blobs**: El filtrado por área y relación de aspecto es fundamental para eliminar falsos positivos y mantener solo detecciones válidas de vehículos.

4. **Análisis de Diferencias vs Fondo**: Comparar cada frame con el fondo calculado es más efectivo que comparar frames consecutivos, ya que elimina el problema de "fantasmas" y proporciona detecciones más limpias.

## Estructura del Proyecto

```
deteccion_conteo_vehiculos/
├── deteccion_conteo_vehiculos.ipynb    # Notebook principal con el algoritmo completo
├── README.md                            # Este archivo
├── highway/                             # Secuencia de frames del video
│   ├── highway_00001.png
│   ├── highway_00002.png
│   ├── highway_00003.png
│   ├── highway_00004.png
│   ├── highway_00005.png
│   ├── highway_00006.png
│   ├── highway_00007.png
│   ├── highway_00008.png
│   ├── highway_00009.png
│   └── highway_00010.png
└── highway.mp4                          # Video original
```

## Notebook

- **[Detección y Conteo de Vehículos](./deteccion_conteo_vehiculos.ipynb)** - Implementación completa del algoritmo de detección y conteo de vehículos

## Licencia

Este proyecto es parte de un portafolio personal de proyectos de ciencia de datos y visión por computadora.

[Volver a Computer Vision →](../README.md)
