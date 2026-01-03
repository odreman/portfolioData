# Anonimización de Datos: Airbnb Madrid

## 📋 Descripción

Este proyecto demuestra técnicas de anonimización de datos trabajando con un dataset real de Airbnb de la comunidad de Madrid. El objetivo es anonimizar los datos y transformarlos para que representen datos de Valladolid, aplicando técnicas de anonimización y transformación de datos geográficos mientras se preserva la privacidad de la información sensible.

## 🎯 Objetivos

- Aplicar técnicas de anonimización de datos personales y sensibles
- Transformar datos geográficos (coordenadas, códigos postales) de Madrid a Valladolid
- Preservar la estructura y utilidad de los datos durante el proceso de anonimización
- Analizar dependencias entre variables para una anonimización efectiva
- Implementar técnicas de procesamiento de lenguaje natural para anonimizar texto

## 📊 Datos

- `dataset_airbnb_madrid.csv`: Dataset con información de alojamientos de Airbnb en Madrid
  - Incluye: IDs, URLs, nombres, descripciones, precios, códigos postales, coordenadas geográficas

## 🛠️ Herramientas Utilizadas

- **Python** para análisis y transformación de datos
- **Pandas** para manipulación de datos
- **NumPy** para operaciones numéricas
- **Faker** para generación de datos sintéticos
- **SpaCy** para procesamiento de lenguaje natural y reconocimiento de entidades
- **Jupyter Notebook** para análisis interactivo

## 📂 Estructura del Proyecto

```
anonimizacion_airbnb/
├── dataset_airbnb_madrid.csv
├── anonimizacion_airbnb.ipynb
└── README.md
```

## 🔍 Técnicas Aplicadas

### Anonimización de Identificadores
- Reordenamiento aleatorio del dataset
- Asignación de nuevos IDs secuenciales
- Actualización de URLs para reflejar nuevos IDs

### Anonimización de Precios
- Generalización de precios en rangos
- Mantenimiento de coherencia entre precio diario y semanal
- Preservación de información agregada para análisis

### Anonimización Geográfica
- Reducción de precisión de coordenadas (redondeo a 1 decimal)
- Generalización de códigos postales (primeros 2 dígitos)
- Transformación de ubicaciones de Madrid a Valladolid

### Anonimización de Texto
- Reconocimiento de entidades nombradas (NER) con SpaCy
- Reemplazo de nombres de personas, lugares y organizaciones
- Generación de pseudónimos coherentes con Faker

## 📝 Temas Cubiertos

- Análisis de dependencias entre variables
- Estrategias de anonimización por tipo de dato
- Procesamiento de lenguaje natural para anonimización
- Transformación de datos geográficos
- Preservación de utilidad de datos durante anonimización

## 🚀 Ejecución

Para ejecutar el análisis:

```bash
cd anonimizacion_airbnb
jupyter notebook anonimizacion_airbnb.ipynb
```

## 📄 Notas

- El dataset original se mantiene intacto
- Todas las transformaciones se aplican a una copia del dataset
- El proceso de anonimización preserva la estructura de los datos para análisis posteriores

