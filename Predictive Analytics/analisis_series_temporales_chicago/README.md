# Análisis de Series Temporales: Chicago

## 📋 Descripción

Este proyecto realiza un análisis completo de una serie temporal utilizando datos de alquileres de bicicletas en Chicago. El objetivo principal es identificar y eliminar los componentes de estacionalidad y tendencia de la serie temporal, trabajando con datos a nivel horario sin agrupar.

## 🎯 Objetivo

El objetivo de este proyecto es realizar el análisis de una serie temporal y eliminar sus componentes de estacionalidad y tendencia. Se utiliza el dataset de los alquileres de bicicletas de Chicago, específicamente el número de alquileres de los usuarios registrados, analizando los datos a nivel horario.

## 📊 Dataset

- **Dataset:** `hour_chicago.csv`
- **Tipo:** Serie temporal de alquileres de bicicletas
- **Ubicación:** Chicago
- **Granularidad:** Datos horarios (sin agrupar)
- **Variable objetivo:** Número de alquileres de usuarios registrados

## 🛠️ Herramientas Utilizadas

- **Python** para desarrollo y análisis
- **Pandas** para manipulación de datos temporales
- **NumPy** para operaciones numéricas
- **Matplotlib** para visualizaciones
- **Jupyter Notebook** para análisis interactivo

## 📝 Temas Cubiertos

- Análisis de series temporales
- Identificación de componentes de estacionalidad
- Identificación de tendencias
- Eliminación de componentes estacionales
- Eliminación de tendencias
- Preprocesamiento de datos temporales
- Visualización de series temporales

## 🚀 Ejecución

### Requisitos Previos
- Python 3.x
- Dataset `hour_chicago.csv` en el directorio del proyecto

### Instalación de Dependencias

Se recomienda crear un entorno virtual para este proyecto.

```bash
# Crear entorno virtual (opcional)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalación de librerías principales
pip install pandas numpy matplotlib
```

### Ejecutar el Análisis

```bash
cd analisis_series_temporales_chicago
jupyter notebook analisis_series_temporales_chicago.ipynb
```

## 📄 Estructura del Proyecto

```
analisis_series_temporales_chicago/
├── analisis_series_temporales_chicago.ipynb
├── hour_chicago.csv
└── README.md
```

## 📄 Licencia

Este portafolio es de carácter educativo y personal.

---

**Última actualización:** 2024

