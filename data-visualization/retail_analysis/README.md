# Análisis de Retail: Vinos y Supermercados

## 📋 Descripción
Este proyecto incluye dos análisis principales:
1. **Análisis de Vinos**: Evaluación de vinos de diferentes regiones, con foco en precios, puntuaciones y relación calidad-precio.
2. **Análisis de Ventas de Supermercado**: Estudio de patrones de ventas, comportamiento del cliente y rendimiento de productos.

## 🎯 Objetivos

- Identificar las regiones vinícolas con los mejores vinos según puntuación y precio
- Analizar patrones de ventas en supermercados
- Determinar la relación entre precio y calidad de los vinos
- Identificar oportunidades de negocio en el sector minorista

## 📊 Datos

### Vinos
- `winemag-data-130k-v2.csv`: Base de datos con más de 130,000 vinos de todo el mundo
  - Incluye país, región, variedad, bodega, precio y puntuación

### Supermercado
- `supermarket_sales.csv`: Datos de transacciones de supermercados
  - Incluye información de ventas, productos, precios y datos demográficos de clientes

## 🛠️ Herramientas Utilizadas

- **Python** para análisis de datos
- **Pandas** para manipulación de datos
- **Matplotlib** y **Seaborn** para visualizaciones
- **Jupyter Notebook** para análisis interactivo
- **Funciones personalizadas** en `utils.py` para visualizaciones avanzadas

## 📂 Estructura del Proyecto

```
retail_analysis/
├── winemag-data-130k-v2.csv
├── supermarket_sales.csv
├── analisis_vinos_supermercados.ipynb
├── utils.py
└── README.md
```

## 📝 Hallazgos Clave

### Análisis de Vinos
- Identificación de las regiones con los vinos mejor puntuados
- Análisis de la relación precio-calidad
- Comparación entre países y regiones productoras

### Análisis de Supermercado
- Patrones de compra por ubicación
- Desempeño de diferentes líneas de productos
- Comportamiento del cliente por género y tipo (miembro/normal)

## 🚀 Cómo Ejecutar

1. Clona el repositorio
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Abre el notebook en Jupyter:
   ```bash
   jupyter notebook analisis_vinos_supermercados.ipynb
   ```

## 📝 Notas Adicionales

- Los datos de vinos incluyen información de más de 40 países
- El análisis de supermercado cubre múltiples ubicaciones
- Se incluyen visualizaciones interactivas para mejor exploración

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

## ✉️ Contacto

Para más información o colaboraciones, no dudes en contactarme.
