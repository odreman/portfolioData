# Detección de Anomalías para Estrategias de Inversión en Mercado de Valores

[← Volver al índice](../README.md) | [📓 Ver Notebook](./anomaly_detection_investment_strategy.ipynb)

## Descripción

Este proyecto explora el uso de técnicas de detección de anomalías para validar estrategias de inversión en el mercado de valores, específicamente aplicado a acciones del IBEX35. El objetivo es identificar puntos de entrada y salida basados en comportamientos anómalos de precios y evaluar la rentabilidad de una estrategia de trading mediante backtesting.

## Objetivo

El objetivo principal es:
- Utilizar técnicas de detección de anomalías para identificar fechas clave donde el precio se comporta de forma anómala
- Validar hipótesis sobre el comportamiento del precio después de anomalías (techos y suelos)
- Evaluar la rentabilidad de una estrategia de inversión mediante backtesting
- Comparar diferentes métodos de detección de anomalías (método sencillo vs Isolation Forest)

**Hipótesis de partida:**
- Las anomalías de tipo 'techo' (máximos anómalos) suelen ir seguidas de caídas en el precio
- Las anomalías de tipo 'suelo' (mínimos anómalos) suelen ir seguidas de subidas en el precio (3-5 días)

## Dataset

- **Archivos**: 
  - `historico_desde_2023_challenge_s3_plus.pkl`: Datos históricos de precios
  - `historico_desde_2023_challenge_s3_vprotocol4.pkl`: Datos adicionales (opcional)
- **Período**: 2 de Enero de 2023 hasta 21 de Enero de 2025
- **Valores analizados** (IBEX35):
  - BBVA (BBVA.MC)
  - IBERDROLA (IBE.MC)
  - INDITEX (ITX.MC)
  - SANTANDER (SAN.MC)
  - TELEFONICA (TEF.MC)
- **Variables disponibles**:
  - Adj Close: Precio de cierre ajustado
  - Close: Precio de cierre
  - High: Precio máximo del día
  - Low: Precio mínimo del día
  - Open: Precio de apertura
  - Volume: Volumen de transacciones

## Herramientas y Técnicas Empleadas

### Librerías de Python
- **pandas**: Manipulación y análisis de datos financieros
- **numpy**: Operaciones numéricas
- **matplotlib**: Visualización de series temporales
- **seaborn**: Visualizaciones estadísticas
- **scikit-learn**: Isolation Forest para detección de anomalías

### Técnicas Implementadas

1. **Detección de Anomalías**
   - Método sencillo basado en desviaciones estándar
   - Isolation Forest (método avanzado de machine learning)
   - Identificación de anomalías de tipo 'techo' y 'suelo'

2. **Análisis de Series Temporales**
   - Análisis de comportamiento post-anomalía
   - Identificación de patrones de reversión
   - Análisis de coincidencia de anomalías entre valores

3. **Backtesting**
   - Simulación de estrategia de inversión
   - Cálculo de rentabilidad
   - Evaluación de rendimiento de la estrategia

4. **Visualización**
   - Gráficos de series temporales con anomalías marcadas
   - Comparación de métodos de detección
   - Análisis de rentabilidad

## Temas Cubiertos

- **Detección de anomalías**: Técnicas para identificar comportamientos anómalos en series temporales financieras
- **Isolation Forest**: Algoritmo de machine learning para detección de outliers
- **Análisis técnico**: Identificación de puntos de entrada y salida
- **Backtesting**: Validación de estrategias de inversión con datos históricos
- **Análisis de rentabilidad**: Cálculo de ganancias/pérdidas de estrategias de trading

## Ejecución

### Requisitos Previos

1. Python 3.7 o superior
2. Jupyter Notebook o JupyterLab
3. Instalación de dependencias (ver sección Dependencias)
4. Archivos de datos históricos en formato pickle

### Pasos para Ejecutar

1. Clonar o descargar el repositorio
2. Navegar al directorio del proyecto:
   ```bash
   cd anomaly_detection_investment_strategy
   ```

3. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Asegurarse de que los archivos de datos históricos estén en el directorio

5. Abrir el notebook:
   ```bash
   jupyter notebook anomaly_detection_investment_strategy.ipynb
   ```

6. Ejecutar las celdas en orden secuencial

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

### Carga y Exploración de Datos

