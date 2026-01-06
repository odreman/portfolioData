# Reducción de Dimensionalidad con PCA para Análisis de Vehículos

[← Volver al índice](../README.md) | [📓 Ver Notebook](./pca_vehicle_analysis.ipynb)

## Descripción

Este proyecto aplica la técnica de Análisis de Componentes Principales (PCA) para reducir la dimensionalidad de un dataset con características de distintos modelos de vehículos. El objetivo es visualizar y analizar las diferencias entre todoterrenos (Cars) y turismos (Passenger) en un espacio de dimensiones reducidas, conservando la mayor parte de la información original.

## Objetivo

El objetivo principal es:
- Reducir la dimensionalidad de un dataset con múltiples características de vehículos
- Identificar las componentes principales que capturan la mayor variabilidad
- Evaluar si los diferentes tipos de vehículos (todoterrenos y turismos) quedan identificados en el espacio reducido
- Interpretar el significado de las componentes principales en términos de las variables originales

## Dataset

- **Archivo**: `Car_sales.csv`
- **Descripción**: Dataset con características de 157 modelos de vehículos
- **Variables principales** (15 en total):
  - `Manufacturer`: Fabricante del vehículo
  - `Model`: Modelo del vehículo
  - `Sales_in_thousands`: Ventas en miles
  - `4_year_resale_value`: Valor de reventa a 4 años
  - `Vehicle_type`: Tipo de vehículo (Car/Passenger)
  - `Price_in_thousands`: Precio en miles
  - `Engine_size`: Tamaño del motor
  - `Horsepower`: Potencia
  - `Wheelbase`: Distancia entre ejes
  - `Width`: Ancho
  - `Length`: Longitud
  - `Curb_weight`: Peso
  - `Fuel_capacity`: Capacidad de combustible
  - `Fuel_efficiency`: Eficiencia de combustible
  - `Latest_Launch`: Último lanzamiento

## Herramientas y Técnicas Empleadas

### Librerías de Python
- **pandas**: Manipulación y análisis de datos
- **numpy**: Operaciones numéricas
- **matplotlib**: Visualización de datos (2D y 3D)
- **seaborn**: Visualizaciones estadísticas avanzadas
- **scikit-learn**: PCA, StandardScaler

### Técnicas Implementadas

1. **Análisis de Componentes Principales (PCA)**
   - Reducción de dimensionalidad de 10 a 3 variables
   - Método del codo para determinar número óptimo de componentes
   - Análisis de varianza explicada
   - Interpretación de componentes mediante loadings y correlaciones

2. **Preprocesamiento de Datos**
   - Limpieza de nombres de variables
   - Conversión de tipos de datos
   - Tratamiento de valores faltantes (imputación con mediana/media)
   - Estandarización de variables (StandardScaler)

3. **Análisis Exploratorio**
   - Análisis de distribuciones
   - Matriz de correlaciones
   - Visualización de datos en 2D y 3D
   - Validación con casos de prueba

## Temas Cubiertos

- **PCA**: Fundamentos teóricos y aplicación práctica
- **Reducción de dimensionalidad**: De 10 variables a 3 componentes principales
- **Estandarización de datos**: Importancia y aplicación
- **Análisis de varianza explicada**: Método del codo y selección de componentes
- **Interpretación de componentes**: Relación con variables originales
- **Visualización multidimensional**: Representación en espacios reducidos

## Ejecución

### Requisitos Previos

1. Python 3.7 o superior
2. Jupyter Notebook o JupyterLab
3. Instalación de dependencias (ver sección Dependencias)

### Pasos para Ejecutar

1. Clonar o descargar el repositorio
2. Navegar al directorio del proyecto:
   ```bash
   cd pca_vehicle_analysis
   ```

3. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Abrir el notebook:
   ```bash
   jupyter notebook pca_vehicle_analysis.ipynb
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

### Preprocesamiento

1. Cargar el dataset `Car_sales.csv`
2. Limpiar nombres de variables (eliminar espacios)
3. Convertir tipos de datos apropiados
4. Tratar valores faltantes (imputación)
5. Estandarizar variables numéricas

### Aplicación de PCA

1. Seleccionar variables numéricas para PCA (10 variables)
2. Aplicar método del codo para determinar número óptimo de componentes
3. Aplicar PCA con 3 componentes (86.61% de varianza explicada)
4. Visualizar resultados en 2D y 3D
5. Interpretar componentes mediante correlaciones

### Validación

1. Seleccionar casos de prueba (uno de cada tipo de vehículo)
2. Transformar casos de prueba al espacio PCA
3. Evaluar capacidad de clasificación

## Resultados Obtenidos

### Reducción de Dimensionalidad

- **Variables iniciales**: 10 variables numéricas
- **Componentes seleccionadas**: 3 componentes principales
- **Varianza explicada**:
  - PC1: 59.77% (tamaño y potencia del vehículo)
  - PC2: 20.18% (aspectos económicos y dimensiones)
  - PC3: 6.66% (eficiencia y características adicionales)
- **Varianza total conservada**: 86.61%

### Interpretación de Componentes

**Primera Componente (PC1) - 59.77%:**
- Representa principalmente el tamaño y potencia del vehículo
- Variables más importantes: Curb_weight (0.911), Engine_size (0.894), Fuel_capacity (0.853)
- Valores positivos: vehículos grandes y potentes (típico de Cars)
- Valores negativos: vehículos pequeños y menos potentes (típico de Passenger)

**Segunda Componente (PC2) - 20.18%:**
- Representa aspectos económicos y algunas dimensiones
- Variables más importantes: 4_year_resale_value (0.761), Price_in_thousands (0.665)
- Menos útil para distinguir entre tipos de vehículos

**Tercera Componente (PC3) - 6.66%:**
- Relacionada con eficiencia y características adicionales
- Muestra mejor separación entre Cars (valores negativos) y Passenger (valores positivos)

### Separación de Grupos

- **PC1 vs PC2**: Separación moderada con solapamiento considerable
- **PC1 vs PC3**: Mejor separación, menor solapamiento
- **PC2 vs PC3**: Separación más clara entre grupos
- **Visualización 3D**: La combinación de las tres componentes ayuda a distinguir mejor los grupos

## Insights Clave

1. **Reducción efectiva**: Se logró reducir de 10 dimensiones a 3, conservando más del 85% de la varianza.

2. **PC1 como diferenciador principal**: La primera componente es la más efectiva para distinguir entre tipos de vehículos, representando principalmente tamaño y potencia.

3. **Solapamiento entre categorías**: Existe solapamiento entre Cars y Passenger, indicando características compartidas. Esto es esperado ya que algunos vehículos pueden tener características intermedias.

4. **Casos extremos**: Los casos extremos (como Cadillac Escalade) son más fáciles de clasificar que los casos intermedios (como Acura Integra).

5. **Correlaciones identificadas**: Se identificaron altas correlaciones entre variables relacionadas (tamaño, potencia, eficiencia), lo que justifica la efectividad de PCA.

6. **Aplicaciones prácticas**: PCA es útil para visualización, reducción de ruido, y preprocesamiento para algoritmos de machine learning.

## Estructura de Carpeta

```
pca_vehicle_analysis/
│
├── pca_vehicle_analysis.ipynb  # Notebook principal
├── Car_sales.csv                # Dataset de vehículos
├── coches.jpeg                  # Imagen ilustrativa
├── README.md                    # Este archivo
└── requirements.txt             # Dependencias
```

## Enlaces

- **📓 Notebook Principal**: [pca_vehicle_analysis.ipynb](./pca_vehicle_analysis.ipynb)
- **Dataset**: [Car_sales.csv](./Car_sales.csv)
- **Documentación scikit-learn PCA**: [https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)

## Licencia

Este proyecto es de código abierto y está disponible para uso educativo y de investigación.

---

**Nota**: Este proyecto demuestra la aplicación práctica de técnicas de reducción de dimensionalidad para análisis exploratorio y visualización de datos de alta dimensionalidad.

