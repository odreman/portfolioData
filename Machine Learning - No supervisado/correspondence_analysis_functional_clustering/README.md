# Análisis de Correspondencias y Clustering Funcional

[← Volver al índice](../README.md) | [📓 Ver Notebook](./correspondence_analysis_functional_clustering.ipynb)

## Descripción

Este proyecto presenta dos técnicas avanzadas de aprendizaje no supervisado aplicadas a diferentes tipos de datos:

1. **Análisis de Correspondencias (CA)**: Técnica de reducción de dimensionalidad para datos categóricos que permite visualizar las relaciones entre categorías de dos variables nominales en un espacio de pocas dimensiones.

2. **Clustering Funcional (FDA)**: Técnica de agrupación para datos funcionales que considera la forma completa de las curvas en lugar de valores puntuales, ideal para series temporales.

## Objetivo

El objetivo principal es demostrar cómo estas técnicas pueden extraer insights valiosos de diferentes tipos de datos:

- **Análisis de Correspondencias**: Identificar relaciones entre marcas de productos y atributos percibidos por consumidores, permitiendo estrategias de posicionamiento y análisis de competencia.

- **Clustering Funcional**: Agrupar estaciones meteorológicas según patrones de temperatura anual, identificando regiones climáticas similares basándose en la evolución temporal completa.

## Dataset

### Parte 1: Percepción de Marcas de Café
- **Archivo**: `coffe.csv`
- **Descripción**: Tabla de frecuencias que relaciona 6 marcas de café refrigerado (AA, BB, CC, DD, EE, FF) con 23 atributos percibidos por consumidores
- **Estructura**: 135 filas con columnas `image` (atributo), `brand` (marca), `freq` (frecuencia de asociación)
- **Atributos**: Incluyen características como "healthy", "premium", "traditional", "men", "women", "low fat", "caffeine", entre otros

