# Machine Learning - No Supervisado

Portafolio de proyectos de Machine Learning No Supervisado que demuestra la aplicación práctica de diversas técnicas de aprendizaje no supervisado para análisis de datos, segmentación, reducción de dimensionalidad y descubrimiento de patrones.

## 📚 Descripción General

Este repositorio contiene una colección de proyectos que abordan diferentes problemas utilizando técnicas de aprendizaje no supervisado. Cada proyecto incluye un análisis completo desde la exploración de datos hasta la interpretación de resultados, con documentación detallada y código reproducible.

## 🎯 Proyectos Incluidos

### 1. [Análisis de Correspondencias y Clustering Funcional](./correspondence_analysis_functional_clustering/)
**Técnicas**: Análisis de Correspondencias (CA), Análisis de Datos Funcionales (FDA), K-Means Funcional

Aplicación de análisis de correspondencias para estudiar la percepción de marcas de café y clustering funcional para análisis de datos de temperatura en España.

- 📓 [Notebook](./correspondence_analysis_functional_clustering/correspondence_analysis_functional_clustering.ipynb)
- 📖 [README](./correspondence_analysis_functional_clustering/README.md)

---

### 2. [Clustering de Cereales con K-Means](./cereal_clustering_kmeans/)
**Técnicas**: K-Means Clustering, Análisis de Segmentación

Análisis de clustering aplicado a datos nutricionales de cereales para identificar grupos de productos con características similares.

- 📓 [Notebook](./cereal_clustering_kmeans/cereal_clustering_kmeans.ipynb)
- 📖 [README](./cereal_clustering_kmeans/README.md)

---

### 3. [Análisis PCA de Vehículos](./pca_vehicle_analysis/)
**Técnicas**: Principal Component Analysis (PCA), Reducción de Dimensionalidad

Aplicación de PCA para reducir la dimensionalidad de características de vehículos y distinguir entre diferentes tipos de vehículos.

- 📓 [Notebook](./pca_vehicle_analysis/pca_vehicle_analysis.ipynb)
- 📖 [README](./pca_vehicle_analysis/README.md)

---

### 4. [Análisis Factorial de Récords Atléticos](./factor_analysis_athletics/)
**Técnicas**: Factor Analysis, Análisis de Componentes Latentes

Identificación de factores latentes en récords atléticos nacionales de mujeres para posicionar países según sus fortalezas.

- 📓 [Notebook](./factor_analysis_athletics/factor_analysis_athletics.ipynb)
- 📖 [README](./factor_analysis_athletics/README.md)

---

### 5. [Detección de Anomalías para Estrategias de Inversión](./anomaly_detection_investment_strategy/)
**Técnicas**: Detección de Anomalías, Isolation Forest, Análisis de Series Temporales

Uso de técnicas de detección de anomalías para validar estrategias de inversión en el mercado de valores mediante backtesting.

- 📓 [Notebook](./anomaly_detection_investment_strategy/anomaly_detection_investment_strategy.ipynb)
- 📖 [README](./anomaly_detection_investment_strategy/README.md)

---

### 6. [Clustering para Plan de Expansión de Tiendas](./clustering_store_expansion/)
**Técnicas**: K-Means, DBSCAN, Clustering Jerárquico, Análisis Geográfico

Aplicación de clustering para identificar áreas óptimas para la apertura de nuevos centros comerciales utilizando información censal.

- 📓 [Notebook](./clustering_store_expansion/clustering_store_expansion.ipynb)
- 📖 [README](./clustering_store_expansion/README.md)

---

### 7. [Análisis de Cesta de la Compra con Reglas de Asociación](./market_basket_analysis/)
**Técnicas**: Market Basket Analysis, Algoritmo Apriori, Reglas de Asociación

Análisis de cesta de la compra mediante reglas de asociación para identificar patrones de compra y relaciones entre productos.

- 📓 [Notebook](./market_basket_analysis/market_basket_analysis.ipynb)
- 📖 [README](./market_basket_analysis/README.md)

