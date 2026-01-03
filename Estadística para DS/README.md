# Portafolio de Estadística para Data Science

Bienvenido a mi portafolio de análisis estadísticos aplicados a la ciencia de datos. Este repositorio contiene una colección de análisis que demuestran habilidades en estadística, inferencia, regresión y visualización de datos utilizando Python.

## 📚 Análisis

### 1. [Análisis de Tweets: Introducción a Estadística y Análisis de Datos](./introduccion_nociones_basicas.ipynb)

**📓 Notebook:** [introduccion_nociones_basicas.ipynb](./introduccion_nociones_basicas.ipynb)

**Objetivo:** Introducir conceptos fundamentales de estadística y análisis de datos trabajando con datos reales de actividad en redes sociales durante eventos políticos importantes.

**Descripción:** Este análisis explora datos de tweets durante las elecciones americanas de 2020, analizando la distribución de actividad de usuarios en la plataforma X (Twitter). Se trabajan conceptos básicos de estadística descriptiva, visualización de distribuciones y técnicas de muestreo.

**Tecnologías utilizadas:**
- **Pandas** - Carga y manipulación de datos CSV
- **NumPy** - Operaciones numéricas
- **Matplotlib** - Visualización de histogramas y funciones de densidad

**Temas cubiertos:**
- Carga de datos desde URLs remotas
- Construcción de histogramas con funciones de densidad superpuestas
- Muestreo aleatorio simple (10% de la muestra)
- Comparación de estadísticas entre muestra completa y muestra reducida
- Reglas para determinar número óptimo de bins (Sturges, Freedman-Diaconis, Scott)

---

### 2. [Análisis de Datos Bursátiles: Estadística Descriptiva](./estadistica_descriptiva.ipynb)

**📓 Notebook:** [estadistica_descriptiva.ipynb](./estadistica_descriptiva.ipynb)

**Objetivo:** Aplicar técnicas de estadística descriptiva para analizar el comportamiento de datos financieros, específicamente incrementos diarios de acciones del IBEX.

**Descripción:** Este análisis trabaja con datos bursátiles de compañías españolas del IBEX, analizando incrementos diarios de precios. Se exploran medidas de tendencia central, dispersión, y se aplican técnicas avanzadas de visualización para entender patrones temporales en los mercados financieros.

**Tecnologías utilizadas:**
- **Pandas** - Manipulación de series temporales financieras
- **NumPy** - Cálculos estadísticos
- **Matplotlib** - Visualizaciones básicas
- **Seaborn** - Visualizaciones estadísticas avanzadas
- **Plotly** - Gráficos interactivos
- **Meteostat** - Datos meteorológicos (si aplica)

**Temas cubiertos:**
- Estadísticas descriptivas (media, mediana, desviación estándar)
- Medidas de tendencia central y dispersión
- Análisis de series temporales financieras
- Visualización de datos univariados
- Histogramas y gráficos de densidad
- Medias móviles para suavizado de datos

---

### 3. [Análisis Estadístico: Normalidad e Intervalos de Confianza](./normalidad_intervalos_confianza.ipynb)

**📓 Notebook:** [normalidad_intervalos_confianza.ipynb](./normalidad_intervalos_confianza.ipynb)

**Objetivo:** Aplicar pruebas estadísticas de normalidad y construir intervalos de confianza para realizar inferencias sobre poblaciones a partir de muestras.

**Descripción:** Este análisis explora conceptos avanzados de inferencia estadística, trabajando con datos de procesos de producción (tiempos de fabricación) y datos ambientales. Se aplican pruebas de normalidad (Shapiro-Wilk, Kolmogorov-Smirnov) y se construyen intervalos de confianza utilizando diferentes métodos, incluyendo bootstrap.

**Tecnologías utilizadas:**
- **Pandas** - Manipulación de datos
- **NumPy** - Operaciones numéricas y estadísticas
- **SciPy** - Pruebas estadísticas (normalidad, hipótesis)
- **Matplotlib** - Visualización de distribuciones
- **TQDM** - Barras de progreso para procesos iterativos

**Temas cubiertos:**
- Pruebas de normalidad (Shapiro-Wilk, Kolmogorov-Smirnov)
- Identificación de distribuciones bimodales
- Construcción de intervalos de confianza
- Método bootstrap para estimación de intervalos
- Comparación de desviaciones estándar entre grupos
- Inferencia estadística y toma de decisiones

---

### 4. [Análisis de Producción de Aceitunas: Variables por Parejas](./analisis_variables_parejas.ipynb)

**📓 Notebook:** [analisis_variables_parejas.ipynb](./analisis_variables_parejas.ipynb)

**Objetivo:** Explorar relaciones entre múltiples variables en un contexto agrícola, identificando correlaciones, patrones y dependencias entre factores que afectan la producción.

**Descripción:** Este análisis trabaja con datos de producción de aceitunas, incluyendo variables como temperatura, humedad, tipo de aceituna, campo de cultivo y recolector. Se analizan relaciones entre variables categóricas y numéricas, aplicando técnicas de visualización bivariada y pruebas estadísticas de asociación.

