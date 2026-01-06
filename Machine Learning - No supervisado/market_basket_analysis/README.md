# Reglas de Asociación para Análisis de Cesta de la Compra

[← Volver al índice](../README.md) | [📓 Ver Notebook](./market_basket_analysis.ipynb)

## Descripción

Este proyecto aplica técnicas de reglas de asociación para realizar un análisis de cesta de la compra (market basket analysis) a partir de datos de transacciones de un supermercado online. El objetivo es identificar patrones de compra, relaciones entre productos y generar insights para estrategias de marketing y recomendaciones.

## Objetivo

El objetivo principal es:
- Realizar un análisis de cesta de la compra mediante reglas de asociación
- Identificar productos que se compran frecuentemente juntos
- Descubrir patrones de compra de los clientes
- Generar recomendaciones de productos relacionados
- Optimizar estrategias de marketing y posicionamiento de productos

## Dataset

- **Archivo**: `data/Online Retail.xlsx`
- **Descripción**: Dataset de transacciones de un supermercado online
- **Período**: Datos históricos de transacciones
- **Países**: 38 países diferentes
- **Variables principales**:
  - `InvoiceNo`: Número de factura/transacción
  - `StockCode`: Código del producto
  - `Description`: Descripción del producto
  - `Quantity`: Cantidad comprada
  - `InvoiceDate`: Fecha de la transacción
  - `UnitPrice`: Precio unitario
  - `CustomerID`: Identificador del cliente
  - `Country`: País de la transacción

## Herramientas y Técnicas Empleadas

### Librerías de Python
- **pandas**: Manipulación y análisis de datos de transacciones
- **numpy**: Operaciones numéricas
- **matplotlib**: Visualización de datos
- **seaborn**: Visualizaciones estadísticas avanzadas
- **mlxtend**: Algoritmo Apriori y generación de reglas de asociación

### Técnicas Implementadas

1. **Market Basket Analysis**
   - Algoritmo Apriori para encontrar itemsets frecuentes
   - Generación de reglas de asociación
   - Cálculo de métricas (soporte, confianza, lift)

2. **Preprocesamiento de Datos**
   - Limpieza de datos de transacciones
   - Transformación a formato de matriz binaria (one-hot encoding)
   - Filtrado de transacciones válidas

3. **Análisis Exploratorio**
   - Análisis de distribución geográfica
   - Identificación de productos más vendidos
   - Análisis de frecuencia de transacciones

4. **Visualización**
   - Gráficos de productos más vendidos
   - Visualización de reglas de asociación
   - Análisis de métricas de reglas

## Temas Cubiertos

- **Reglas de asociación**: Fundamentos y aplicación práctica
- **Algoritmo Apriori**: Encontrar itemsets frecuentes
- **Market Basket Analysis**: Análisis de cesta de la compra
- **Métricas de reglas**: Soporte, confianza, lift
- **Aplicaciones en retail**: Recomendaciones y estrategias de marketing

## Ejecución

### Requisitos Previos

1. Python 3.7 o superior
2. Jupyter Notebook o JupyterLab
3. Instalación de dependencias (ver sección Dependencias)
4. Archivo de datos `Online Retail.xlsx` en la carpeta `data/`

### Pasos para Ejecutar

1. Clonar o descargar el repositorio
2. Navegar al directorio del proyecto:
   ```bash
   cd market_basket_analysis
   ```

3. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Asegurarse de que el archivo `data/Online Retail.xlsx` esté en el directorio correcto

5. Abrir el notebook:
   ```bash
   jupyter notebook market_basket_analysis.ipynb
   ```

6. Ejecutar las celdas en orden secuencial

## Dependencias

Las siguientes librerías son necesarias para ejecutar el proyecto:

```
pandas>=1.3.0
numpy>=1.21.0
matplotlib>=3.4.0
seaborn>=0.11.0
mlxtend>=0.22.0
openpyxl>=3.0.0
jupyter>=1.0.0
```

### Instalación de Dependencias

