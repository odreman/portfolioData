# Análisis de Series Temporales: Impacto de Madrid Central en la Calidad del Aire

[← Volver al Portafolio Python](../README.md) | [📓 Ver Notebook](./analisis-calidad-aire-madrid-central.ipynb)

## 📋 Descripción

Este proyecto analiza el impacto de la implementación de Madrid Central en la calidad del aire, específicamente en la concentración de dióxido de nitrógeno (NO2). Utilizando técnicas de análisis de series temporales con pandas, se examina cómo varió la presencia de NO2 antes y después de la entrada en vigor de esta medida de restricción de tráfico el 30 de noviembre de 2018.

## 🎯 Objetivo

Analizar cómo varió la presencia de dióxido de nitrógeno (NO2) en las mediciones realizadas por una estación de calidad del aire dentro de Madrid Central, en torno a la fecha en que se activó por primera vez la restricción.

**Pregunta de investigación:** ¿Disminuyó la concentración de NO2 en el aire tras la aplicación de Madrid Central?

## 📊 Datos

Los datos utilizados provienen del [Sistema Integral de la Calidad del Aire del Ayuntamiento de Madrid](https://datos.madrid.es/portal/site/egob/menuitem.c05c1f754a33a9fbe4b2e4b284f1a5a0/?vgnextoid=f3c0f7d512273410VgnVCM2000000c205a0aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD&vgnextfmt=default), que publica su portal de datos abiertos.

- **Período analizado:** 2018, 2019 y 2020
- **Estación de medición:** Plaza del Carmen (única estación dentro de Madrid Central)
- **Compuestos analizados:** NO2, CO, NO, NOx, O3

## 🛠️ Tecnologías Utilizadas

- **Python 3.x**
- **Pandas** - Manipulación y análisis de datos
- **NumPy** - Operaciones numéricas
- **Matplotlib** - Visualización de datos
- **GeoPandas** - Análisis geoespacial
- **Folium** - Visualización de mapas interactivos

## 📁 Estructura del Proyecto

```
analisis-calidad-aire-madrid-central/
├── analisis-calidad-aire-madrid-central.ipynb  # Notebook principal
├── Anio201810/                                 # Datos de 2018
├── Anio201912/                                 # Datos de 2019
├── Anio202009/                                 # Datos de 2020
├── estaciones.csv                              # Información de estaciones
├── Madrid_Central/                             # Shapefile de Madrid Central
├── Interprete_ficheros_ calidad_ del_ aire_global.pdf  # Documentación
└── README.md
```

## 🚀 Instalación

1. Clonar o descargar el repositorio
2. Instalar las dependencias:

```bash
pip install pandas numpy matplotlib geopandas folium shapely
```

O usando conda (recomendado para geopandas):

```bash
conda install geopandas folium
pip install pandas numpy matplotlib
```

## 📖 Metodología

El análisis se estructura en los siguientes pasos:

1. **Carga de datos:** Lectura y concatenación de todos los archivos CSV mensuales
2. **Filtrado:** Selección de datos de la estación "Plaza del Carmen"
3. **Transformación:** Reestructuración de datos de formato ancho a formato largo
4. **Indexación temporal:** Creación de índice de fecha y hora
5. **Análisis exploratorio:** Visualización de la evolución temporal del NO2
6. **Análisis comparativo:** Comparación de niveles antes y después de Madrid Central
7. **Análisis de reducción:** Cálculo de diferencias año a año

## 📈 Resultados Principales

El análisis incluye:

- Visualización de la evolución temporal del NO2 con marcador de la fecha de implementación
- Cálculo de medias móviles para identificar tendencias
- Análisis de reducción comparando cada día con el mismo día del año anterior
- Comparación de emisiones medias de diferentes gases entre años

## 📝 Uso

**📓 [Abrir Notebook](./analisis-calidad-aire-madrid-central.ipynb)**

Abrir el notebook `analisis-calidad-aire-madrid-central.ipynb` en Jupyter Notebook o JupyterLab y ejecutar las celdas en orden.

---

[← Volver al Portafolio Python](../README.md)

## 📄 Licencia

Este proyecto es de carácter educativo y utiliza datos públicos del Ayuntamiento de Madrid.

## 🔗 Referencias

- [Portal de Datos Abiertos del Ayuntamiento de Madrid](https://datos.madrid.es/)
- [Sistema Integral de la Calidad del Aire](https://datos.madrid.es/portal/site/egob/menuitem.c05c1f754a33a9fbe4b2e4b284f1a5a0/?vgnextoid=f3c0f7d512273410VgnVCM2000000c205a0aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD&vgnextfmt=default)


