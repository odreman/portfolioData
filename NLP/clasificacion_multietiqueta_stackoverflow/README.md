# Clasificación Multi-Etiqueta de Posts de StackOverflow

## 📋 Descripción

Este proyecto implementa un clasificador multi-etiqueta para predecir etiquetas de posts de StackOverflow. Es la segunda parte del proyecto, donde se entrenan y evalúan modelos de clasificación utilizando las features construidas en la primera parte.

## 🎯 Objetivo

Entrenar y evaluar modelos de clasificación multi-etiqueta que puedan predecir múltiples etiquetas para cada post de StackOverflow, trabajando con un dataset etiquetado con 100 etiquetas distintas.

## 📊 Dataset

- **Archivos:** 
  - `data/train.tsv` - Dataset de entrenamiento
  - `data/test.tsv` - Dataset de prueba
- **Estructura:** Títulos de posts de StackOverflow con etiquetas asociadas
- **Idioma:** Inglés
- **Etiquetas:** 100 etiquetas distintas posibles
- **Característica:** Cada post puede tener múltiples etiquetas (clasificación multi-etiqueta)

## 🛠️ Tecnologías Utilizadas

- **Scikit-learn** - Modelos de clasificación y evaluación
- **Pandas** - Manipulación de datos
- **NumPy** - Computación numérica
- **NLTK** - Procesamiento de texto (si se requiere preprocesamiento adicional)

## 📖 Temas Cubiertos

- Clasificación multi-etiqueta
- Entrenamiento de modelos de clasificación
- Evaluación de modelos multi-etiqueta
- Feature engineering para NLP
- Análisis de rendimiento de modelos
- Métricas específicas para clasificación multi-etiqueta

## 📁 Estructura del Proyecto

```
clasificacion_multietiqueta_stackoverflow/
├── README.md
└── 02_clasificador/
    ├── clasificacion_multietiqueta_stackoverflow.ipynb
    ├── data/
    │   ├── train.tsv
    │   └── test.tsv
    └── metrics.py
```

## 🚀 Ejecución

1. Asegúrate de tener instaladas las dependencias:
```bash
pip install pandas numpy scikit-learn nltk
```

2. **Importante**: Este proyecto utiliza las features construidas en la primera parte (preprocesamiento). Asegúrate de haber completado el preprocesamiento antes de ejecutar este notebook.

3. Abre el notebook `clasificacion_multietiqueta_stackoverflow.ipynb` en Jupyter

4. Ejecuta todas las celdas para entrenar y evaluar los modelos

## 📈 Resultados Clave

- Modelos entrenados para clasificación multi-etiqueta
- Evaluación del rendimiento de los modelos
- Análisis de qué etiquetas se predicen mejor
- Comparación de diferentes enfoques de clasificación
- Métricas de rendimiento específicas para multi-etiqueta

## 💡 Notas Importantes

- Este proyecto es la **segunda parte** de un sistema completo de clasificación
- Requiere las features construidas en la primera parte (preprocesamiento)
- La clasificación multi-etiqueta es más compleja que la clasificación simple, ya que cada post puede tener múltiples etiquetas
- Las métricas de evaluación son específicas para problemas multi-etiqueta

## 🔗 Enlaces

- [Notebook completo](02_clasificador/clasificacion_multietiqueta_stackoverflow.ipynb)
- [Primera parte: Preprocesamiento](../preprocesamiento_texto_stackoverflow/)
- [Volver al índice de NLP](../README.md)

