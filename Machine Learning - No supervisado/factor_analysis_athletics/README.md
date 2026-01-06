# Análisis Factorial de Récords Atléticos Femeninos

[← Volver al índice](../README.md) | [📓 Ver Notebook](./factor_analysis_athletics.ipynb)

## Descripción

Este proyecto aplica técnicas de Análisis Factorial para identificar factores latentes en los récords nacionales de mujeres en diferentes pruebas atléticas. El objetivo es simplificar el modelo de datos y realizar un análisis de posicionamiento de países según su rendimiento en factores identificados como "Resistencia" y "Velocidad".

## Objetivo

El objetivo principal es:
- Identificar factores latentes que expliquen las correlaciones entre diferentes pruebas atléticas
- Simplificar el modelo de datos reduciendo la dimensionalidad
- Realizar un gráfico de posicionamiento de países en relación a los factores extraídos
- Analizar el perfil atlético de diferentes países según su rendimiento en resistencia y velocidad

## Dataset

- **Archivo**: `women_records.csv`
- **Descripción**: Récords nacionales de mujeres que representan a 55 países en siete tipos de competiciones atléticas diferentes
- **Variables** (7 pruebas atléticas):
  - `X1`: 100 metros (segundos)
  - `X2`: 200 metros (segundos)
  - `X3`: 400 metros (segundos)
  - `X4`: 800 metros (minutos)
  - `X5`: 1500 metros (minutos)
  - `X6`: 3000 metros (minutos)
  - `X7`: Marathon (minutos)
- **Países**: 55 países representados

## Herramientas y Técnicas Empleadas

### Librerías de Python
- **pandas**: Manipulación y análisis de datos
- **numpy**: Operaciones numéricas
- **matplotlib**: Visualización de datos
- **seaborn**: Visualizaciones estadísticas avanzadas
- **scikit-learn**: StandardScaler para estandarización
- **factor_analyzer**: Análisis factorial, tests de idoneidad (KMO, Bartlett)
- **skimpy**: Exploración rápida de datos

### Técnicas Implementadas

1. **Análisis Factorial**
   - Validación de idoneidad (Test de Bartlett, KMO)
   - Determinación del número óptimo de factores (Scree Plot, criterio de Kaiser)
   - Rotación varimax para interpretación
   - Cálculo de cargas factoriales y comunalidades
   - Cálculo de puntuaciones factoriales

2. **Preprocesamiento de Datos**
   - Estandarización de variables
   - Análisis de correlaciones

3. **Visualización**
   - Matriz de correlaciones (heatmap)
   - Scree Plot
   - Matriz de cargas factoriales
   - Gráfico de comunalidades
   - Posicionamiento de países en espacio factorial

## Temas Cubiertos

- **Análisis Factorial**: Fundamentos teóricos y aplicación práctica
- **Validación de idoneidad**: Tests de Bartlett y KMO
- **Selección de factores**: Método del Scree Plot y criterio de Kaiser
- **Rotación de factores**: Rotación varimax para interpretación
- **Interpretación de factores**: Identificación de constructos latentes
- **Análisis de posicionamiento**: Visualización de observaciones en espacio factorial

## Ejecución

### Requisitos Previos

1. Python 3.7 o superior
2. Jupyter Notebook o JupyterLab
3. Instalación de dependencias (ver sección Dependencias)

### Pasos para Ejecutar

1. Clonar o descargar el repositorio
2. Navegar al directorio del proyecto:
   ```bash
   cd factor_analysis_athletics
   ```

3. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Abrir el notebook:
   ```bash
   jupyter notebook factor_analysis_athletics.ipynb
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
factor_analyzer>=0.4.0
skimpy>=0.0.1
jupyter>=1.0.0
```

### Instalación de Dependencias

```bash
pip install pandas numpy matplotlib seaborn scikit-learn factor_analyzer skimpy jupyter
```

## Cómo Usar

### Preprocesamiento

1. Cargar el dataset `women_records.csv`
2. Explorar la estructura de los datos
3. Estandarizar las variables numéricas
4. Analizar la matriz de correlaciones

### Validación de Idoneidad

1. Realizar Test de Bartlett (verificar correlaciones significativas)
2. Calcular índice KMO (verificar adecuación de los datos)
3. Evaluar si el análisis factorial es apropiado

### Análisis Factorial

1. Determinar número óptimo de factores (Scree Plot)
2. Aplicar análisis factorial con rotación varimax
3. Analizar cargas factoriales e interpretar factores
4. Calcular puntuaciones factoriales para cada país
5. Visualizar posicionamiento de países

## Resultados Obtenidos

### Validación de Idoneidad

- **Test de Bartlett**: Chi-cuadrado = 314.02, p-value < 0.001
  - Indica que las variables están significativamente correlacionadas
  - El análisis factorial es apropiado

- **Test KMO**: Score = 0.890
  - Valor excelente (superior a 0.7)
  - Indica que existe una estructura factorial clara en los datos

### Factores Identificados

**Factor 1 - RESISTENCIA (59.77% de varianza):**
- Representa la capacidad de resistencia aeróbica
- Alta correlación con pruebas de media y larga distancia:
  - 800 metros
  - 1500 metros
  - 3000 metros
  - Marathon

**Factor 2 - VELOCIDAD (20.18% de varianza):**
- Representa la capacidad de velocidad y potencia anaeróbica
- Alta correlación con pruebas cortas:
  - 100 metros
  - 200 metros

### Posicionamiento de Países

**Top 5 países en Resistencia:**
1. Western Samoa
2. Mauritius
3. Guatemala
4. Dominican Republic
5. Papua New Guinea

**Top 5 países en Velocidad:**
1. Cook Islands
2. Democratic People's Republic of Korea
3. Singapore
4. Luxembourg
5. Western Samoa

## Insights Clave

1. **Factores fisiológicos identificados**: Los dos factores identificados (Resistencia y Velocidad) tienen sentido desde el punto de vista fisiológico del rendimiento deportivo, representando diferentes sistemas energéticos.

2. **Diferenciación clara**: Se observa una clara diferenciación entre especialidades atléticas, con pruebas de velocidad y resistencia agrupándose en factores distintos.

3. **Patrones geográficos**: Los resultados muestran patrones que coinciden con la tradición histórica del atletismo, donde ciertos países destacan en resistencia y otros en velocidad.

4. **Países equilibrados**: Algunos países como Western Samoa muestran rendimiento en ambos factores, indicando programas de desarrollo atlético más equilibrados.

5. **Aplicabilidad del método**: El análisis factorial demuestra ser efectivo para identificar estructura latente en datos de rendimiento deportivo.

## Estructura de Carpeta

```
factor_analysis_athletics/
│
├── factor_analysis_athletics.ipynb  # Notebook principal
├── women_records.csv                # Dataset de récords atléticos
├── README.md                        # Este archivo
└── requirements.txt                 # Dependencias
```

## Enlaces

- **📓 Notebook Principal**: [factor_analysis_athletics.ipynb](./factor_analysis_athletics.ipynb)
- **Dataset**: [women_records.csv](./women_records.csv)
- **Documentación factor_analyzer**: [https://factor-analyzer.readthedocs.io/](https://factor-analyzer.readthedocs.io/)

## Licencia

Este proyecto es de código abierto y está disponible para uso educativo y de investigación.

---

**Nota**: Este proyecto demuestra la aplicación práctica del Análisis Factorial para identificar factores latentes en datos de rendimiento deportivo, proporcionando insights valiosos sobre el perfil atlético de diferentes países.

