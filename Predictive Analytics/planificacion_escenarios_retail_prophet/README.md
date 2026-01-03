# Planificación de Escenarios Retail con Prophet

## 📋 Descripción

Este proyecto utiliza Prophet, una herramienta de Facebook para pronósticos de series temporales, para analizar el impacto del confinamiento en las ventas de una cadena de retail y planificar escenarios futuros. El proyecto trabaja con ventas de múltiples tiendas y categorías desde principios de 2018 hasta el final del confinamiento estricto.

## 🎯 Objetivo

Analizar el impacto del confinamiento en las ventas de una cadena de retail y desarrollar pronósticos para planificar escenarios futuros. El objetivo es mejorar el stockage de productos de distintas categorías y poder planificar mejor el futuro post-confinamiento utilizando Prophet para modelar y predecir las ventas.

## 📊 Dataset

- **Tabla Ventas Cats.csv**: Dataset con ventas de todas las tiendas de una cadena de retail en diferentes categorías desde principios de 2018 hasta el final del confinamiento estricto

## 🛠️ Herramientas Utilizadas

- **Python** para desarrollo y análisis
- **Pandas** para manipulación de datos temporales
- **NumPy** para operaciones numéricas
- **Prophet** (Facebook) para pronósticos de series temporales
- **Matplotlib** para visualizaciones
- **Jupyter Notebook** para análisis interactivo

## 📝 Temas Cubiertos

- Análisis de impacto de eventos externos (confinamiento) en ventas
- Modelado de series temporales con Prophet
- Pronósticos y planificación de escenarios futuros
- Análisis de múltiples categorías de productos
- Análisis de múltiples tiendas
- Visualización de evolución de ventas por categoría
- Planificación de stockage basada en pronósticos
- Análisis temporal desde 2018 hasta post-confinamiento

## 🚀 Ejecución

### Requisitos Previos
- Python 3.x
- Dataset `Tabla Ventas Cats.csv` en el directorio del proyecto

### Instalación de Dependencias

Se recomienda crear un entorno virtual para este proyecto.

```bash
# Crear entorno virtual (opcional)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalación de librerías principales
pip install pandas numpy matplotlib prophet
```

> [!NOTE]
> Prophet puede requerir dependencias adicionales. Si tienes problemas, consulta la [documentación oficial de Prophet](https://facebook.github.io/prophet/).

### Ejecutar el Análisis

```bash
cd planificacion_escenarios_retail_prophet
jupyter notebook planificacion_escenarios_retail_prophet.ipynb
```

## 📄 Estructura del Proyecto

```
planificacion_escenarios_retail_prophet/
├── planificacion_escenarios_retail_prophet.ipynb
├── Tabla Ventas Cats.csv
└── README.md
```

## 📄 Licencia

Este portafolio es de carácter educativo y personal.

---

**Última actualización:** 2024

