# Procesamiento de Imágenes Nocturnas

Este proyecto implementa técnicas de mejora y preprocesamiento de imágenes capturadas en condiciones de baja iluminación, aplicando ajustes de histograma, ecualización adaptativa y filtrado para mejorar la visibilidad y calidad de las imágenes obtenidas por cámaras de seguridad nocturnas.

## Descripción

El proyecto aborda el desafío de procesar imágenes capturadas en condiciones de baja iluminación, donde la visibilidad es limitada y los detalles son difíciles de apreciar. Se implementan diversas técnicas de procesamiento de imágenes para mejorar el contraste, reducir el ruido y detectar bordes de manera efectiva.

## Objetivo

Desarrollar un pipeline completo de procesamiento de imágenes nocturnas que mejore significativamente la visibilidad y permita la detección precisa de bordes y características en condiciones de baja iluminación.

## Dataset

El proyecto utiliza una imagen de prueba capturada por una cámara de seguridad nocturna (`img/1.jpg`). La imagen tiene dimensiones de 2848x4256 píxeles en formato RGB y presenta características típicas de imágenes nocturnas: baja luminosidad general, concentración de valores de intensidad en el rango bajo del histograma, y dificultad para apreciar detalles sin procesamiento.

## Herramientas y Técnicas Empleadas

### Bibliotecas Principales
- **scikit-image**: Procesamiento de imágenes, filtros y transformaciones
- **NumPy**: Operaciones numéricas y manipulación de arrays
- **Matplotlib**: Visualización de imágenes y histogramas
- **imageio**: Carga de imágenes

### Técnicas de Procesamiento

1. **Análisis de Histogramas**
   - Evaluación de la distribución de intensidades de píxeles
   - Identificación de características de iluminación

2. **Ecualización de Histograma**
   - **Ecualización Global**: Redistribución uniforme de intensidades en toda la imagen
   - **Ecualización Adaptativa**: Redistribución local de intensidades utilizando elementos estructurantes

3. **Reducción de Ruido**
   - Filtro Gaussiano para suavizado y eliminación de ruido

4. **Segmentación**
   - Umbralización adaptativa de Otsu para binarización

5. **Detección de Bordes**
   - Operador de Sobel para detección básica de bordes
   - Operador de Canny para detección robusta con supresión de no-máximos

6. **Operaciones Morfológicas**
   - Dilatación binaria para mejora de bordes detectados

## Temas Cubiertos

- Procesamiento de imágenes en condiciones de baja iluminación
- Análisis y mejora de histogramas
- Técnicas de ecualización (global vs adaptativa)
- Filtrado espacial y reducción de ruido
- Segmentación mediante umbralización
- Detección de bordes con múltiples operadores
- Pipeline completo de procesamiento de imágenes
- Comparación de técnicas de mejora de contraste

## Ejecución

### Dependencias

```bash
pip install numpy pandas matplotlib scikit-image imageio
```

### Cómo Usar

1. Asegúrate de tener la imagen de prueba en la carpeta `img/1.jpg`
2. Abre el notebook `procesamiento_imagenes_nocturnas.ipynb`
3. Ejecuta las celdas en orden secuencial
4. El notebook procesará la imagen y mostrará los resultados de cada etapa

### Estructura de Ejecución

El pipeline sigue estos pasos:
1. Carga de la imagen original
2. Análisis de dimensiones y espacio de color
3. Visualización inicial
4. Análisis de histograma original
5. Ecualización de histograma (global y adaptativa)
6. Comparación de técnicas de ecualización
7. Detección de bordes con Sobel
8. Optimización con Canny y filtro Gaussiano
9. Pipeline completo integrado

## Resultados Obtenidos

### Mejoras de Contraste

- **Imagen Original**: Media de intensidad de 0.02 (muy oscura)
- **Imagen Ecualizada**: Media de intensidad de 193.12 (mejora significativa)
- **Distribución**: El histograma se redistribuye de manera más uniforme, expandiendo el rango de valores desde 0 hasta 255

### Comparación de Técnicas

- **Ecualización Global**: Proporciona mejores resultados en este caso específico, mejorando el contraste general de manera más efectiva
- **Ecualización Adaptativa**: Útil para ajustes locales, pero en este caso la global fue superior

### Detección de Bordes

- El operador de Canny con preprocesamiento Gaussiano proporciona detección de bordes más robusta y precisa que Sobel
- Las operaciones morfológicas de dilatación mejoran la continuidad de los bordes detectados

## Insights Clave

1. **Ecualización Global vs Adaptativa**: Aunque la ecualización adaptativa suele ser preferida para imágenes con variaciones locales de iluminación, en imágenes nocturnas muy oscuras la ecualización global puede proporcionar mejores resultados al mejorar el contraste general de manera más uniforme.

2. **Importancia del Preprocesamiento**: La reducción de ruido mediante filtro Gaussiano antes de la detección de bordes es crucial para obtener resultados precisos en imágenes nocturnas.

3. **Pipeline Secuencial**: La combinación ordenada de técnicas (ecualización → reducción de ruido → segmentación → detección de bordes → mejora morfológica) es más efectiva que aplicar técnicas de forma aislada.

4. **Análisis de Histograma**: El análisis del histograma es fundamental para entender las características de la imagen y seleccionar las técnicas de mejora más apropiadas.

## Estructura del Proyecto

```
procesamiento_imagenes_nocturnas/
├── procesamiento_imagenes_nocturnas.ipynb    # Notebook principal con el pipeline completo
├── README.md                                   # Este archivo
└── img/                                       # Carpeta con imágenes de entrada
    └── 1.jpg                                  # Imagen de prueba nocturna
```

## Notebook

- **[Procesamiento de Imágenes Nocturnas](./procesamiento_imagenes_nocturnas.ipynb)** - Implementación completa del pipeline de procesamiento de imágenes nocturnas

## Licencia

Este proyecto es parte de un portafolio personal de proyectos de ciencia de datos y visión por computadora.

[Volver a Computer Vision →](../README.md)
