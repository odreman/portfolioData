# Clustering para Plan de Expansión de Tiendas

[← Volver al índice](../README.md) | [📓 Ver Notebook](./clustering_store_expansion.ipynb)

## Descripción

Este proyecto aplica técnicas de clustering para identificar áreas óptimas para la apertura de nuevos centros comerciales utilizando información censal. El objetivo es segmentar regiones según perfiles de clientes que se adapten a diferentes tipologías de establecimientos (boutiques, supermercados de presupuesto medio, grandes superficies, etc.).

## Objetivo

El objetivo principal es:
- Identificar áreas geográficas con perfiles de clientes similares mediante clustering
- Segmentar regiones según características demográficas y socioeconómicas
- Proporcionar insights para la toma de decisiones sobre ubicación de nuevos establecimientos
- Adaptar la tipología de tienda al perfil de cada región identificada

## Dataset

- **Archivo**: `census2000.csv`
- **Descripción**: Información censal de diferentes zonas geográficas
- **Variables** (8 en total):
  - `Numrow`: Número de fila
  - `ID`: Identificador del registro
  - `LocX`: Coordenada X para geolocalización
  - `LocY`: Coordenada Y para geolocalización
  - `RegDens`: Densidad de población de la región
  - `RegPop`: Número de habitantes de la región
  - `MedHHInc`: Nivel de ingresos medio de la unidad familiar
  - `MeanHHSz`: Tamaño medio de la unidad familiar (Household)
- **Registros**: 33,178 registros iniciales (filtrados según criterios)

## Herramientas y Técnicas Empleadas

### Librerías de Python
- **pandas**: Manipulación y análisis de datos
- **numpy**: Operaciones numéricas
- **matplotlib**: Visualización de datos
- **seaborn**: Visualizaciones estadísticas avanzadas
- **scikit-learn**: Algoritmos de clustering (K-Means, DBSCAN, etc.)
- **folium**: Visualización geográfica interactiva

### Técnicas Implementadas

1. **Clustering**
   - K-Means para segmentación de regiones
   - Determinación del número óptimo de clusters
   - Análisis de perfiles de cada cluster

2. **Preprocesamiento de Datos**
   - Filtrado de registros (unidades familiares >= 2)
   - Estandarización de variables
   - Manejo de valores faltantes

3. **Análisis Exploratorio**
   - Visualización de distribución geográfica
   - Análisis de correlaciones entre variables
   - Histogramas y gráficos de dispersión

4. **Visualización Geográfica**
   - Mapas interactivos con Folium
   - Marcado de clusters en mapas
   - Análisis de distribución espacial

## Temas Cubiertos

- **Clustering no supervisado**: Segmentación de regiones geográficas
- **Análisis demográfico**: Uso de datos censales para análisis de mercado
- **Visualización geográfica**: Representación de clusters en mapas
- **Análisis de mercado**: Identificación de oportunidades de expansión
- **Segmentación de clientes**: Agrupación según características socioeconómicas

## Ejecución

### Requisitos Previos

1. Python 3.7 o superior
2. Jupyter Notebook o JupyterLab
3. Instalación de dependencias (ver sección Dependencias)

### Pasos para Ejecutar

1. Clonar o descargar el repositorio
2. Navegar al directorio del proyecto:
   ```bash
   cd clustering_store_expansion
   ```

3. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Abrir el notebook:
   ```bash
   jupyter notebook clustering_store_expansion.ipynb
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
folium>=0.12.0
jupyter>=1.0.0
```

### Instalación de Dependencias

```bash
pip install pandas numpy matplotlib seaborn scikit-learn folium jupyter
```

## Cómo Usar

### Carga y Preprocesamiento

1. Cargar el dataset `census2000.csv`
2. Inspeccionar la estructura y tipos de datos
3. Filtrar registros con unidades familiares >= 2
4. Manejar valores faltantes si es necesario

### Análisis Exploratorio

1. Visualizar distribución geográfica de las zonas
2. Analizar distribuciones de variables clave (ingresos, densidad, población)
3. Identificar correlaciones entre variables
4. Generar visualizaciones descriptivas

### Aplicación de Clustering

1. Seleccionar variables relevantes para clustering
2. Estandarizar variables numéricas
3. Determinar número óptimo de clusters (método del codo, silhouette score)
4. Aplicar algoritmo de clustering (K-Means)
5. Analizar perfiles de cada cluster

### Visualización y Análisis

1. Visualizar clusters en mapas geográficos
2. Analizar características de cada cluster
3. Identificar áreas óptimas para diferentes tipologías de tiendas
4. Generar recomendaciones basadas en perfiles de clusters

## Resultados Obtenidos

### Segmentación de Regiones

- **Clusters identificados**: Se identifican diferentes grupos de regiones con características similares
- **Perfiles de clusters**: Cada cluster representa un perfil demográfico y socioeconómico distinto
- **Distribución geográfica**: Los clusters muestran patrones espaciales que pueden indicar áreas de oportunidad

### Características de los Clusters

Cada cluster se caracteriza por:
- Nivel de ingresos medio
- Densidad de población
- Tamaño de unidades familiares
- Ubicación geográfica

### Recomendaciones de Expansión

- **Boutiques**: Áreas con alto nivel de ingresos y baja densidad
- **Supermercados de presupuesto medio**: Áreas con ingresos medios y densidad moderada
- **Grandes superficies**: Áreas con alta densidad de población y tamaño de familia grande

## Insights Clave

1. **Segmentación efectiva**: El clustering permite identificar claramente diferentes perfiles de mercado que requieren diferentes estrategias comerciales.

2. **Patrones geográficos**: Los clusters muestran patrones espaciales que pueden indicar áreas de oportunidad o competencia.

3. **Adaptación de estrategia**: Diferentes tipologías de tiendas pueden ser más adecuadas para diferentes clusters, permitiendo una estrategia de expansión más precisa.

4. **Análisis demográfico**: Las variables censales proporcionan información valiosa sobre el potencial de mercado de cada región.

5. **Visualización geográfica**: Los mapas interactivos facilitan la comprensión de la distribución espacial de los clusters y la toma de decisiones.

## Estructura de Carpeta

```
clustering_store_expansion/
│
├── clustering_store_expansion.ipynb  # Notebook principal
├── census2000.csv                    # Dataset censal
├── correlacion.png                   # Visualización de correlaciones
├── dendrograma.png                   # Dendrograma (si se usa clustering jerárquico)
├── logaritmo.png                     # Visualización adicional
├── tienda.jpg                        # Imagen ilustrativa
├── README.md                         # Este archivo
└── requirements.txt                  # Dependencias
```

## Enlaces

- **📓 Notebook Principal**: [clustering_store_expansion.ipynb](./clustering_store_expansion.ipynb)
- **Dataset**: [census2000.csv](./census2000.csv)
- **Documentación scikit-learn**: [https://scikit-learn.org/stable/](https://scikit-learn.org/stable/)
- **Documentación Folium**: [https://python-visualization.github.io/folium/](https://python-visualization.github.io/folium/)

## Licencia

Este proyecto es de código abierto y está disponible para uso educativo y de investigación.

---

**Nota**: Este proyecto demuestra la aplicación práctica de técnicas de clustering para análisis de mercado y toma de decisiones estratégicas en retail, proporcionando una metodología para identificar oportunidades de expansión basada en datos demográficos.