---

## 🛠️ Tecnologías y Herramientas

Los proyectos utilizan las siguientes tecnologías y librerías:

- **Python 3.7+**
- **pandas**: Manipulación y análisis de datos
- **numpy**: Operaciones numéricas
- **matplotlib & seaborn**: Visualización de datos
- **scikit-learn**: Algoritmos de machine learning
- **scipy**: Funciones científicas y estadísticas
- **prince**: Análisis de correspondencias
- **scikit-fda**: Análisis de datos funcionales
- **mlxtend**: Reglas de asociación
- **factor_analyzer**: Análisis factorial
- **folium**: Visualización geográfica

## 📋 Estructura del Repositorio

```
Machine Learning - No supervisado/
│
├── README.md (este archivo)
│
├── correspondence_analysis_functional_clustering/
│   ├── correspondence_analysis_functional_clustering.ipynb
│   ├── README.md
│   └── requirements.txt
│
├── cereal_clustering_kmeans/
│   ├── cereal_clustering_kmeans.ipynb
│   ├── README.md
│   └── requirements.txt
│
├── pca_vehicle_analysis/
│   ├── pca_vehicle_analysis.ipynb
│   ├── README.md
│   └── requirements.txt
│
├── factor_analysis_athletics/
│   ├── factor_analysis_athletics.ipynb
│   ├── README.md
│   └── requirements.txt
│
├── anomaly_detection_investment_strategy/
│   ├── anomaly_detection_investment_strategy.ipynb
│   ├── README.md
│   └── requirements.txt
│
├── clustering_store_expansion/
│   ├── clustering_store_expansion.ipynb
│   ├── README.md
│   └── requirements.txt
│
└── market_basket_analysis/
    ├── market_basket_analysis.ipynb
    ├── README.md
    └── requirements.txt
```

## 🚀 Cómo Usar Este Repositorio

### Requisitos Previos

- Python 3.7 o superior
- Jupyter Notebook o JupyterLab
- pip (gestor de paquetes de Python)

### Instalación

1. Clonar o descargar el repositorio
2. Navegar al directorio del proyecto deseado
3. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Abrir el notebook:
   ```bash
   jupyter notebook nombre_del_notebook.ipynb
   ```

### Ejecución

Cada proyecto es independiente y puede ejecutarse por separado. Los notebooks están diseñados para ser ejecutados secuencialmente desde el inicio hasta el final.

## 📊 Técnicas Cubiertas

Este portafolio demuestra la aplicación práctica de las siguientes técnicas de aprendizaje no supervisado:

- **Clustering**:
  - K-Means
  - DBSCAN
  - Clustering Jerárquico
  - Clustering Funcional

- **Reducción de Dimensionalidad**:
  - Principal Component Analysis (PCA)
  - Factor Analysis

- **Análisis de Correspondencias**:
  - Análisis de Correspondencias Simple (CA)

- **Análisis de Datos Funcionales**:
  - Functional Data Analysis (FDA)

- **Detección de Anomalías**:
  - Isolation Forest
  - Métodos basados en desviaciones estándar

- **Reglas de Asociación**:
  - Algoritmo Apriori
  - Market Basket Analysis

## 🎓 Aprendizajes Clave

Cada proyecto proporciona insights sobre:

- Preprocesamiento y limpieza de datos
- Selección y transformación de variables
- Aplicación de técnicas no supervisadas
- Interpretación de resultados
- Visualización de datos y resultados
- Validación de modelos y métricas

## 📝 Notas

- Todos los proyectos son independientes y pueden ejecutarse por separado
- Cada proyecto incluye su propio `requirements.txt` con las dependencias necesarias
- Los datasets utilizados están incluidos en cada carpeta o se proporcionan enlaces en los READMEs
- Los notebooks están completamente documentados y listos para ejecución

## 📄 Licencia

Este proyecto es de código abierto y está disponible para uso educativo y de investigación.

---

**Última actualización**: 2025