```bash
pip install pandas numpy matplotlib seaborn mlxtend openpyxl jupyter
```

## Cómo Usar

### Carga y Exploración de Datos

1. Cargar el dataset `Online Retail.xlsx`
2. Explorar la estructura de los datos
3. Analizar distribución geográfica (países)
4. Identificar productos más vendidos
5. Visualizar los 10 productos más frecuentes

### Preprocesamiento

1. Limpiar datos (eliminar valores nulos, transacciones inválidas)
2. Filtrar transacciones por país si es necesario
3. Transformar datos a formato de matriz binaria
4. Preparar datos para algoritmo Apriori

### Generación de Reglas de Asociación

1. Aplicar algoritmo Apriori para encontrar itemsets frecuentes
2. Definir umbral de soporte mínimo
3. Generar reglas de asociación
4. Filtrar reglas por confianza y lift
5. Analizar reglas más relevantes

### Análisis e Interpretación

1. Analizar reglas con mayor lift (mayor asociación)
2. Identificar productos que se compran frecuentemente juntos
3. Generar recomendaciones basadas en reglas
4. Visualizar reglas más importantes

## Resultados Obtenidos

### Análisis Exploratorio

- **Países**: 38 países diferentes en el dataset
- **País con más transacciones**: United Kingdom (495,478 transacciones)
- **Productos más frecuentes**: Se identifican los productos estrella del catálogo

### Reglas de Asociación Generadas

- **Itemsets frecuentes**: Conjuntos de productos que aparecen frecuentemente juntos
- **Reglas de asociación**: Relaciones del tipo "Si compra A, entonces compra B"
- **Métricas calculadas**:
  - **Soporte**: Frecuencia de aparición del itemset
  - **Confianza**: Probabilidad de comprar B dado que se compra A
  - **Lift**: Medida de la fuerza de la asociación

### Insights de Negocio

- **Productos complementarios**: Identificación de productos que se compran juntos
- **Oportunidades de cross-selling**: Productos para recomendar en conjunto
- **Estrategias de posicionamiento**: Ubicación óptima de productos relacionados
- **Bundling de productos**: Oportunidades para crear paquetes de productos

## Insights Clave

1. **Patrones de compra identificados**: Las reglas de asociación revelan patrones claros de comportamiento de compra que pueden ser utilizados para estrategias de marketing.

2. **Productos complementarios**: Se identifican productos que naturalmente se compran juntos, lo que permite crear estrategias de cross-selling efectivas.

3. **Métricas de calidad**: El lift es una métrica clave para identificar asociaciones realmente significativas, no solo coincidencias.

4. **Aplicaciones prácticas**: 
   - Recomendaciones de productos en e-commerce
   - Optimización de layout de tiendas físicas
   - Estrategias de descuentos y promociones
   - Creación de paquetes de productos

5. **Limitaciones**: Las reglas de asociación muestran correlaciones, no causalidades. Es importante validar las reglas con conocimiento del dominio.

## Estructura de Carpeta

```
market_basket_analysis/
│
├── market_basket_analysis.ipynb  # Notebook principal
├── data/
│   └── Online Retail.xlsx        # Dataset de transacciones
├── README.md                      # Este archivo
└── requirements.txt               # Dependencias
```

## Enlaces

- **📓 Notebook Principal**: [market_basket_analysis.ipynb](./market_basket_analysis.ipynb)
- **Dataset**: [data/Online Retail.xlsx](./data/Online Retail.xlsx)
- **Documentación mlxtend**: [https://rasbt.github.io/mlxtend/](https://rasbt.github.io/mlxtend/)
- **Dataset Online Retail**: Dataset público disponible en UCI Machine Learning Repository

## Licencia

Este proyecto es de código abierto y está disponible para uso educativo y de investigación.

---

**Nota**: Este proyecto demuestra la aplicación práctica de técnicas de reglas de asociación para análisis de retail, proporcionando una metodología para identificar patrones de compra y generar recomendaciones de productos basadas en datos reales de transacciones.