**Tecnologías utilizadas:**
- **Pandas** - Manipulación de datos con variables mixtas
- **NumPy** - Cálculos numéricos
- **Seaborn** - Visualizaciones bivariadas (heatmaps, violin plots, clustermaps)
- **Matplotlib** - Gráficos personalizados

**Temas cubiertos:**
- Clasificación de variables (categóricas, ordinales, intervalo, ratio)
- Visualización univariada de cada variable
- Heatmaps para tablas de contingencia
- Diagramas de violín para comparación de distribuciones
- Análisis de correlación numérica (matrices de correlación)
- Prueba de chi-cuadrado para variables categóricas
- Clustermaps para visualización de correlaciones
- Intervalos de confianza para medias por grupo

---

### 5. [Análisis de Pruebas PISA: Regresión Lineal](./regresion_lineal.ipynb)

**📓 Notebook:** [regresion_lineal.ipynb](./regresion_lineal.ipynb)

**Objetivo:** Construir y evaluar modelos de regresión lineal para predecir calificaciones educativas y analizar relaciones entre variables socioeconómicas y rendimiento académico.

**Descripción:** Este análisis implementa modelos de regresión lineal trabajando con datos de las pruebas PISA de múltiples países. Se exploran relaciones entre calificaciones en diferentes materias (matemáticas, lectura, ciencias), considerando también variables como renta per cápita y diferencias por género. Se evalúa la capacidad predictiva de los modelos y se interpretan los coeficientes.

**Tecnologías utilizadas:**
- **Pandas** - Manipulación de datos educativos
- **NumPy** - Operaciones numéricas
- **Statsmodels** - Modelado estadístico y regresión (OLS)
- **Matplotlib** - Visualización de modelos (gráficos 3D, residuos)

**Temas cubiertos:**
- Regresión lineal múltiple
- Predicción de calificaciones educativas
- Interpretación de coeficientes de regresión
- Visualización de modelos en 3D
- Evaluación de bondad del ajuste (R², p-valores)
- Métricas de evaluación (RMSE, BIAS, RME)
- Intervalos de confianza para predicciones
- Comparación de modelos con diferentes variables predictoras

---

### 6. [Análisis de la Tienda de Fortnite: Emotes y Bailes](./analisis_fortnite_emotes/analisis_emotes_fortnite.ipynb)

**📓 Notebook:** [analisis_emotes_fortnite.ipynb](./analisis_fortnite_emotes/analisis_emotes_fortnite.ipynb)

**Objetivo:** Analizar datos de la tienda de Fortnite, específicamente los emotes (bailes), para identificar patrones de popularidad, características y relaciones que puedan explicar el éxito de diferentes items.

**Descripción:** Este análisis explora un conjunto de datos complejo que combina información de la API de Fortnite, datos de scraping de FortniteGG, y características extraídas de videos (audio, reconocimiento de artistas). Se aplican técnicas de clustering, análisis de popularidad basado en votos de usuarios, y procesamiento de datos multimedia para entender qué factores influyen en la popularidad de los emotes.

**Tecnologías utilizadas:**
- **Pandas** - Manipulación de datos complejos (JSON, CSV)
- **NumPy** - Operaciones numéricas
- **Scikit-learn** - Clustering (KMeans), preprocesamiento (StandardScaler)
- **Matplotlib/Seaborn** - Visualización de resultados
- **TensorFlow/PyTorch** - Procesamiento de datos multimedia (si aplica)
- **OpenCV** - Procesamiento de imágenes/videos
- **Transformers** - Procesamiento de audio y reconocimiento

**Temas cubiertos:**
- Integración de datos de múltiples fuentes (API, scraping)
- Análisis de popularidad basado en votos de usuarios
- Clustering de items por características similares
- Extracción de características de audio/video
- Reconocimiento de artistas y canciones
- Análisis de patrones en datos de videojuegos
- Visualización de relaciones complejas entre variables

---

## 🛠️ Tecnologías Utilizadas

- **Python 3.x**
- **Pandas** - Manipulación y análisis de datos
- **NumPy** - Computación numérica
- **Matplotlib** - Visualización de datos
- **Seaborn** - Visualizaciones estadísticas avanzadas
- **SciPy** - Estadística y pruebas estadísticas
- **Statsmodels** - Modelado estadístico y regresión
- **Plotly** - Visualizaciones interactivas

## 📖 Temas Cubiertos

- Estadística descriptiva
- Distribuciones de probabilidad
- Pruebas de normalidad
- Intervalos de confianza
- Análisis de correlación
- Regresión lineal
- Visualización de datos
- Inferencia estadística

## 🚀 Cómo Navegar este Portafolio

Cada análisis es un notebook Jupyter independiente que contiene:
- Descripción del problema
- Análisis paso a paso
- Visualizaciones
- Interpretación de resultados

Para ejecutar un análisis:
```bash
cd "Estadística para DS"
jupyter notebook nombre_del_analisis.ipynb
```

## 📝 Notas

- Todos los análisis utilizan datos públicos o de ejemplo
- Los notebooks están listos para ejecutarse
- Cada análisis es independiente y puede ejecutarse por separado
- Los datos se cargan desde URLs públicas cuando es necesario

## 📄 Licencia

Este portafolio es de carácter educativo y personal.

---

**Última actualización:** 2024
