# Predicción de Ventas Retail con Modelos Regresivos

## 📋 Descripción

Este proyecto desarrolla modelos de predicción de ventas para artículos específicos en retail utilizando técnicas de machine learning y optimización de hiperparámetros. El proyecto incluye exploración exhaustiva de datos, identificación de comportamientos y peculiaridades de artículos, y desarrollo de múltiples modelos regresivos optimizados.

## 🎯 Objetivo

El objetivo de este proyecto es usar un dataframe de ventas en retail para desarrollar un modelo de predicción de ventas para un artículo específico. Se explora el comportamiento del artículo elegido, se identifican sus peculiaridades, y se construye un modelo predictivo probando distintos algoritmos y optimizando hiperparámetros.

## 📊 Dataset

- **Dataframe_Retail.csv**: Dataset completo de ventas en retail con información de artículos y fechas

## 🛠️ Herramientas Utilizadas

- **Python** para desarrollo y análisis
- **Pandas** para manipulación y exploración de datos
- **NumPy** para operaciones numéricas
- **Scikit-learn** para modelos de machine learning:
  - DecisionTreeRegressor
  - GradientBoostingRegressor
  - KNeighborsRegressor
  - MLPRegressor
  - SVR
  - GridSearchCV y RandomizedSearchCV para optimización
- **Optuna** para optimización de hiperparámetros
- **Matplotlib/Seaborn** para visualizaciones
- **Jupyter Notebook** para análisis interactivo

## 📝 Temas Cubiertos

- Exploración de datos de ventas retail
- Análisis de comportamiento de artículos específicos
- Identificación de patrones y peculiaridades en datos de ventas
- Desarrollo de modelos regresivos
- Optimización de hiperparámetros con GridSearchCV y RandomizedSearchCV
- Optimización avanzada con Optuna
- Comparación de múltiples algoritmos de regresión
- Validación cruzada
- Evaluación de modelos predictivos
- Manejo de días sin ventas (valores cero)

## 🚀 Ejecución

### Requisitos Previos
- Python 3.x
- Dataset `Dataframe_Retail.csv` en el directorio del proyecto

### Instalación de Dependencias

Se recomienda crear un entorno virtual para este proyecto.

```bash
# Crear entorno virtual (opcional)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalación de librerías principales
pip install pandas numpy scikit-learn matplotlib seaborn optuna
```

### Ejecutar el Análisis

```bash
cd prediccion_ventas_retail
jupyter notebook prediccion_ventas_retail.ipynb
```

## 📄 Estructura del Proyecto

```
prediccion_ventas_retail/
├── prediccion_ventas_retail.ipynb
├── Dataframe_Retail.csv
└── README.md
```

## 📄 Licencia

Este portafolio es de carácter educativo y personal.

---

**Última actualización:** 2024

