# Pegado de Imágenes y Panorama

Este proyecto implementa técnicas de alineación y fusión de múltiples imágenes parcialmente superpuestas para generar una imagen panorámica completa, utilizando detección de características, matching de descriptores y transformaciones geométricas.

## Descripción

El proyecto aborda el desafío de combinar múltiples imágenes de una escena para crear una vista panorámica completa. Se implementa un sistema completo que detecta características comunes entre imágenes, las alinea mediante transformaciones geométricas y las fusiona de manera natural, resolviendo un caso práctico de análisis forense mediante técnicas de visión por computadora.

## Objetivo

Desarrollar un sistema capaz de combinar múltiples imágenes parcialmente superpuestas para generar una imagen panorámica completa. El objetivo es resolver un caso práctico de análisis forense mediante técnicas de visión por computadora, combinando imágenes de una escena del crimen para revelar información oculta que no es visible en las imágenes individuales.

## Dataset

El proyecto utiliza imágenes de una escena del crimen almacenadas en la carpeta `imgs/`. El dataset contiene 2 imágenes que muestran diferentes partes de un escritorio, con áreas de superposición que permiten su alineación y fusión.

**Estructura del dataset:**
- `imgs/`: Carpeta con imágenes de la escena (formato JPG)

## Herramientas y Técnicas Empleadas

### Bibliotecas Principales
- **scikit-image**: Procesamiento de imágenes, detección de características y transformaciones
- **NumPy**: Operaciones numéricas y manipulación de arrays
- **Matplotlib**: Visualización de imágenes y resultados
- **ipywidgets**: Interfaz interactiva para ajuste de parámetros

### Técnicas de Procesamiento

1. **Detección de Características**
   - Uso de ORB (Oriented FAST and Rotated BRIEF) para encontrar puntos clave
   - Detección de esquinas y características distintivas en cada imagen

2. **Matching de Descriptores**
   - Emparejamiento de características entre imágenes
   - Identificación de correspondencias entre puntos clave

3. **Estimación de Transformación**
   - Cálculo de homografía entre imágenes
   - Uso de RANSAC para filtrar correspondencias incorrectas
   - Aplicación de transformaciones proyectivas, afines o euclidianas

4. **Alineación de Imágenes**
   - Transformación de imágenes para alinearlas
   - Corrección de perspectiva y rotación

5. **Fusión de Imágenes**
   - Técnicas de blending para combinar imágenes
   - Eliminación de costuras visibles
   - Mezcla suave en áreas de superposición

## Temas Cubiertos

- Detección de características (ORB, FAST, BRIEF)
- Matching de descriptores
- Estimación de homografía
- Algoritmo RANSAC para filtrado robusto
- Transformaciones geométricas (proyectivas, afines, euclidianas)
- Fusión y blending de imágenes
- Creación de panoramas

## Ejecución

### Dependencias

```bash
pip install numpy pandas matplotlib scikit-image ipywidgets
```

### Cómo Usar

1. Asegúrate de tener las imágenes en la carpeta `imgs/`
2. Asegúrate de tener el archivo `utils.py` con las funciones auxiliares
3. Abre el notebook `pegado_imagenes_panorama.ipynb`
4. Ejecuta las celdas en orden secuencial
5. El notebook procesará las imágenes y generará el panorama combinado

### Estructura de Ejecución

El pipeline sigue estos pasos:
1. Carga de las imágenes de entrada
2. Detección de características en cada imagen (ORB)
3. Matching de descriptores entre imágenes
4. Filtrado de correspondencias con RANSAC
5. Estimación de homografía
6. Transformación y alineación de imágenes
7. Fusión de imágenes mediante blending
8. Visualización del panorama resultante

## Resultados Obtenidos

### Creación de Panorama

- El sistema detecta exitosamente características comunes entre las imágenes
- Las imágenes se alinean correctamente mediante transformaciones geométricas
- El panorama resultante revela información completa de la escena

### Precisión del Sistema

- El algoritmo RANSAC filtra efectivamente las correspondencias incorrectas
- La homografía calculada proporciona una alineación precisa
- El blending elimina costuras visibles en el panorama final

## Insights Clave

1. **Importancia del Matching**: La calidad del matching de descriptores es crucial para una alineación precisa. Un buen matching reduce significativamente los errores en la estimación de la transformación.

2. **RANSAC para Robustez**: El algoritmo RANSAC es esencial para filtrar correspondencias incorrectas (outliers) y obtener una estimación robusta de la transformación.

3. **Fusión de Imágenes**: Las técnicas de blending son fundamentales para crear panoramas naturales sin costuras visibles. La mezcla suave en áreas de superposición mejora significativamente la calidad visual.

4. **Detección de Características**: ORB proporciona un buen equilibrio entre velocidad y precisión para este tipo de aplicación, siendo adecuado para imágenes con suficiente textura.

## Estructura del Proyecto

```
pegado_imagenes_panorama/
├── pegado_imagenes_panorama.ipynb    # Notebook principal con el algoritmo completo
├── README.md                           # Este archivo
├── imgs/                               # Imágenes de entrada
│   ├── img1.jpg
│   └── img2.jpg
└── utils.py                            # Funciones auxiliares (si está presente)
```

## Notebook

- **[Pegado de Imágenes y Panorama](./pegado_imagenes_panorama.ipynb)** - Implementación completa de las técnicas de pegado de imágenes y creación de panoramas

## Licencia

Este proyecto es parte de un portafolio personal de proyectos de ciencia de datos y visión por computadora.

[Volver a Computer Vision →](../README.md)