1. Cargar los datos históricos desde archivos pickle
2. Explorar la estructura del DataFrame (MultiIndex)
3. Seleccionar el período de análisis (2023-01-02 a 2025-01-21)
4. Extraer precios de cierre ajustados para análisis

### Detección de Anomalías

1. **Método sencillo**: 
   - Calcular desviaciones estándar
   - Identificar valores que exceden umbrales (ej: ±2 desviaciones estándar)
   - Clasificar como anomalías de 'techo' o 'suelo'

2. **Isolation Forest**:
   - Entrenar modelo con datos históricos
   - Identificar anomalías con mayor precisión
   - Comparar resultados con método sencillo

### Validación de la Estrategia

1. Analizar coincidencia de anomalías entre diferentes valores
2. Evaluar comportamiento post-anomalía (días siguientes)
3. Calcular porcentaje de veces que se cumple el comportamiento esperado
4. Realizar backtesting con inversión inicial de 10,000€
5. Calcular rentabilidad total de la estrategia

## Resultados Obtenidos

### Análisis de Anomalías

- **Coincidencia entre valores**: Se analiza si las anomalías ocurren en fechas similares entre diferentes acciones, lo que podría indicar eventos del mercado que afectan a múltiples valores.

- **Tipos de anomalías identificadas**:
  - Anomalías de 'techo': Máximos anómalos que potencialmente preceden caídas
  - Anomalías de 'suelo': Mínimos anómalos que potencialmente preceden subidas

### Validación del Comportamiento Esperado

- **Días de seguimiento**: Se evalúa el comportamiento del precio durante 3-5 días después de la anomalía
- **Porcentaje de éxito**: Se calcula en qué porcentaje de las ocasiones se produce el comportamiento esperado
- **Robustez del patrón**: Se analiza la consistencia del patrón a lo largo del tiempo

### Rentabilidad de la Estrategia

- **Inversión inicial**: 10,000€
- **Rentabilidad calculada**: Ganancia o pérdida total utilizando la estrategia
- **Comparación con buy-and-hold**: Se compara el rendimiento con una estrategia de comprar y mantener

### Comparación de Métodos

- **Método sencillo vs Isolation Forest**: Se comparan los resultados de ambos métodos en términos de:
  - Número de anomalías detectadas
  - Precisión en la identificación de puntos de reversión
  - Rentabilidad de la estrategia resultante

## Insights Clave

1. **Efectividad de la detección de anomalías**: Las técnicas de detección de anomalías pueden identificar puntos potenciales de reversión en el mercado.

2. **Diferencias entre métodos**: Isolation Forest puede proporcionar una detección más precisa que métodos basados en umbrales simples, aunque requiere más recursos computacionales.

3. **Coincidencia de anomalías**: Si múltiples valores muestran anomalías en fechas similares, esto puede indicar eventos macroeconómicos o del mercado que afectan al sector.

4. **Rentabilidad de la estrategia**: La estrategia basada en detección de anomalías puede ser rentable, pero requiere validación cuidadosa y gestión de riesgo.

5. **Limitaciones**: Las estrategias basadas en patrones históricos no garantizan resultados futuros. Es importante considerar factores adicionales como volatilidad, volumen y contexto del mercado.

## Estructura de Carpeta

```
anomaly_detection_investment_strategy/
│
├── anomaly_detection_investment_strategy.ipynb  # Notebook principal
├── historico_desde_2023_challenge_s3_plus.pkl  # Datos históricos
├── historico_desde_2023_challenge_s3_vprotocol4.pkl  # Datos adicionales
├── README.md                                    # Este archivo
└── requirements.txt                             # Dependencias
```

## Enlaces

- **📓 Notebook Principal**: [anomaly_detection_investment_strategy.ipynb](./anomaly_detection_investment_strategy.ipynb)
- **Documentación Isolation Forest**: [https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html)

## Advertencias

⚠️ **Importante**: Este proyecto es únicamente para fines educativos y de investigación. Las estrategias de inversión presentadas no constituyen asesoramiento financiero. El trading en mercados financieros conlleva riesgos significativos y puede resultar en pérdidas. Siempre consulte con un asesor financiero profesional antes de tomar decisiones de inversión.

## Licencia

Este proyecto es de código abierto y está disponible para uso educativo y de investigación.

---

**Nota**: Este proyecto demuestra la aplicación práctica de técnicas de detección de anomalías y machine learning para análisis de mercados financieros, proporcionando una base para el desarrollo de estrategias de trading más sofisticadas.

