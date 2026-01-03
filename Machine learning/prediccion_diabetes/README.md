# Predicción de Diabetes con Regresión Logística

## 📋 Descripción

Este proyecto implementa un modelo de regresión logística para predecir la presencia de diabetes en pacientes basándose en características médicas. El proyecto incluye análisis exploratorio de datos, preprocesamiento, y evaluación del modelo con múltiples métricas.

## 🎯 Objetivo

Desarrollar un modelo de clasificación binaria para predecir si un paciente tiene diabetes (tested_positive) o no (tested_negative) utilizando regresión logística, una técnica fundamental de machine learning.

## 📊 Dataset

- **Dataset:** `data2.csv`
- **Variables:** 8 características médicas:
  - `preg`: Número de embarazos
  - `plas`: Concentración de glucosa en plasma
  - `pres`: Presión arterial diastólica
  - `skin`: Grosor del pliegue cutáneo del tríceps
  - `insu`: Insulina sérica de 2 horas
  - `mass`: Índice de masa corporal (BMI)
  - `pedi`: Función de pedigrí de diabetes
  - `age`: Edad
- **Variable objetivo:** `class` (tested_positive / tested_negative)

## 🛠️ Herramientas Utilizadas

- **Python** para desarrollo y análisis
- **Pandas** para manipulación de datos
- **NumPy** para operaciones numéricas
- **Scikit-learn** para:
  - LogisticRegression
  - StandardScaler
  - train_test_split
  - Métricas de evaluación
- **Matplotlib/Seaborn** para visualizaciones
- **Jupyter Notebook** para análisis interactivo

## 📝 Temas Cubiertos

- Análisis exploratorio de datos
- Visualización de distribuciones de variables
- División de datos en entrenamiento y test
- Preprocesamiento con StandardScaler
- Modelado con Regresión Logística
- Evaluación con múltiples métricas:
  - Accuracy
  - Precision
  - Recall
  - F1-Score
  - Matriz de confusión

## 🚀 Ejecución

### Requisitos Previos
- Python 3.x
- Dataset `data2.csv` en el directorio del proyecto

### Instalación de Dependencias

Se recomienda crear un entorno virtual para este proyecto.

```bash
# Crear entorno virtual (opcional)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalación de librerías principales
pip install pandas numpy scikit-learn matplotlib seaborn
```

### Ejecutar el Análisis

```bash
cd prediccion_diabetes
jupyter notebook prediccion_diabetes.ipynb
```

## 📄 Estructura del Proyecto

```
prediccion_diabetes/
├── prediccion_diabetes.ipynb
├── data2.csv
├── convert_to_csv.ipynb (utilidad para conversión de formato)
└── README.md
```

## 📄 Licencia

Este portafolio es de carácter educativo y personal.

---

**Última actualización:** 2024

