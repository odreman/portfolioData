# Clustering de Cereales con K-Means

[← Volver al índice](../README.md) | [📓 Ver Notebook](./cereal_clustering_kmeans.ipynb)

## Descripción

Este proyecto aplica técnicas de clustering mediante el algoritmo K-Means para agrupar cereales según su perfil nutricional. El análisis permite identificar segmentos de mercado y desarrollar estrategias de posicionamiento para diferentes tipos de consumidores basándose en características nutricionales clave.

## Objetivo

El objetivo principal es agrupar distintos tipos de cereales según su información nutricional para identificar:
- Perfiles nutricionales distintos en el mercado
- Segmentos de consumidores potenciales para cada tipo de cereal
- Estrategias de posicionamiento para fabricantes
- Relación entre características nutricionales y percepción del consumidor (rating)

## Dataset

- **Archivo**: `cereal.csv`
- **Descripción**: Base de datos con información nutricional de 77 cereales distintos
- **Variables** (16 en total):
  - `Name`: Nombre del cereal
  - `Mfr`: Fabricante (A, G, K, N, P, Q, R)
  - `Type`: Tipo (C=Cold, H=Hot)
  - `calories`: Calorías por porción
  - `protein`: Gramos de proteínas
  - `fat`: Gramos de grasa
  - `sodium`: Miligramos de sodio
  - `fiber`: Gramos de fibra dietética
  - `carbo`: Gramos de carbohidratos
  - `sugars`: Gramos de azúcares
  - `potass`: Miligramos de potasio
  - `vitamins`: Porcentaje de vitaminas y minerales (25 o 100)
  - `shelf`: Estante de demostración (1, 2 o 3)
  - `weight`: Peso en onzas de una porción
  - `cups`: Número de tazas en una porción
  - `rating`: Calificación de los consumidores

## Herramientas y Técnicas Empleadas

### Librerías de Python
- **pandas**: Manipulación y análisis de datos
- **numpy**: Operaciones numéricas y arrays
- **matplotlib**: Visualización de datos (2D y 3D)
- **seaborn**: Visualizaciones estadísticas avanzadas
- **scikit-learn**: Algoritmo K-Means y métricas

### Técnicas Implementadas

1. **K-Means Clustering**
   - Determinación del número óptimo de clusters (método del codo)
   - Clustering con 3 grupos
   - Análisis de centroides y etiquetas

2. **Análisis Exploratorio de Datos (EDA)**
   - Exploración de variables nutricionales
   - Selección de variables clave (calorías, azúcares, grasas)
   - Análisis extendido con variables adicionales (fibra, proteína, rating)

3. **Visualización**
   - Gráficos 3D de clusters
   - Visualizaciones bidimensionales (proyecciones)
   - Análisis de correlaciones
   - Boxplots y scatter plots

## Temas Cubiertos

- **Clustering no supervisado**: Fundamentos y aplicación práctica de K-Means
- **Selección de variables**: Identificación de características más discriminativas
- **Evaluación de clusters**: Método del codo y análisis de separación
- **Análisis nutricional**: Segmentación de productos alimenticios
- **Relación con rating**: Impacto de características nutricionales en percepción del consumidor
- **Visualización multidimensional**: Representación de datos en 2D y 3D

## Ejecución

### Requisitos Previos

1. Python 3.7 o superior
2. Jupyter Notebook o JupyterLab
3. Instalación de dependencias (ver sección Dependencias)

### Pasos para Ejecutar

1. Clonar o descargar el repositorio
2. Navegar al directorio del proyecto:
   ```bash
   cd cereal_clustering_kmeans
   ```

3. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Abrir el notebook:
   ```bash
   jupyter notebook cereal_clustering_kmeans.ipynb
   ```

5. Ejecutar las celdas en orden secuencial

## Dependencias

Las siguientes librerías son necesarias para ejecutar el proyecto:

```
pandas>=1.3.0
numpy>=1.21.0
matplotlib>=3.4.0
seaborn>=0.11.0
scikit-learn>=1.0.0
jupyter>=1.0.0
```

