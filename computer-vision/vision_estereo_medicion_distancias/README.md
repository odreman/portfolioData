# Visión Estéreo para Medición de Distancias

Este proyecto implementa un sistema de visión estéreo para calcular distancias en profundidad, incluyendo calibración de cámaras, rectificación de imágenes y cálculo de disparidad.

## Descripción

El proyecto aborda el desafío de medir distancias en profundidad utilizando técnicas de visión estéreo. Se implementa un sistema completo que utiliza dos cámaras calibradas para capturar imágenes de la misma escena desde diferentes perspectivas, calculando la disparidad entre las imágenes y convirtiéndola en distancias reales mediante triangulación.

## Objetivo

Desarrollar un sistema capaz de medir distancias en profundidad utilizando técnicas de visión estéreo, validando el sistema con objetos a distancias conocidas. El sistema debe ser capaz de calcular distancias precisas mediante el análisis de la disparidad entre imágenes estéreo.

## Dataset

El proyecto utiliza un sistema de visión estéreo previamente calibrado. Los parámetros de calibración se encuentran en el archivo `calibrated.npz` e incluyen:

- Parámetros intrínsecos de las cámaras (`mtx_left`, `mtx_right`)
- Coeficientes de distorsión (`dist_left`, `dist_right`)
- Coordenadas del patrón de calibración (`objpoints`, `imgpointsL`, `imgpointsR`)

**Imágenes de validación:**
- `imgs/img_L_test1.jpg` y `imgs/img_R_test1.jpg`: Objeto a 85cm
- `imgs/img_L_test2.jpg` y `imgs/img_R_test2.jpg`: Objeto a 105cm

## Herramientas y Técnicas Empleadas

### Bibliotecas Principales
- **scikit-image**: Procesamiento de imágenes y transformaciones
- **OpenCV**: Calibración estéreo, rectificación y cálculo de disparidad
- **NumPy**: Operaciones numéricas y manipulación de arrays
- **Matplotlib**: Visualización de imágenes estéreo y resultados

### Técnicas de Procesamiento

1. **Calibración Estéreo**
   - Obtención de parámetros intrínsecos y extrínsecos de las cámaras
   - Cálculo de matrices de calibración estéreo
   - Corrección de distorsión de lentes

2. **Rectificación de Imágenes**
   - Alineación de imágenes estéreo
   - Corrección de epipolaridad
   - Transformación a coordenadas rectificadas

3. **Cálculo de Disparidad**
   - Determinación de diferencias entre imágenes izquierda y derecha
   - Algoritmos de matching estéreo (SGBM, BM)
   - Generación de mapas de disparidad

4. **Reconstrucción 3D**
   - Conversión de disparidad a coordenadas 3D
   - Cálculo de distancias en profundidad
   - Triangulación de puntos

5. **Validación del Sistema**
   - Comparación de distancias calculadas con valores reales conocidos
   - Análisis de precisión y error
   - Ajuste de parámetros para optimización

## Temas Cubiertos

- Calibración de cámaras estéreo
- Rectificación de imágenes estéreo
- Cálculo de disparidad
- Reconstrucción 3D mediante triangulación
- Medición de distancias en profundidad
- Validación de sistemas de visión estéreo

## Ejecución

### Dependencias

```bash
pip install numpy pandas matplotlib scikit-image opencv-python
```

### Cómo Usar

1. Asegúrate de tener el archivo `calibrated.npz` con los parámetros de calibración
2. Asegúrate de tener las imágenes de prueba en la carpeta `imgs/`
3. Asegúrate de tener el archivo `util_visionestereo_challenge.py` con funciones auxiliares
4. Abre el notebook `vision_estereo_medicion_distancias.ipynb`
5. Ejecuta las celdas en orden secuencial
6. El notebook calculará las distancias y las comparará con los valores conocidos

### Estructura de Ejecución

El pipeline sigue estos pasos:
1. Carga de parámetros de calibración
2. Carga de imágenes estéreo de prueba
3. Rectificación de imágenes
4. Cálculo de disparidad
5. Conversión de disparidad a distancias
6. Validación con distancias conocidas
7. Visualización de resultados

## Resultados Obtenidos

### Medición de Distancias

- El sistema calcula exitosamente las distancias en profundidad
- Las distancias calculadas se comparan con valores reales conocidos
- El sistema proporciona mediciones precisas dentro de un margen de error aceptable

### Validación del Sistema

- **Test 1 (85cm)**: El sistema calcula una distancia cercana al valor real
- **Test 2 (105cm)**: El sistema calcula una distancia cercana al valor real
- La precisión del sistema se valida mediante comparación con distancias conocidas

## Insights Clave

1. **Importancia de la Calibración**: Una calibración precisa es fundamental para obtener mediciones correctas. Los errores en la calibración se propagan directamente a las mediciones de distancia.

2. **Rectificación de Imágenes**: La rectificación correcta de las imágenes estéreo es esencial para facilitar el matching y mejorar la precisión del cálculo de disparidad.

3. **Cálculo de Disparidad**: La calidad del mapa de disparidad determina directamente la precisión de las mediciones. Algoritmos más sofisticados (SGBM) proporcionan mejores resultados que métodos básicos.

4. **Validación del Sistema**: La validación con objetos a distancias conocidas es crucial para verificar la precisión del sistema y ajustar parámetros si es necesario.

## Estructura del Proyecto

```
vision_estereo_medicion_distancias/
├── vision_estereo_medicion_distancias.ipynb    # Notebook principal con el sistema completo
├── README.md                                     # Este archivo
├── calibrated.npz                                # Parámetros de calibración estéreo
├── imgs/                                         # Imágenes estéreo de prueba
│   ├── img_L_test1.jpg
│   ├── img_R_test1.jpg
│   ├── img_L_test2.jpg
│   └── img_R_test2.jpg
└── util_visionestereo_challenge.py              # Funciones auxiliares
```

## Notebook

- **[Visión Estéreo para Medición de Distancias](./vision_estereo_medicion_distancias.ipynb)** - Implementación completa del sistema de visión estéreo

## Licencia

Este proyecto es parte de un portafolio personal de proyectos de ciencia de datos y visión por computadora.

[Volver a Computer Vision →](../README.md)
