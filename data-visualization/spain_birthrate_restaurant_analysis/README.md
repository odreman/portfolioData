# Análisis de Natalidad y Restaurantes en España

## 📋 Descripción
Este proyecto explora la relación entre las tasas de natalidad y la distribución de restaurantes con estrellas Michelin en las diferentes comunidades autónomas de España. Mediante el uso de datos geográficos y estadísticos, se analizan patrones y correlaciones inesperadas entre estos dos conjuntos de datos aparentemente no relacionados.

## 🎯 Objetivos

- Analizar la distribución geográfica de las tasas de natalidad en España
- Mapear la ubicación de restaurantes con estrellas Michelin
- Identificar posibles correlaciones entre desarrollo económico (representado por restaurantes de alta gama) y tasas de natalidad
- Visualizar los hallazgos mediante mapas interactivos y gráficos

## 📊 Datos

### Datos de Natalidad (`natalidad.geojson`)
- **NAME_1**: Nombre de la comunidad autónoma
- **NAME_2**: Nombre de la provincia
- **CC_2**: Código de la provincia
- **NAT2018**: Tasa de natalidad por cada 1,000 habitantes (2018)
- **geometry**: Datos geoespaciales para el mapeo

### Datos de Restaurantes Michelin (`one-star-michelin-restaurants.csv`)
- **name**: Nombre del restaurante
- **region**: Región donde se encuentra
- **city**: Ciudad de ubicación
- **cuisine**: Tipo de cocina
- **price**: Rango de precios
- **url**: Enlace al perfil del restaurante
- **longitude**: Longitud geográfica
- **latitude**: Latitud geográfica

## 🛠️ Herramientas Utilizadas

- **Python** para análisis de datos
- **GeoPandas** para manipulación de datos geoespaciales
- **Matplotlib** y **Seaborn** para visualizaciones
- **Contextily** para mapas base
- **Jupyter Notebook** para análisis interactivo

## 📂 Estructura del Proyecto

```
spain_birthrate_restaurant_analysis/
├── natalidad.geojson
├── one-star-michelin-restaurants.csv
├── two-stars-michelin-restaurants.csv
├── three-stars-michelin-restaurants.csv
├── analisis_natalidad_restaurantes.ipynb
└── README.md
```

## 📝 Hallazgos Clave

### Distribución de Natalidad
- Análisis de las tasas de natalidad por comunidad autónoma
- Identificación de regiones con tasas más altas y más bajas
- Evolución temporal de las tasas de natalidad

### Restaurantes Michelin
- Distribución geográfica de restaurantes con estrellas Michelin
- Relación entre densidad de restaurantes y desarrollo económico regional
- Tipos de cocina predominantes por región

### Correlaciones
- Análisis de posibles relaciones entre desarrollo económico (indicado por restaurantes de alta gama) y tasas de natalidad
- Comparación entre regiones turísticas y no turísticas
- Impacto de la urbanización en las tendencias demográficas

## 🚀 Cómo Ejecutar

1. Clona el repositorio
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Abre el notebook en Jupyter:
   ```bash
   jupyter notebook analisis_natalidad_restaurantes.ipynb
   ```

## 📝 Notas Adicionales

- Los datos de natalidad proceden del INE (Instituto Nacional de Estadística de España)
- Los datos de restaurantes Michelin se han obtenido de fuentes públicas
- El análisis incluye técnicas de limpieza y preparación de datos geoespaciales

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

## ✉️ Contacto

Para más información o colaboraciones, no dudes en contactarme.