### Instalación de Dependencias

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

## Cómo Usar

### Análisis Básico con 3 Variables

1. Cargar el dataset `cereal.csv`
2. Seleccionar variables clave: calorías, azúcares, grasas
3. Aplicar método del codo para validar número de clusters
4. Ejecutar K-Means con 3 clusters
5. Visualizar resultados en 3D y proyecciones 2D
6. Interpretar perfiles nutricionales

### Análisis Extendido

1. Incorporar variables adicionales: fibra, proteína, rating
2. Re-ejecutar clustering con variables extendidas
3. Analizar correlaciones entre variables
4. Evaluar relación entre características nutricionales y rating
5. Identificar perfil del cereal exitoso

## Resultados Obtenidos

### Clustering con 3 Variables (Calorías, Azúcares, Grasas)

**3 Clusters identificados:**

1. **Cluster "Sabrosos"** (18 cereales, 23.4%):
   - Alto en calorías (130), azúcares (10.2g) y grasas (2g)
   - Orientados al sabor

2. **Cluster "Nutritivos"** (6 cereales, 7.8%):
   - Bajo en calorías (61.7), azúcares (1.8g) y grasas (0.3g)
   - Enfocados en salud

3. **Cluster "Balanceados"** (53 cereales, 68.8%):
   - Valores intermedios (104.2 cal, 6.4g azúcares, 0.8g grasas)
   - Perfil equilibrado

### Clustering Extendido (6 Variables)

**Cambios en la distribución:**

- **Cluster "Sabrosos"**: Aumentó a 41 cereales (53.2%)
- **Cluster "Nutritivos"**: Se mantiene en 6 cereales (7.8%)
- **Cluster "Balanceados"**: Disminuyó a 30 cereales (39.0%)

**Hallazgos clave:**
- Los cereales nutritivos obtienen el mejor rating (68.9)
- Los cereales sabrosos tienen el rating más bajo (33.0)
- La fibra es el nutriente más valorado por los consumidores
- Los azúcares tienen impacto negativo en el rating

## Insights Clave

1. **Segmentación del mercado:**
   - El mercado está dominado por cereales balanceados (68.8% en análisis básico)
   - Existe un nicho especializado de cereales nutritivos (7.8%)
   - Los cereales sabrosos representan un segmento significativo (23.4%)

2. **Variables más discriminativas:**
   - Calorías y grasas proporcionan la mejor separación entre clusters
   - La combinación Calorías vs Grasas muestra la mejor diferenciación visual

3. **Relación con rating:**
   - Los cereales nutritivos (alto en fibra, bajo en azúcares) obtienen mejores ratings
   - La fibra es el nutriente más valorado por los consumidores
   - Los azúcares tienen impacto negativo en la percepción del consumidor

4. **Perfil del cereal exitoso:**
   - Alto contenido de fibra
   - Bajo contenido de azúcares
   - Calorías moderadas
   - Proteína adecuada

5. **Aplicaciones prácticas:**
   - Desarrollo de nuevos productos basados en perfiles exitosos
   - Estrategias de posicionamiento para diferentes segmentos
   - Segmentación de clientes por preferencias nutricionales
   - Identificación de gaps en el mercado

## Estructura de Carpeta

```
cereal_clustering_kmeans/
│
├── cereal_clustering_kmeans.ipynb  # Notebook principal
├── cereal.csv                      # Dataset de cereales
├── README.md                       # Este archivo
└── requirements.txt                # Dependencias
```

## Enlaces

- **📓 Notebook Principal**: [cereal_clustering_kmeans.ipynb](./cereal_clustering_kmeans.ipynb)
- **Dataset**: [cereal.csv](./cereal.csv)
- **Documentación scikit-learn**: [https://scikit-learn.org/stable/](https://scikit-learn.org/stable/)

## Licencia

Este proyecto es de código abierto y está disponible para uso educativo y de investigación.

---

**Nota**: Este proyecto demuestra la aplicación práctica de técnicas de clustering no supervisado para análisis de mercado y desarrollo de productos en la industria alimentaria.