### Parte 2: Datos Meteorológicos
- **Fuente**: Dataset `fetch_aemet` de scikit-fda
- **Descripción**: Datos diarios de 73 estaciones meteorológicas españolas para el periodo 1980-2009
- **Contenido**: Información geográfica de cada estación y media de temperatura diaria
- **Origen**: AEMET (Agencia Estatal de Meteorología) - [Más información](http://www.aemet.es/)

## Herramientas y Técnicas Empleadas

### Librerías de Python
- **pandas**: Manipulación y análisis de datos
- **numpy**: Operaciones numéricas
- **matplotlib**: Visualización de datos
- **seaborn**: Visualizaciones estadísticas avanzadas
- **prince**: Análisis de correspondencias
- **scikit-fda**: Análisis de datos funcionales y clustering funcional

### Técnicas Implementadas

1. **Análisis de Correspondencias (CA)**
   - Reducción de dimensionalidad para datos categóricos
   - Visualización de relaciones marca-atributo
   - Evaluación de inercia explicada
   - Interpretación de mapas de posicionamiento

2. **Clustering Funcional**
   - K-Means funcional para series temporales
   - Representación de datos funcionales (FDataGrid)
   - Agrupación basada en similitud de curvas completas

3. **Análisis Exploratorio de Datos (EDA)**
   - Exploración de estructura de datos
   - Análisis estadístico descriptivo
   - Visualización de distribuciones
   - Creación de tablas de contingencia
   - Heatmaps y gráficos de dispersión

## Temas Cubiertos

- **Análisis de Correspondencias**: Fundamentos teóricos, aplicación práctica, interpretación de resultados
- **Datos Funcionales**: Conceptos de Functional Data Analysis (FDA)
- **Clustering Funcional**: K-Means aplicado a curvas y series temporales
- **Visualización de Datos**: Mapas de correspondencias, gráficos de curvas temporales
- **Análisis de Posicionamiento de Marcas**: Estrategias de marketing basadas en percepción del consumidor
- **Análisis Climático**: Identificación de patrones regionales en datos meteorológicos

## Ejecución

### Requisitos Previos

1. Python 3.7 o superior
2. Jupyter Notebook o JupyterLab
3. Instalación de dependencias (ver sección Dependencias)

### Pasos para Ejecutar

1. Clonar o descargar el repositorio
2. Navegar al directorio del proyecto:
   ```bash
   cd correspondence_analysis_functional_clustering
   ```

3. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Abrir el notebook:
   ```bash
   jupyter notebook correspondence_analysis_functional_clustering.ipynb
   ```

5. Ejecutar las celdas en orden secuencial

## Dependencias

Las siguientes librerías son necesarias para ejecutar el proyecto:

```
pandas>=1.3.0
numpy>=1.21.0
matplotlib>=3.4.0
seaborn>=0.11.0
prince>=0.7.0
scikit-fda>=0.9.0
jupyter>=1.0.0
```

### Instalación de Dependencias

```bash
pip install pandas numpy matplotlib seaborn prince scikit-fda jupyter
```

**Nota**: El dataset de AEMET se descarga automáticamente al ejecutar `datasets.fetch_aemet()` en el notebook.

## Cómo Usar

### Análisis de Correspondencias

1. Cargar el dataset `coffe.csv`
2. Realizar exploración de datos
3. Crear tabla de contingencia
4. Aplicar análisis de correspondencias con 2 componentes
5. Visualizar mapa de correspondencias
6. Interpretar resultados y caracterizar marcas

### Clustering Funcional

1. Cargar dataset de AEMET usando `datasets.fetch_aemet()`
2. Seleccionar curvas representativas
3. Visualizar curvas de temperatura
4. Aplicar K-Means funcional
5. Interpretar clusters identificados

## Resultados Obtenidos

### Análisis de Correspondencias

- **Inercia explicada**: 82.7% (Dimensión 1: 62.9%, Dimensión 2: 19.8%)
- **Marcas analizadas**: 6 marcas con perfiles distintivos
- **Atributos identificados**: 23 atributos de percepción
- **Insights clave**:
  - Marcas CC y DD compiten directamente en el segmento saludable/moderno
  - Oportunidad de mercado en posicionamiento premium/atractivo
  - Perfiles claramente diferenciados por marca

### Clustering Funcional

- **Clusters identificados**: 2 grupos principales
- **Cluster 0**: Estaciones con temperaturas más bajas (probablemente norte de España)
- **Cluster 1**: Estaciones con temperaturas más altas (probablemente sur de España)
- **Validación**: Resultados coherentes con la realidad climática española

## Insights Clave

1. **Análisis de Correspondencias**:
   - El análisis revela oportunidades de posicionamiento estratégico para nuevas marcas
   - La proximidad en el mapa indica competencia directa entre marcas similares
   - El 82.7% de inercia explicada valida la calidad de la representación reducida

2. **Clustering Funcional**:
   - El clustering funcional captura patrones que no serían evidentes con análisis puntuales
   - La consideración de la forma completa de las curvas permite identificar regiones climáticas
   - La técnica es efectiva para datos de series temporales con estructura funcional

3. **Aplicaciones Prácticas**:
   - Segmentación de mercado basada en percepción del consumidor
   - Identificación de patrones regionales en datos meteorológicos
   - Estrategias de diferenciación de productos
   - Análisis de competencia en espacios de atributos

## Estructura de Carpeta

```
correspondence_analysis_functional_clustering/
│
├── correspondence_analysis_functional_clustering.ipynb  # Notebook principal
├── coffe.csv                                            # Dataset de marcas de café
├── README.md                                            # Este archivo
└── newlogomioti.png                                    # Imagen (no utilizada en análisis)
```

## Enlaces

- **📓 Notebook Principal**: [correspondence_analysis_functional_clustering.ipynb](./correspondence_analysis_functional_clustering.ipynb)
- **Dataset de café**: [coffe.csv](./coffe.csv)
- **Dataset AEMET**: Se descarga automáticamente desde scikit-fda al ejecutar el notebook
- **Documentación scikit-fda**: [https://fda.readthedocs.io/](https://fda.readthedocs.io/)
- **Documentación prince (CA)**: [https://github.com/MaxHalford/prince](https://github.com/MaxHalford/prince)

## Licencia

Este proyecto es de código abierto y está disponible para uso educativo y de investigación.

---

**Nota**: Este proyecto demuestra técnicas avanzadas de aprendizaje no supervisado aplicadas a casos de uso reales, mostrando tanto el análisis de datos categóricos como funcionales.

